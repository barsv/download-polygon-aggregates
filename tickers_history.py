from polygon import RESTClient
import csv
from datetime import datetime, timedelta
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.FileHandler('polygon_download.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

# Read API key from secret.txt
def read_api_key(file_path='secret.txt'):
    """Read API key from secret.txt."""
    try:
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
        print("Successfully read API key from secret.txt")
        return api_key
    except Exception as e:
        print(f"Error reading API key from {file_path}: {e}")
        return None

# Polygon API client
API_KEY = read_api_key()

def download_ticker_history(start_date: str, end_date: str, output_file: str):
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
                        active=False,
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
    # polygon has data from 2003-??-??
    download_ticker_history("2003-01-01", datetime.now().strftime("%Y-%m-%d"), "tickers_history_inactive.csv")

