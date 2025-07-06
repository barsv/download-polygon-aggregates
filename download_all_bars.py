# This script reads the ticker details data that was saved by download_ticker_overview.py
# sorts tickers by market cap.
# and downloads 1 second bars for each ticker in the list.

import settings
import os
import pandas as pd
from download_bars import download_second_bars

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

def main():
    ticker_details_df = load_ticker_details()
    if ticker_details_df is None:
        print("Failed to load ticker details")
        return
    # Sort by market cap in descending order (largest first)
    # NaN values will automatically be placed at the end
    sorted_by_market_cap = ticker_details_df.sort_values('market_cap', ascending=False, na_position='last')

    tickers = sorted_by_market_cap['ticker'].tolist()
    for ticker in tickers:
        print(ticker)
        download_second_bars(ticker, settings.START_DATE, settings.END_DATE)
    
    return sorted_by_market_cap

if __name__ == "__main__":
    main()