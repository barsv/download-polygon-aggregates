import os
import sys
import pandas as pd
from datetime import datetime
import pyarrow.parquet as pq

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import settings
from filter_outliers import filter_outliers

# aggregate_bars creates the 1-minute bars from 1-second bars
from aggregate_bars import aggregate_bars

# how may bars to return to frontend
BARS_RETURN_LIIMIT = 3000

def resample_rule_to_seconds(rule: str) -> int:
    """Convert pandas resample rule to seconds."""
    import re
    match = re.match(r'^(\d+)(s|min|h|d|w)$', rule.lower())
    if not match:
        raise ValueError(f"Invalid resample rule: {rule}")
    
    number, unit = match.groups()
    number = int(number)
    
    multipliers = {
        's': 1,           # seconds
        'min': 60,        # minutes  
        'h': 3600,        # hours
        'd': 86400,       # days
        'w': 604800       # weeks
    }
    return number * multipliers[unit]

def validate_resample_rule(rule: str) -> bool:
    """Validate if resample rule is allowed."""
    allowed_rules = [
        '1s', '5s', '10s', '15s', '30s',
        '1min', '5min', '15min', '30min', 
        '1h', '4h', '12h',
        '1d', '1w'
    ]
    return rule in allowed_rules

def aggregate_ohlc_data(df: pd.DataFrame, resample_rule: str) -> pd.DataFrame:
    """
    Universal OHLC aggregation function.
    
    Args:
        df: DataFrame with OHLC data and timestamp index OR timestamp column
        resample_rule: Pandas resample rule (e.g., '5s', '1min', '4h', '1d')
    
    Returns:
        Aggregated DataFrame with timestamp index
    """
    if resample_rule == '1s':
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
    # If interval is 1min, skip resampling (already 1-minute data)
    if interval == '1min':
        df_result = df
        df_result = df_result.reset_index()
    else:
        # Use universal aggregation function with original interval
        df_result = aggregate_ohlc_data(df, interval)
    # when we request forward data we pass the timestamp of the last visible bar, 
    # hence we need to drop the first bar because it already exists on the chart.
    if direction == "forward":
        df_result = df_result.iloc[1:]
    return df_result

def get_aggregated_seconds_df(ticker: str, interval: str, timestamp: int = None, direction: str = "both", remove_outliers: bool = False) -> pd.DataFrame:
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
    # filter outliers
    if remove_outliers:
        df = filter_outliers(df)
    # resample
    if interval == '1s':
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

