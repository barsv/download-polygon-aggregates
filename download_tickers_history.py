# this script downloads active and inactive tickers for all dates.
# this is necessary to find the list of all tickers that have ever existed.
# the code and the approach is not optimal, but ok for now.

from polygon import RESTClient
import csv
from datetime import datetime, timedelta
import logging
import settings
import utils
import api_key
import os

START_DATE = settings.START_DATE
END_DATE = settings.END_DATE

utils.setup_logger()
logger = logging.getLogger()

API_KEY = api_key.read_api_key()

def download_ticker_history(start_date: str, end_date: str, active: bool, output_file: str):
    """
    Downloads daily snapshots of tickers from Polygon's reference API
    and writes them to a CSV file.
    
    Parameters:
    - start_date (str): "YYYY-MM-DD"
    - end_date (str): "YYYY-MM-DD"
    - output_file (str): Path to output CSV file.
    """
    client = RESTClient(API_KEY)
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Header row
        writer.writerow([
            "date", "ticker", "composite_figi", "active", "cik", "currency_name", "delisted_utc",
            "last_updated_utc", "locale", "market", "name", "primary_exchange", "type"
        ])
        current = start
        while current <= end:
            # Skip weekends (no trading)
            if current.weekday() < 5:
                date_str = current.strftime("%Y-%m-%d")
                logger.info(f"Fetching tickers for {date_str}...")
                try:
                    # Fetch all pages of tickers for the given date
                    tickers = client.list_tickers(
                        date=date_str,
                        market="stocks",
                        active=active,
                        limit=1000
                    )
                    # Write each ticker to CSV
                    for t in tickers:
                        writer.writerow([
                            date_str,
                            t.ticker,
                            t.composite_figi,
                            t.active,
                            t.cik,
                            t.currency_name,
                            t.delisted_utc,
                            t.last_updated_utc,
                            t.locale,
                            t.market,
                            t.name,
                            t.primary_exchange,
                            t.type,
                        ])
                except Exception as e:
                    logger.error(f"Error fetching {date_str}: {e}")
            current += timedelta(days=1)

if __name__ == "__main__":
    data_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers')
    logger.info("Downloading active tickers...")
    download_ticker_history(START_DATE, END_DATE, True, os.path.join(data_dir, "tickers_history_active.csv"))
    logger.info("Downloading inactive tickers...")
    download_ticker_history(START_DATE, END_DATE, False, os.path.join(data_dir, "tickers_history_inactive.csv"))
    logger.info("All done.")

