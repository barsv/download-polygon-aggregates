# this script downloads raw daily aggregates for all tickers without considering renames.
# for example, for 'META' will will download a single file that contains first history for the META ETF and then
# the history for the META stock.
import settings
import os
import pandas as pd
from datetime import datetime, timedelta
import api_key
from polygon import RESTClient

API_KEY = api_key.read_api_key()
client = RESTClient(API_KEY)

tickers_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')

# read history dataframe from the 'tickers_first_last_active.csv' file
history_file = os.path.join(tickers_dir, 'tickers_first_last_active.csv')
history_df = pd.read_csv(history_file, parse_dates=['first_active', 'last_active'])

all_tickers = history_df['ticker'].unique()

today_string = datetime.now().strftime('%Y-%m-%d')
raw_daily_dir = os.path.join(tickers_dir, '..',  'raw_daily')
os.makedirs(raw_daily_dir, exist_ok=True)
saved_tickers_count = 0
# dump all daily aggregates for all tickers in the history.
for ticker in all_tickers:
    try:
        file_path = os.path.join(raw_daily_dir, f'{ticker}.csv')
        if os.path.exists(file_path):
            saved_tickers_count += 1
            continue
        aggs = client.get_aggs(ticker, 1, 'day', '2003-09-10', today_string)
        # save to a file:
        aggs_df = pd.DataFrame(aggs)
        file_path = os.path.join(raw_daily_dir, f'{ticker}.csv')
        aggs_df.to_csv(file_path, index=False)
        saved_tickers_count += 1
        if (saved_tickers_count % 10 == 0):
            print(f"Saved daily aggs for {saved_tickers_count} tickers out of {len(all_tickers)}")
    except Exception as e:
        print(f"Error fetching aggregates for {ticker}: {e}")