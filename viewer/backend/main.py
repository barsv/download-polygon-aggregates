import os
import sys
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from datetime import datetime
import io
import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.dataset as ds

from viewer.backend import main_service

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import settings
from download_all_bars import load_ticker_details

app = FastAPI()

ticker_details_df = None
sorted_tickers = None

@app.get("/api/tickers")
async def get_tickers(search: str = None):
    global ticker_details_df, sorted_tickers
    if ticker_details_df is None:
        ticker_details_df = load_ticker_details()
        if ticker_details_df is not None:
            sorted_by_market_cap = ticker_details_df.sort_values('market_cap', ascending=False, na_position='last')
            sorted_tickers = sorted_by_market_cap['ticker'].tolist()
    if sorted_tickers is None:
        return {"error": "Ticker details not found or failed to process"}
    if search:
        search_lower = search.lower()
        filtered_tickers = [t for t in sorted_tickers if t.lower().startswith(search_lower)]
    else:
        filtered_tickers = sorted_tickers
    return {"tickers": filtered_tickers[:20]}

@app.get("/api/bars/{ticker}")
async def get_bars(ticker: str, timestamp: int = None, direction = "", interval: str = "1s"):
    """
    Get bars for a ticker with specified interval.
    
    Args:
        interval: Resample rule (e.g., '1s', '5s', '1min', '5min', '1h', '4h', '1d', '1w')
    """
    if not main_service.validate_resample_rule(interval):
        return {"error": f"Unsupported interval: {interval}"}
    
    # Determine if we need seconds or minutes data
    interval_seconds = main_service.resample_rule_to_seconds(interval)
    
    if interval_seconds < 60:
        # Use seconds data
        df = main_service.get_aggregated_seconds_df(ticker, interval, timestamp, direction)
    else:
        # Use minutes data
        df = main_service.get_aggregated_minutes_df(ticker, interval, timestamp, direction)
    
    # Rename timestamp column to time for lightweight-charts.js
    df.rename(columns={'timestamp': 'time'}, inplace=True)
    result = {"ticker": ticker, "bars": df.to_dict(orient='records')}
    return result

@app.get("/api/download/files/{ticker}")
async def get_download_files(ticker: str, interval: str = "1s"):
    if not main_service.validate_resample_rule(interval):
        return {"error": f"Unsupported interval: {interval}"}
    
    interval_seconds = main_service.resample_rule_to_seconds(interval)
    
    if interval_seconds < 60:
        # For seconds, return yearly files
        bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
        if not os.path.exists(bars_dir):
            return {"error": "Bars data not found for this ticker"}
        parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])
        return {"files": parquet_files}
    else:
        # For minute+ periods, return a single aggregated file option
        bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
        file_path = os.path.join(bars_dir, f"{ticker}.parquet")
        if not os.path.exists(file_path):
            # Try to aggregate from seconds data
            seconds_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
            if not os.path.exists(seconds_dir):
                return {"error": "No data found for this ticker"}
        
        # Generate a virtual filename for the aggregated data
        virtual_filename = f"{ticker}_{interval}.parquet"
        return {"files": [virtual_filename]}

@app.get("/api/download/file/{ticker}/{filename}")
async def download_file(ticker: str, filename: str, format: str = "parquet", time_format: str = None, interval: str = "1s"):
    try:
        if not main_service.validate_resample_rule(interval):
            return {"error": f"Unsupported interval: {interval}"}
        if format not in ["parquet", "csv"]:
            return {"error": f"Unsupported format: {format}"}
        # check that ticker is alphanumeric or dots, dashes, underscores
        if not ticker.replace('.', '').replace('-', '').replace('_', '').isalnum():
            return {"error": "Ticker is not valid"}
        
        interval_seconds = main_service.resample_rule_to_seconds(interval)
        
        # load file
        if interval_seconds < 60:
            # get year from filename
            year = filename.split('.')[0].split('_')[-1]
            # check that 'year' is an int between 2003 and 2050
            if not year.isdigit() or not (2003 <= int(year) <= 2050):
                return {"error": "Year is not valid"}
            bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
            file_path = os.path.join(bars_dir, f"{year}.parquet")
        else:
            bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
            file_path = os.path.join(bars_dir, f"{ticker}.parquet")
        
        if not os.path.exists(file_path):
            return {"error": "File not found"}
        df = pd.read_parquet(file_path)
        
        # aggregate
        if interval_seconds < 60:
            if interval != "1s":
                df = main_service.aggregate_ohlc_data(df, interval)
        else:
            df.reset_index(inplace=True)
            df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
            if interval != "1min":
                df = main_service.aggregate_ohlc_data(df, interval)
        
        # return the file
        if interval_seconds < 60:
            result_filename = f"{ticker}_{interval}_{year}.{format}"
        else:
            result_filename = f"{ticker}_{interval}.{format}"
            
        headers = {'Content-Disposition': f'attachment; filename="{result_filename}"'}
        if format == "parquet":
            output = io.BytesIO()
            table = pa.table(df)
            pq.write_table(table, output)
            output.seek(0)
            return StreamingResponse(output, media_type="application/octet-stream", headers=headers)
        elif format == "csv":
            if time_format and time_format != 'timestamp':
                # Convert Python datetime format to pandas format
                pandas_format = time_format \
                    .replace('yyyy', '%Y') \
                    .replace('MM', '%m') \
                    .replace('dd', '%d') \
                    .replace('HH', '%H') \
                    .replace('mm', '%M') \
                    .replace('ss', '%S') \
                    .replace('fff', '%f')
                # Convert timestamp to datetime and format
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.strftime(pandas_format)
            output = io.StringIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return StreamingResponse(io.BytesIO(output.getvalue().encode('utf-8')), media_type="text/csv", headers=headers)
        else:
            return {"error": "Unsupported format"}
    except Exception as e:
        return {"error": f"Download failed: {str(e)}"}