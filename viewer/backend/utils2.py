import os
import sys
import pandas as pd
from datetime import datetime
import pyarrow.parquet as pq

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import settings

# aggregate_bars creates the 1-minute bars from 1-second bars
from aggregate_bars import aggregate_bars

# how may bars to return to frontend
BARS_RETURN_LIIMIT = 3000

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

def aggregate_ohlc_data(df: pd.DataFrame, resample_rule: str) -> pd.DataFrame:
    """
    Universal OHLC aggregation function.
    
    Args:
        df: DataFrame with OHLC data and timestamp index OR timestamp column
        resample_rule: Pandas resample rule (e.g., '5S', '1M', '4H', '1D')
    
    Returns:
        Aggregated DataFrame with timestamp index
    """
    if resample_rule == '1S':
        return df  # No aggregation needed for 1 second
    
    # --- create index on timestamp ---
    if 'timestamp' in df.columns:
        # Convert 'timestamp' to datetime and set as index
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit="s")
        df.set_index('timestamp', inplace=True)
    else:
        # Convert existing int index to datetime index
        df.index = pd.to_datetime(df.index, unit="s")
        df.index.name = 'timestamp'
    
    # --- Aggregate OHLC data ---
    result = df.resample(resample_rule).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last'
    }).dropna()
    
    # --- Restore UNIX‐seconds column ---
    result = result.reset_index()
    result['timestamp'] = (result['timestamp'].astype("int64") // 10**9).astype(int)

    # --- Move timestamp column to first position ---
    cols = result.columns.tolist()
    # pop the 'timestamp' and insert at position 0
    cols.insert(0, cols.pop(cols.index('timestamp')))
    result = result[cols]
    
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

def get_aggregated_minutes_df(ticker: str, interval: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
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
    minute_limit = BARS_RETURN_LIIMIT * interval_minutes
    
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
    return df_result

def get_aggregated_seconds_df(ticker: str, interval: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load second bars and aggregate to specified interval on-the-fly."""
    # simplified logic - load from one file. if it will be on the year boundary we will return whatever there is up to 
    # the edge. and the next ajax will load from the next file.
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return None
    all_parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])
    if timestamp:
        # find the file for that year
        target_year = datetime.fromtimestamp(timestamp).year
        file_name = f"{target_year}.parquet"
    else:
        # last file
        file_name = all_parquet_files[-1]
    required_columns = ['timestamp', 'open', 'high', 'low', 'close']
    df = pd.read_parquet(os.path.join(bars_dir, file_name), columns=required_columns)
    
    # Calculate limit based on interval
    interval_seconds = resample_rule_to_seconds(interval)
    second_limit = BARS_RETURN_LIIMIT * interval_seconds
    if timestamp is None:
        df = df.tail(second_limit)
    else:
        # slice what we need for frontend
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
    # resample
    if interval == '1S':
        # skip resampling (already 1-second data)
        df_result = df
    else:
        # Use universal aggregation function with original interval
        df_result = aggregate_ohlc_data(df, interval)
    # when we request forward data we pass from frontend the timestamp of the last visible bar, 
    # hence we need to drop the first bar because it already exists on the chart.
    if direction == "forward":
        df_result = df_result.iloc[1:]
    return df_result
