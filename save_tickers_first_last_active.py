# this script converts 'tickers_history_active.csv' into 'tickers_first_last_active.csv'.
'''
algorithm:
1. loop through active_tickers_file
2. collect all rows for the first day.
   need to check here that there are no duplicate tickers within one day.
   create a dictionary that maps a ticker to its row.
3. repeat (2) for the next day.
   now loop over all tickers in the current day and compare them to tickers in the previous day.
   if there is a change in (composite_figi, active, cik, delisted_utc, name, primary_exchange, type)
   then log it into history as history['figi']['ticker']['date']=row.
   if there are new tickers then they will be added as well.
   when processing a row in the active_today remove it from active_yesterday.
   in the end active_yesterday will have tickers that are missing today. add them to the history.
   history['figi']['ticker']['date']=null
'''
import csv
from datetime import datetime, timedelta
import settings
import os
import pandas as pd

history = {}
counter = 0
active_today = {}
active_yesterday = {}
tickers_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')
active_tickers_file = os.path.join(tickers_dir, 'tickers_history_active.csv')

with open(active_tickers_file, newline='', encoding='utf-8') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        counter += 1
        if counter % (1000 * 1000) == 0:
            print(f"Processed {counter} rows")
        figi  = row["composite_figi"]
        if not figi:
            # Skip rows without FIGI
            continue
        ticker= row["ticker"]
        date  = datetime.fromisoformat(row["date"]).date()
        if figi not in history:
            # first time encountering this FIGI
            history[figi] = { ticker: { 'first_active' : date } }
        else:
            f = history[figi]
            if ticker not in f:
                # first time encountering this ticker for this FIGI
                f[ticker] = { 'first_active' : date }
            else:
                # known ticker for this FIGI
                f[ticker]['last_active'] = date

# convert history to a DataFrame and save it to a CSV file
history_list = []
for figi, tickers in history.items():
    for ticker, ranges in tickers.items():
        row = {
            'figi': figi,
            'ticker': ticker,
            'first_active': ranges.get('first_active', None),
            'last_active': ranges.get('last_active', None)
        }
        history_list.append(row)

history_df = pd.DataFrame(history_list)
history_df.to_csv(os.path.join(tickers_dir, 'tickers_first_last_active.csv'), index=False)