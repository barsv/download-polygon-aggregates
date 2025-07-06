# this script downloads ticker overview for all tickers.

import settings
import os
import pandas as pd
from datetime import datetime, timedelta
import api_key
from polygon import RESTClient
import time

API_KEY = api_key.read_api_key()
client = RESTClient(API_KEY)

tickers_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')
# read history dataframe from the 'tickers_first_last_active.csv' file
history_file = os.path.join(tickers_dir, 'tickers_first_last_active.csv')
history_df = pd.read_csv(history_file)

all_tickers = history_df['ticker'].unique()

# List to store all ticker details
all_ticker_details = []

# Fields to exclude (nested objects)
exclude_fields = {'address', 'branding'}

print(f"Processing {len(all_tickers)} tickers...")

for i, ticker in enumerate(all_tickers):
    try:
        if i % 10 == 0:
            print(f"Processing {i+1}/{len(all_tickers)}: {ticker}")
        # Get ticker details
        details = client.get_ticker_details(ticker)
        # Convert to dictionary and exclude nested objects
        if details:
            ticker_dict = {}
            for key, value in details.__dict__.items():
                if key not in exclude_fields:
                    ticker_dict[key] = value
            all_ticker_details.append(ticker_dict)
    except Exception as e:
        # Skip NOT_FOUND errors silently, show only unexpected errors
        if "NOT_FOUND" not in str(e) and "not found" not in str(e).lower():
            print(f"Error processing ticker {ticker}: {e}")
        continue

# Convert to DataFrame and save
if all_ticker_details:
    df = pd.DataFrame(all_ticker_details)
    
    # Save to CSV
    output_file = os.path.join(tickers_dir, 'ticker_details.csv')
    df.to_csv(output_file, index=False)
    
    print(f"Saved {len(df)} ticker details to {output_file}")
else:
    print("No ticker details were retrieved")