def get_viewport_data(ticker: str, start_timestamp: int, end_timestamp: int, screen_width_pixels: int) -> pd.DataFrame:
    """
    Smart aggregated data for a specific viewport.
    
    Decides the resolution based on seconds per pixel density.
    """
    range_duration = end_timestamp - start_timestamp
    if range_duration <= 0 or screen_width_pixels <= 0:
        return None
        
    seconds_per_pixel = range_duration / screen_width_pixels
    
    # Determine resolution
    # Thresholds:
    # < 10 sec/px -> 1s data
    # < 5 min/px  -> 1min data (aggregated from 1min if needed, or raw 1min)
    # < 2 hours/px -> 1h data
    # >= 2 hours/px -> 1d data
    
    # We call existing functions but with a twist: they usually return BARS_RETURN_LIIMIT bars.
    # Here we want a specific range [start, end].
    # So we might need to adjust or create new logic, or trick existing functions.
    # Existing get_aggregated_minutes_df/seconds_df logic is heavily tied to "timestamp + direction" or "tail".
    # It doesn't support "start -> end" explicitly.
    
    # Let's create a custom loader for specific range to avoid hacking the existing ones too much.
    # But reuse the aggregation logic.
    
    if seconds_per_pixel < 1:
        interval = "1s"
        source = "seconds"
    elif seconds_per_pixel < 60:
         # e.g. 30s per pixel. 1s data is too much (30 bars per pixel).
         # aggregate 1s data to something larger? No, "1min" data is better?
         # If 1s/px < density < 60s/px, we want visible bars. 
         # If we use 1min bars, they will be > 1px wide.
         # Let's stick to:
         interval = "1s" # or aggregated seconds?
         source = "seconds"
    elif seconds_per_pixel < 3600: # < 1h per pixel
         interval = "1min"
         source = "minutes"
    elif seconds_per_pixel < 86400: # < 1d per pixel
         interval = "1h"
         source = "minutes"
    else:
         interval = "1d"
         source = "minutes"
         
    # Optimization: if range is huge, don't try to load seconds.
    
    # Optimization: if range is huge, don't try to load seconds.
    
    # Standard buffer for smooth panning (50%)
    buffer = range_duration * 0.5
    query_start = int(start_timestamp - buffer)
    query_end = int(end_timestamp + buffer)

    df = None
    if source == "minutes":
        bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
        file_path = os.path.join(bars_dir, f"{ticker}.parquet")
        if not os.path.exists(file_path):
             return None
        
        # Read range
        filters = [
            ('timestamp', '>=', query_start),
            ('timestamp', '<=', query_end)
        ]
        table = pq.read_table(file_path, columns=['timestamp', 'open', 'high', 'low', 'close'], filters=filters)
        df = table.to_pandas()
        
    elif source == "seconds":
        start_year = datetime.fromtimestamp(query_start).year
        end_year = datetime.fromtimestamp(query_end).year
        
        bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
        if not os.path.exists(bars_dir):
            return None
            
        dfs = []
        for year in range(start_year, end_year + 1):
            file_path = os.path.join(bars_dir, f"{year}.parquet")
            if os.path.exists(file_path):
                filters = [
                    ('timestamp', '>=', query_start),
                    ('timestamp', '<=', query_end)
                ]
                try:
                    table = pq.read_table(file_path, columns=['timestamp', 'open', 'high', 'low', 'close'], filters=filters)
                    dfs.append(table.to_pandas())
                except Exception:
                    pass
        if dfs:
            df = pd.concat(dfs)
    
    # --- Smart Border Logic ---
    try:
        # Ensure we have at least one point before start and one point after end
        # to allow the chart to draw connecting lines across gaps (weekends, etc.)
        
        left_anchor = None
        right_anchor = None
        
        # Helper to get first/last timestamp
        def get_ts(d, pos):
            if 'timestamp' in d.columns:
                return d['timestamp'].iloc[pos]
            else:
                return d.index[pos]

        # Check Left
        if df is None or df.empty or get_ts(df, 0) > start_timestamp:
            left_anchor = find_anchor_point(ticker, start_timestamp, 'backward')
            
        # Check Right
        if df is None or df.empty or get_ts(df, -1) < end_timestamp:
            right_anchor = find_anchor_point(ticker, end_timestamp, 'forward')
            
        # Combine
        parts = []
        if left_anchor is not None: 
            parts.append(left_anchor)
        if df is not None and not df.empty:
            # Ensure timestamp is a column for concatenation if it's currently index
            if 'timestamp' not in df.columns and df.index.name == 'timestamp':
                 df = df.reset_index()
            parts.append(df)
        if right_anchor is not None:
             # Anchor points usually come as DFs. Ensure they have timestamp col too.
             if 'timestamp' not in right_anchor.columns and right_anchor.index.name == 'timestamp':
                 right_anchor = right_anchor.reset_index()
             parts.append(right_anchor)
             
        # Also clean left anchor
        if left_anchor is not None:
             if 'timestamp' not in left_anchor.columns and left_anchor.index.name == 'timestamp':
                 left_anchor = left_anchor.reset_index()

        if parts:
            df = pd.concat(parts)
            # Normalize for downstream
            if 'timestamp' not in df.columns and df.index.name == 'timestamp':
                df = df.reset_index()
            df = df.drop_duplicates(subset='timestamp').sort_values('timestamp')
        else:
            return None
    except Exception as e:
        import traceback
        with open('error.log', 'w') as f:
            f.write(traceback.format_exc())
        raise e



def get_last_timestamp(ticker: str) -> int:
    """
    Get the last available timestamp for a ticker.
    Checks minutes file first as it is easier.
    """
    # Check minute bars
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
    file_path = os.path.join(bars_dir, f"{ticker}.parquet")
    
    if os.path.exists(file_path):
        # Read just the last row? 
        # PyArrow allows reading metadata or specific query? 
        try:
             # Fast way: read file metadata? No, need content.
             # Read tail.
             # Since it's parquet, we might not assume order unless sorted.
             # But our data is sorted.
             # Let's read the index column from the end?
             # Actually, reading the whole index column is cheap for 20 years of minutes (~5MB).
             # Let's try reading just the last partition/row group?
             # For simplicity now, read 'timestamp' column and take max.
             table = pq.read_table(file_path, columns=['timestamp'])
             # Get max
             # Convert to numpy/pandas
             ts = table['timestamp'].to_numpy()
             if len(ts) > 0:
                 return int(ts[-1]) # Assuming sorted
        except Exception:
             pass
             
    # Fallback to seconds if minutes not found
    seconds_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if os.path.exists(seconds_dir):
        files = sorted([f for f in os.listdir(seconds_dir) if f.endswith('.parquet')])
        if files:
            last_file = files[-1]
            try:
                table = pq.read_table(os.path.join(seconds_dir, last_file), columns=['timestamp'])
                ts = table['timestamp'].to_numpy()
                if len(ts) > 0:
                    return int(ts[-1])
            except Exception:
                pass
                
    return None


