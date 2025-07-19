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

def resample_rule_to_seconds(rule: str) -> int:
    """Convert pandas resample rule to seconds."""
    import re
    match = re.match(r'^(\d+)([SMHDW])$', rule.upper())
    if not match:
        raise ValueError(f"Invalid resample rule: {rule}")
    
    number, unit = match.groups()
    number = int(number)
    
    multipliers = {
        'S': 1,           # seconds
        'M': 60,          # minutes  
        'H': 3600,        # hours
        'D': 86400,       # days
        'W': 604800       # weeks
    }
    
    return number * multipliers[unit]

def validate_resample_rule(rule: str) -> bool:
    """Validate if resample rule is allowed."""
    allowed_rules = [
        '1S', '5S', '10S', '15S', '30S',
        '1M', '5M', '15M', '30M', 
        '1H', '4H', '12H',
        '1D', '1W'
    ]
    return rule in allowed_rules

def aggregate_ohlc_data(df: pd.DataFrame, resample_rule: str, timestamp_col: str = 'timestamp') -> pd.DataFrame:
    """
    Universal OHLC aggregation function.
    
    Args:
        df: DataFrame with OHLC data and timestamp column
        resample_rule: Pandas resample rule (e.g., '5S', '1M', '4H', '1D')
        timestamp_col: Name of timestamp column
    
    Returns:
        Aggregated DataFrame (modifies input DataFrame!)
    """
    if resample_rule == '1S':
        return df  # No aggregation needed for 1 second
    
    # Convert timestamp to datetime for resampling
    df['datetime_idx'] = pd.to_datetime(df[timestamp_col], unit='s')
    df.set_index('datetime_idx', inplace=True)
    
    # Aggregate OHLC data
    result = df.resample(resample_rule).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last'
    }).dropna()
    
    # Convert back to timestamp
    result[timestamp_col] = (result.index.astype(int) // 10**9)
    result.reset_index(drop=True, inplace=True)
    
    return result

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

def _get_aggregated_minutes_df(ticker: str, interval: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load minute bars and aggregate to specified interval on-the-fly."""
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
    
    # Calculate limit based on interval
    interval_minutes = resample_rule_to_seconds(interval) // 60
    minute_limit = LIMIT * interval_minutes
    
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
    # If interval is 1M, skip resampling (already 1-minute data)
    if interval == '1M':
        df_result = df
    else:
        # Use universal aggregation function with original interval
        df_result = aggregate_ohlc_data(df, interval)
    # when we request forward data we pass the timestamp of the last visible bar, 
    # hence we need to drop the first bar because it already exists on the chart.
    if direction == "forward":
        df_result = df_result.iloc[1:]
    # Reset index to get timestamp as column
    df_result.reset_index(inplace=True)
    df_result.rename(columns={df_result.columns[0]: 'time'}, inplace=True)
    return df_result

def _get_aggregated_seconds_df(ticker: str, interval: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load second bars and aggregate to specified interval on-the-fly."""
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
    
    # Calculate limit based on interval
    interval_seconds = resample_rule_to_seconds(interval)
    second_limit = LIMIT * interval_seconds
    
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
    # If interval is 1S, skip resampling (already 1-second data)
    if interval == '1S':
        df_result = df
    else:
        # Use universal aggregation function with original interval
        df_result = aggregate_ohlc_data(df, interval)
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
    else:
        filtered_tickers = sorted_tickers
    return {"tickers": filtered_tickers[:20]}

@app.get("/api/bars/{ticker}")
async def get_bars(ticker: str, timestamp: int = None, direction = "", interval: str = "1S"):
    """
    Get bars for a ticker with specified interval.
    
    Args:
        interval: Resample rule (e.g., '1S', '5S', '1M', '5M', '1H', '4H', '1D', '1W')
    """
    if not validate_resample_rule(interval):
        return {"error": f"Unsupported interval: {interval}"}
    
    # Determine if we need seconds or minutes data
    interval_seconds = resample_rule_to_seconds(interval)
    
    if interval_seconds < 60:
        # Use seconds data
        df = _get_aggregated_seconds_df(ticker, interval, timestamp, direction)
    else:
        # Use minutes data
        df = _get_aggregated_minutes_df(ticker, interval, timestamp, direction)
    
    result = {"ticker": ticker, "bars": df.to_dict(orient='records')}
    return result

@app.get("/api/download/files/{ticker}")
async def get_download_files(ticker: str, interval: str = "1S"):
    if not validate_resample_rule(interval):
        return {"error": f"Unsupported interval: {interval}"}
    
    interval_seconds = resample_rule_to_seconds(interval)
    
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
async def download_file(ticker: str, filename: str, format: str = "parquet", time_format: str = None, interval: str = "1S"):
    try:
        if not validate_resample_rule(interval):
            return {"error": f"Unsupported interval: {interval}"}
        if format not in ["parquet", "csv"]:
            return {"error": f"Unsupported format: {format}"}
        # check that ticker is alphanumeric or dots, dashes, underscores
        if not ticker.replace('.', '').replace('-', '').replace('_', '').isalnum():
            return {"error": "Ticker is not valid"}
        
        interval_seconds = resample_rule_to_seconds(interval)
        
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
            if interval != "1S":
                df = aggregate_ohlc_data(df, interval)
        else:
            df.reset_index(inplace=True)
            df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
            if interval != "1M":
                df = aggregate_ohlc_data(df, interval)
        
        # return the file
        if interval_seconds < 60:
            result_filename = f"{ticker}_{interval}_{year}.{format}"
        else:
            result_filename = f"{ticker}_{interval}.{format}"
            
        if format == "parquet":
            output = io.BytesIO()
            table = pa.table(df)
            pq.write_table(table, output)
            output.seek(0)
            return StreamingResponse(output, media_type="application/octet-stream", headers={'Content-Disposition': f'attachment; filename="{result_filename}"'})
        elif format == "csv":
            if time_format and time_format != 'timestamp':
                # Convert Python datetime format to pandas format
                pandas_format = time_format.replace('yyyy', '%Y').replace('MM', '%m').replace('dd', '%d').replace('HH', '%H').replace('mm', '%M').replace('ss', '%S').replace('fff', '%f')
                # Convert timestamp to datetime and format
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.strftime(pandas_format)
            output = io.StringIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return StreamingResponse(io.BytesIO(output.getvalue().encode('utf-8')), media_type="text/csv", headers={'Content-Disposition': f'attachment; filename="{result_filename}"'})
        else:
            return {"error": "Unsupported format"}
    except Exception as e:
        return {"error": f"Download failed: {str(e)}"}