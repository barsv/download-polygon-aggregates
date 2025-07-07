# this script is to download custom bars from Polygon.io.
# the main function is download_bars
# it's possible to use this script to just download bars for a list of tickers. see the main function.
# but the main purpose is to use download_bars function from other scripts.

import os
import pandas as pd
from polygon import RESTClient
from datetime import datetime, timedelta
import logging
import sys
from dateutil import tz
import time
from api_key import read_api_key
from utils import setup_logger
import settings

setup_logger()
logger = logging.getLogger()

# Polygon API client
API_KEY = read_api_key()
if not API_KEY:
    logger.error("No API key provided. Exiting.")
    sys.exit(1)
client = RESTClient(API_KEY)

# Configuration
OUTPUT_DIR = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars')  # Directory to save CSV files
CHUNK_DAYS = 365  # Process one year at a time to manage memory
RETRY_LIMIT = 3  # Number of retries for API failures
RETRY_DELAY = 5  # Seconds to wait between retries

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_to_et(timestamp_ms):
    """Convert Unix timestamp (ms) in UTC to Eastern Time (ET) datetime string."""
    utc_time = datetime.fromtimestamp(timestamp_ms / 1000, tz=tz.tzutc())
    et_time = utc_time.astimezone(tz.gettz('America/New_York'))
    return et_time.strftime('%Y-%m-%d %H:%M:%S')

def fetch_bars(ticker, start_date, end_date, multiplier=1, timespan='minute'):
    """Fetch second-by-second aggregates for a ticker within a date range."""
    data = []
    attempt = 0
    while attempt < RETRY_LIMIT:
        try:
            logger.info(f"Fetching data for {ticker} from {start_date} to {end_date}")
            counter = 0
            for agg in client.list_aggs(
                ticker=ticker,
                multiplier=multiplier,
                timespan=timespan,
                from_=start_date,
                to=end_date,
                adjusted=True,
                sort='asc',
                limit=50000
            ):
                data.append({
                    'timestamp': convert_to_et(agg.timestamp),
                    'open': agg.open,
                    'high': agg.high,
                    'low': agg.low,
                    'close': agg.close,
                    'volume': agg.volume,
                    'vwap': agg.vwap,
                    'transactions': agg.transactions,
                    'otc': agg.otc
                })
                counter += 1
                if counter % (50 * 1000) == 0:
                    logger.info(f"Retrieved {counter} records for {ticker}")
            logger.info(f"Retrieved {len(data)} records for {ticker}")
            return data
        except Exception as e:
            attempt += 1
            logger.warning(f"Attempt {attempt}/{RETRY_LIMIT} failed for {ticker}: {e}")
            if attempt < RETRY_LIMIT:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"Failed to fetch data for {ticker} after {RETRY_LIMIT} attempts")
                return []

def save_to_csv(ticker, data, output_path):
    """Save data to a CSV file, appending if the file exists."""
    if not data:
        logger.warning(f"No data to save for {ticker}")
        return
    df = pd.DataFrame(data)
    logger.info(f"Saving to {output_path}")
    try:
        if os.path.exists(output_path):
            # Append to existing file, avoid duplicating headers
            df.to_csv(output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(output_path, mode='w', header=True, index=False)
        logger.info(f"Saved {len(df)} records to {output_path}")
    except Exception as e:
        logger.error(f"Error saving CSV for {ticker}: {e}")

def save_to_parquet(df, filepath):
    # Optimize data types
    df_opt = df.copy()
    df_opt['timestamp'] = pd.to_datetime(df_opt['timestamp']).astype('int64') // 10**9
    df_opt['open'] = df_opt['open'].astype('float32')
    df_opt['high'] = df_opt['high'].astype('float32')
    df_opt['low'] = df_opt['low'].astype('float32')
    df_opt['close'] = df_opt['close'].astype('float32')
    df_opt['volume'] = df_opt['volume'].astype('uint32')
    df_opt['vwap'] = df_opt['vwap'].astype('float32')
    df_opt['transactions'] = df_opt['transactions'].astype('uint32')
    # Save with Zstd compression
    df_opt.to_parquet(filepath, engine='pyarrow', compression='zstd')

def get_last_day_of_year(date):
    """Get the last day of the year for a given date."""
    return date.replace(month=12, day=31)

def download_second_bars(ticker, start_date, end_date, multiplier=1, timespan='second'):
    """Process a single ticker, fetching data in chunks."""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    current_start = start
    output_dir = os.path.join(OUTPUT_DIR, f'{multiplier}{timespan}', ticker)
    os.makedirs(output_dir, exist_ok=True)
    # Remove existing file to avoid appending to old data
    output_path = os.path.join(output_dir, f"{ticker}.csv")
    if os.path.exists(output_path):
        os.remove(output_path)
    while current_start < end:
        last_day_of_year = get_last_day_of_year(current_start)
        current_end = min(last_day_of_year, end)
        file_name = f"{current_start.year}.parquet"
        if os.path.exists(os.path.join(output_dir, file_name)):
            logger.info(f"File {file_name} already exists, skipping download for {ticker} from {current_start} to {current_end}")
        else:
            logger.info(f"Processing: {file_name}")
            data = fetch_bars(ticker, current_start.strftime('%Y-%m-%d'), current_end.strftime('%Y-%m-%d'), multiplier, timespan)
            save_to_parquet(pd.DataFrame(data), os.path.join(output_dir, file_name))
        current_start = current_end + timedelta(days=1)

def download_bars(ticker, start_date, end_date, multiplier=1, timespan='minute'):
    """Process a single ticker, fetching data in chunks."""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    current_start = start
    output_dir = os.path.join(OUTPUT_DIR, f'{multiplier}{timespan}')
    output_path = os.path.join(output_dir, f"{ticker}.csv")
    os.makedirs(output_dir, exist_ok=True)
    # Remove existing file to avoid appending to old data
    if os.path.exists(output_path):
        os.remove(output_path)
    while current_start < end:
        current_end = min(current_start + timedelta(days=CHUNK_DAYS), end)
        data = fetch_bars(ticker, current_start.strftime('%Y-%m-%d'), current_end.strftime('%Y-%m-%d'), multiplier, timespan)
        save_to_csv(ticker, data, output_path)
        current_start = current_end + timedelta(days=1)

def main():
    # timespan = 'minute' # second, minute, hour, day, week, month, quarter, year
    # multiplier = 1 # for exmple, if timespan is 'minute', multiplier is 1 for 1 minute, 5 for 5 minutes, etc.
    # start_date = settings.START_DATE
    # end_date = settings.END_DATE
    # for ticker in ['SPY']:
    #     logger.info(f"Processing ticker: {ticker}")
    #     download_bars(ticker, start_date, end_date, multiplier, timespan)
    for ticker in ['SPY']:
        logger.info(f"Processing ticker: {ticker}")
        download_second_bars(ticker, '2024-01-01', settings.END_DATE)

if __name__ == '__main__':
    main()
