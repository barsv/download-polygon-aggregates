
import os
import sys
import pandas as pd
from fastapi import FastAPI

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import settings

app = FastAPI()

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
    ticker_details_df = load_ticker_details()
    if ticker_details_df is None:
        return {"error": "Ticker details not found"}
    
    # Sort by market cap in descending order
    sorted_by_market_cap = ticker_details_df.sort_values('market_cap', ascending=False, na_position='last')
    tickers = sorted_by_market_cap['ticker'].tolist()
    return {"tickers": tickers}

@app.get("/api/bars/{ticker}")
async def get_bars(ticker: str):
    bars_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars', '1second', ticker)
    if not os.path.exists(bars_dir):
        return {"error": "Bars data not found for this ticker"}

    # Find the first .parquet file in the directory
    parquet_files = [f for f in os.listdir(bars_dir) if f.endswith('.parquet')]
    if not parquet_files:
        return {"error": "No .parquet files found for this ticker"}

    # For simplicity, load the first found .parquet file
    file_path = os.path.join(bars_dir, parquet_files[0])

    try:
        df = pd.read_parquet(file_path)
        # Ensure required columns exist
        required_columns = ['timestamp', 'open', 'high', 'low', 'close']
        if not all(col in df.columns for col in required_columns):
            return {"error": "Parquet file is missing required columns (timestamp, open, high, low, close)"}
        
        # The timestamp is already in seconds, just rename it to 'time'
        df.rename(columns={'timestamp': 'time'}, inplace=True)
        
        # Select and rename columns for the charting library
        bars_df = df[['time', 'open', 'high', 'low', 'close']].copy()
        
        # Convert to list of dictionaries
        bars = bars_df[:1000].to_dict(orient='records')
        return {"ticker": ticker, "bars": bars}
    except Exception as e:
        return {"error": f"Error reading bars file: {e}"}
