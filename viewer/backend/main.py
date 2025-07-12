import os
import sys
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from datetime import datetime
import io

# Debug: Print startup information
print(f"DEBUG: Starting main.py from {__file__}")
print(f"DEBUG: Current working directory: {os.getcwd()}")
print(f"DEBUG: Python path: {sys.path[:3]}...")  # Show first 3 entries

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

def _get_minutes_df(ticker: str) -> pd.DataFrame:
    """Fetches or generates the DataFrame for 1-minute bars."""
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1minute')
    file_path = os.path.join(bars_dir, f"{ticker}.parquet")
    if not os.path.exists(file_path):
        aggregate_bars(ticker)
        if not os.path.exists(file_path):
            return None
    return pd.read_parquet(file_path)

def _get_seconds_df(ticker: str, from_timestamp: int = None, to_timestamp: int = None) -> pd.DataFrame:
    """Fetches and concatenates DataFrame for 1-second bars."""
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return None

    all_parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])
    files_to_read = []

    if from_timestamp and to_timestamp:
        from_year = datetime.fromtimestamp(from_timestamp).year
        to_year = datetime.fromtimestamp(to_timestamp).year
        for year in range(from_year, to_year + 1):
            file_name = f"{year}.parquet"
            if file_name in all_parquet_files:
                files_to_read.append(os.path.join(bars_dir, file_name))
    elif all_parquet_files:
        files_to_read.append(os.path.join(bars_dir, all_parquet_files[-1]))

    if not files_to_read:
        return None

    return pd.concat([pd.read_parquet(f) for f in files_to_read], ignore_index=True)

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
async def get_bars(ticker: str, from_timestamp: int = None, to_timestamp: int = None, resolution: str = "1second"):
    df = None
    if resolution == "1minute":
        df = _get_minutes_df(ticker)
    elif resolution == "1second":
        df = _get_seconds_df(ticker, from_timestamp, to_timestamp)

    if df is None or df.empty:
        return {"error": f"No data found for {ticker} with resolution {resolution}"}

    df.rename(columns={'timestamp': 'time'}, inplace=True)

    if from_timestamp and to_timestamp:
        df = df[(df['time'] >= from_timestamp) & (df['time'] <= to_timestamp)]
    elif from_timestamp:
        df = df[df['time'] >= from_timestamp]
    elif to_timestamp:
        df = df[df['time'] <= to_timestamp]

    is_initial_load = from_timestamp is None and to_timestamp is None
    if is_initial_load:
        df = df.tail(2000)

    required_columns = ['time', 'open', 'high', 'low', 'close']
    bars_df = df[required_columns].copy()
    
    return {"ticker": ticker, "bars": bars_df.to_dict(orient='records')}

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