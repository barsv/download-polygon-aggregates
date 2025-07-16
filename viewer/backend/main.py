import os
import sys
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from datetime import datetime
import io
import pyarrow.parquet as pq
import pyarrow as pa

# Configuration
LIMIT = 3000

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import settings
from aggregate_bars import aggregate_bars

app = FastAPI()

ticker_details_df = None
sorted_tickers = None

def load_ticker_details():
    """Load ticker details from the CSV file."""
    tickers_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')
    ticker_details_file = os.path.join(tickers_dir, 'ticker_details.csv')
    if not os.path.exists(ticker_details_file):
        return None
    try:
        df = pd.read_csv(ticker_details_file)
        return df
    except Exception as e:
        print(f"Error reading ticker details file: {e}")
        return None

def _get_aggregated_minutes_df(ticker: str, minutes: int, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load minute bars and aggregate to specified minute interval on-the-fly."""
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
    file_path = os.path.join(bars_dir, f"{ticker}.parquet")
    if not os.path.exists(file_path):
        aggregate_bars(ticker)
        if not os.path.exists(file_path):
            return None
    required_columns = ['timestamp', 'open', 'high', 'low', 'close']
    # Use PyArrow for faster reading
    table = pq.read_table(file_path, columns=required_columns)
    df = table.to_pandas()
    # Pre-filter minute data to reduce processing
    minute_limit = LIMIT * minutes
    if timestamp is not None:
        try:
            pos = df.index.get_loc(timestamp)
        except KeyError:
            # Fallback: find position using searchsorted
            pos = df.index.searchsorted(timestamp)
            pos = min(pos, len(df) - 1)
        if direction == "backward":
            start_pos = max(0, pos - minute_limit + 1)
            df = df.iloc[start_pos:pos]
        elif direction == "forward":
            end_pos = min(len(df), pos + minute_limit)
            df = df.iloc[pos:end_pos]
        elif direction == "both":
            start_pos = max(0, pos - minute_limit // 2)
            end_pos = min(len(df), pos + minute_limit // 2)
            df = df.iloc[start_pos:end_pos]
    else:
        df = df.tail(minute_limit)
    # If minutes == 1, skip resampling (already 1-minute data)
    if minutes == 1:
        df_result = df
    else:
        # Convert timestamp index to datetime for resampling (only filtered data)
        df.index = pd.to_datetime(df.index, unit='s')
        # Resample to specified minute interval
        resample_rule = f'{minutes}Min'
        df_result = df.resample(resample_rule).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last'
        }).dropna()
        # Convert back to timestamp index in seconds
        df_result.index = (df_result.index.astype(int) // 10**9)
    # when we request forward data we pass the timestamp of the last visible bar, 
    # hence we need to drop the first bar because it already exists on the chart.
    if direction == "forward":
        df_result = df_result.iloc[1:]
    # Reset index to get timestamp as column
    df_result.reset_index(inplace=True)
    df_result.rename(columns={df_result.columns[0]: 'time'}, inplace=True)
    return df_result

def _get_aggregated_seconds_df(ticker: str, seconds: int, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load second bars and aggregate to specified second interval on-the-fly."""
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return None
    all_parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])
    files_to_read = []
    if timestamp:
        target_year = datetime.fromtimestamp(timestamp).year
        file_name = f"{target_year}.parquet"
        if file_name in all_parquet_files:
            files_to_read.append(os.path.join(bars_dir, file_name))
        # If direction is 'both' and data spans across year boundaries, consider adjacent years
        if direction == "both":
            prev_year_file = f"{target_year - 1}.parquet"
            if prev_year_file in all_parquet_files and os.path.join(bars_dir, prev_year_file) not in files_to_read:
                files_to_read.insert(0, os.path.join(bars_dir, prev_year_file))
            next_year_file = f"{target_year + 1}.parquet"
            if next_year_file in all_parquet_files and os.path.join(bars_dir, next_year_file) not in files_to_read:
                files_to_read.append(os.path.join(bars_dir, next_year_file))
    elif all_parquet_files:
        files_to_read.append(os.path.join(bars_dir, all_parquet_files[-1]))
    if not files_to_read:
        return None
    required_columns = ['timestamp', 'open', 'high', 'low', 'close']
    df = pd.concat([pd.read_parquet(f, columns=required_columns) for f in files_to_read], ignore_index=True)
    # Pre-filter second data to reduce processing
    second_limit = LIMIT * seconds
    if timestamp is not None:
        if direction == "backward":
            idx = df['timestamp'].searchsorted(timestamp, side='right')
            start_idx = max(0, idx - second_limit)
            df = df.iloc[start_idx:idx - 1]
        elif direction == "forward":
            idx = df['timestamp'].searchsorted(timestamp, side='left')
            df = df.iloc[idx:idx + second_limit]
        elif direction == "both":
            idx = df['timestamp'].searchsorted(timestamp, side='left')
            start_idx = max(0, idx - second_limit // 2)
            end_idx = min(len(df), idx + second_limit // 2)
            df = df.iloc[start_idx:end_idx]
    else:
        df = df.tail(second_limit)
    # If seconds == 1, skip resampling (already 1-second data)
    if seconds == 1:
        df_result = df
    else:
        # Convert timestamp to datetime for resampling
        df['timestamp_dt'] = pd.to_datetime(df['timestamp'], unit='s')
        df.set_index('timestamp_dt', inplace=True)
        # Resample to specified second interval
        resample_rule = f'{seconds}S'
        df_result = df.resample(resample_rule).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last'
        }).dropna()
        # Convert back to timestamp
        df_result['timestamp'] = (df_result.index.astype(int) // 10**9)
        df_result.reset_index(drop=True, inplace=True)
    # when we request forward data we pass the timestamp of the last visible bar, 
    # hence we need to drop the first bar because it already exists on the chart.
    if direction == "forward":
        df_result = df_result.iloc[1:]
    # Rename timestamp column to time
    df_result.rename(columns={'timestamp': 'time'}, inplace=True)
    return df_result

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
        return {"tickers": filtered_tickers[:50]}
    else:
        return {"tickers": sorted_tickers[:100]}

@app.get("/api/bars/{ticker}")
async def get_bars(ticker: str, timestamp: int = None, direction = "", period: str = "second", multiplier: int = 1):
    """
    Get bars for a ticker with flexible period and multiplier.
    
    Args:
        period: 'second', 'minute', 'hour', 'day', 'week'
        multiplier: integer multiplier (e.g., 5 for 5-minute bars)
    """
    
    if period == "second":
        df = _get_aggregated_seconds_df(ticker, multiplier, timestamp, direction)
    elif period in ["minute", "hour", "day", "week"]:
        # Convert period to minutes
        period_to_minutes = {
            "minute": 1,
            "hour": 60,
            "day": 1440,
            "week": 10080
        }
        total_minutes = period_to_minutes[period] * multiplier
        df = _get_aggregated_minutes_df(ticker, total_minutes, timestamp, direction)
    else:
        return {"error": f"Unsupported period: {period} with multiplier: {multiplier}"}
        
    result = {"ticker": ticker, "bars": df.to_dict(orient='records')}
    
    return result

@app.get("/api/download/files/{ticker}")
async def get_download_files(ticker: str):
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return {"error": "Bars data not found for this ticker"}
    
    parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])
    return {"files": parquet_files}

