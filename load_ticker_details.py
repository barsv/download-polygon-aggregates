# Utility function to load ticker details from CSV file
# Used by viewer backend to get list of available tickers

import settings
import os
import pandas as pd

def load_ticker_details():
    """Load ticker details from the CSV file created by download_ticker_overview.py"""
    tickers_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')
    ticker_details_file = os.path.join(tickers_dir, 'ticker_details.csv')
    if not os.path.exists(ticker_details_file):
        print(f"Error: Ticker details file not found at {ticker_details_file}")
        return None
    try:
        df = pd.read_csv(ticker_details_file)
        return df
    except Exception as e:
        print(f"Error reading ticker details file: {e}")
        return None
