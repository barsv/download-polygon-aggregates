
import os
import sys
import pandas as pd
from fastapi import FastAPI
from datetime import datetime

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import settings

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

@app.get("/api/tickers")
async def get_tickers(search: str = None):
    global ticker_details_df, sorted_tickers
    if ticker_details_df is None:
        ticker_details_df = load_ticker_details()
        if ticker_details_df is not None:
            # Sort by market cap in descending order and cache the result
            sorted_by_market_cap = ticker_details_df.sort_values('market_cap', ascending=False, na_position='last')
            sorted_tickers = sorted_by_market_cap['ticker'].tolist()

    if sorted_tickers is None:
        return {"error": "Ticker details not found or failed to process"}

    if search:
        # Filter tickers based on the search query (case-insensitive starts-with)
        search_lower = search.lower()
        filtered_tickers = [t for t in sorted_tickers if t.lower().startswith(search_lower)]
        return {"tickers": filtered_tickers[:50]} # Return max 50 matches
    else:
        # Return top 100 tickers if no search query
        return {"tickers": sorted_tickers[:100]}

@app.get("/api/bars/{ticker}")
async def get_bars(ticker: str, from_timestamp: int = None, to_timestamp: int = None):
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return {"error": "Bars data not found for this ticker"}

    all_bars = []
    
    all_parquet_files = sorted([f for f in os.listdir(bars_dir) if f.endswith('.parquet')])

    files_to_read = []
    if from_timestamp and to_timestamp:
        from_year = datetime.fromtimestamp(from_timestamp).year
        to_year = datetime.fromtimestamp(to_timestamp).year
        for year in range(from_year, to_year + 1):
            file_name = f"{year}.parquet"
            if file_name in all_parquet_files:
                files_to_read.append(file_name)
    else:
        # If no date range is specified, load the most recent year's data
        if all_parquet_files:
            files_to_read.append(all_parquet_files[-1])

    for file_name in files_to_read:
        file_path = os.path.join(bars_dir, file_name)
        try:
            df = pd.read_parquet(file_path)
            
            df.rename(columns={'timestamp': 'time'}, inplace=True)

            if from_timestamp and to_timestamp:
                df = df[(df['time'] >= from_timestamp) & (df['time'] <= to_timestamp)]
            elif from_timestamp:
                df = df[df['time'] >= from_timestamp]
            elif to_timestamp:
                df = df[df['time'] <= to_timestamp]

            required_columns = ['time', 'open', 'high', 'low', 'close']

            # For initial load (no from/to timestamp), take only the last 2000 bars from the latest file.
            # This check needs to be here, after filtering, but before extending all_bars.
            if from_timestamp is None and to_timestamp is None and file_name == all_parquet_files[-1]:
                df = df.tail(2000) # Take only the last 2000 rows from this DataFrame

            bars_df = df[required_columns].copy() # Ensure only required columns are returned and avoid SettingWithCopyWarning.
            all_bars.extend(bars_df.to_dict(orient='records'))

        except Exception as e:
            # Catch any errors during file reading or processing (e.g., missing columns, corrupted data).
            # This ensures that a single bad file does not crash the entire API request.
            print(f"Error reading or processing {file_name}: {e}")

    return {"ticker": ticker, "bars": all_bars}
