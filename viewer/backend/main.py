
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
async def get_tickers():
    global ticker_details_df
    if ticker_details_df is None:
        ticker_details_df = load_ticker_details()

    if ticker_details_df is None:
        return {"error": "Ticker details not found"}
    
    # Sort by market cap in descending order
    sorted_by_market_cap = ticker_details_df.sort_values('market_cap', ascending=False, na_position='last')
    tickers = sorted_by_market_cap['ticker'].tolist()
    return {"tickers": tickers}

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
            if not all(col in df.columns for col in required_columns):
                continue
            
            bars_df = df[required_columns].copy()
            all_bars.extend(bars_df.to_dict(orient='records'))

        except Exception as e:
            print(f"Error reading or processing {file_name}: {e}")

    all_bars.sort(key=lambda x: x['time'])

    # For initial load, return the most recent 2000 bars.
    if from_timestamp is None and to_timestamp is None:
        all_bars = all_bars[-2000:]

    return {"ticker": ticker, "bars": all_bars}