@app.get("/api/download/file/{ticker}/{filename}")
async def download_file(ticker: str, filename: str, format: str = "parquet", time_format: str = None):
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    file_path = os.path.join(bars_dir, filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    if format == "parquet":
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    elif format == "csv":
        try:
            df = pd.read_parquet(file_path)
            
            # Format time column if time_format is provided and not 'timestamp'
            if time_format and time_format != 'timestamp':
                try:
                    # Convert Python datetime format to pandas format
                    pandas_format = time_format.replace('yyyy', '%Y').replace('MM', '%m').replace('dd', '%d').replace('HH', '%H').replace('mm', '%M').replace('ss', '%S').replace('fff', '%f')
                    # Convert timestamp to datetime and format
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.strftime(pandas_format)
                except Exception as e:
                    return {"error": f"Failed to format time to {time_format} ({pandas_format}): {e}"}
            
            output = io.StringIO()
            df.to_csv(output, index=False)
            output.seek(0)
            csv_filename = filename.replace(".parquet", ".csv")
            return StreamingResponse(io.BytesIO(output.getvalue().encode('utf-8')), media_type="text/csv", headers={'Content-Disposition': f'attachment; filename="{csv_filename}"'})
        except Exception as e:
            return {"error": f"Error converting to CSV: {e}"}
    else:
        return {"error": "Unsupported format"}
