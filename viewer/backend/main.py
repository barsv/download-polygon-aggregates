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

def _get_minutes_df(ticker: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Load minute bars with pre-filtering using PyArrow."""
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
    
    # Pre-filter based on timestamps and direction
    if timestamp is not None:
        try:
            pos = df.index.get_loc(timestamp)
        except KeyError:
            # Fallback: find position using searchsorted (consistent with _get_seconds_df)
            pos = df.index.searchsorted(timestamp)
            pos = min(pos, len(df) - 1)  # Ensure pos is within bounds
        
        if direction == "backward":
            start_pos = max(0, pos - LIMIT + 1)
            df = df.iloc[start_pos:pos]
        elif direction == "forward":
            end_pos = min(len(df), pos + LIMIT)
            df = df.iloc[pos:end_pos]
        elif direction == "both":
            start_pos = max(0, pos - LIMIT // 2)
            end_pos = min(len(df), pos + LIMIT // 2)
            df = df.iloc[start_pos:end_pos]
    else:
        df = df.tail(LIMIT)
    
    # Reset index to get timestamp as column
    df.reset_index(inplace=True)
    df.rename(columns={df.columns[0]: 'time'}, inplace=True)
        
    return df

def _get_seconds_df(ticker: str, timestamp: int = None, direction: str = "both") -> pd.DataFrame:
    """Fetches and concatenates DataFrame for 1-second bars with filtering."""
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
    
    # Apply filtering based on timestamp and direction
    if timestamp is not None:
        if direction == "backward":
            idx = df['timestamp'].searchsorted(timestamp, side='right')
            start_idx = max(0, idx - LIMIT)
            df = df.iloc[start_idx:idx - 1]
        elif direction == "forward":
            idx = df['timestamp'].searchsorted(timestamp, side='left')
            df = df.iloc[idx:idx + LIMIT]
        elif direction == "both":
            idx = df['timestamp'].searchsorted(timestamp, side='left')
            start_idx = max(0, idx - LIMIT // 2)
            end_idx = min(len(df), idx + LIMIT // 2)
            df = df.iloc[start_idx:end_idx]
    else:
        df = df.tail(LIMIT)
    
    # Rename timestamp column to time
    df.rename(columns={'timestamp': 'time'}, inplace=True)
    
    return df

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
async def get_bars(ticker: str, timestamp: int = None, direction = "", resolution: str = "1second"):
    if resolution == "1minute":
        df = _get_minutes_df(ticker, timestamp, direction)
    elif resolution == "1second":
        df = _get_seconds_df(ticker, timestamp, direction)
    else:
        return {"error": f"Unsupported resolution: {resolution}"}
        
    if df is None or df.empty:
        return {"error": f"No data found for {ticker} with resolution {resolution}"}

    # Both functions now return only the required columns
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
async def download_file(ticker: str, filename: str, format: str = "parquet"):
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    file_path = os.path.join(bars_dir, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    if format == "parquet":
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    elif format == "csv":
        try:
            df = pd.read_parquet(file_path)
            output = io.StringIO()
            df.to_csv(output, index=False)
            output.seek(0)
            csv_filename = filename.replace(".parquet", ".csv")
            return StreamingResponse(io.BytesIO(output.getvalue().encode('utf-8')), media_type="text/csv", headers={'Content-Disposition': f'attachment; filename="{csv_filename}"'})
        except Exception as e:
            return {"error": f"Error converting to CSV: {e}"}
    else:
        return {"error": "Unsupported format"}