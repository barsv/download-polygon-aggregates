import os
import sys
import pandas as pd
import argparse

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import settings

def aggregate_bars(ticker):
    """
    Aggregates 1-second bars into 1-minute bars for a given ticker.
    Processes files year by year to optimize memory usage.
    """
    base_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'bars')
    input_dir = os.path.join(base_dir, '1second', ticker)
    output_dir = os.path.join(base_dir, '1minute')
    output_file = os.path.join(output_dir, f"{ticker}.parquet")

    if not os.path.exists(input_dir):
        print(f"Input directory not found: {input_dir}")
        return

    os.makedirs(output_dir, exist_ok=True)

    all_files_in_input_dir = os.listdir(input_dir)
    parquet_files = sorted([f for f in all_files_in_input_dir if f.endswith('.parquet')])
    
    if not parquet_files:
        print(f"No .parquet files found for ticker {ticker}")
        return

    aggregated_dfs = []
    for file_name in parquet_files:
        # Check for corresponding .txt file indicating no data
        if f"{file_name}.txt" in all_files_in_input_dir:
            try:
                with open(os.path.join(input_dir, f"{file_name}.txt"), 'r') as f:
                    if 'NoData' in f.read():
                        print(f"Skipping {file_name} due to NoData file.")
                        continue
            except IOError:
                pass # If the file can't be read, proceed to read the parquet file

        file_path = os.path.join(input_dir, file_name)
        try:
            df = pd.read_parquet(file_path)
            
            # The timestamp is in seconds, convert to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            df.set_index('timestamp', inplace=True)

            # Resample to 1-minute bars
            agg_df_year = df.resample('1Min').agg({
                'open': 'first',
                'high': 'max',
                'low': 'min',
                'close': 'last',
                'volume': 'sum',
                'vwap': 'mean', # or some other appropriate aggregation for vwap
                'transactions': 'sum'
            }).dropna()
            
            aggregated_dfs.append(agg_df_year)
            print(f"Processed {file_name}")

        except Exception as e:
            print(f"Error reading or processing {file_name}: {e}")

    if not aggregated_dfs:
        print("No data to process after aggregation.")
        return

    final_agg_df = pd.concat(aggregated_dfs, ignore_index=False) # Keep index for proper sorting
    final_agg_df.sort_index(inplace=True) # Ensure chronological order

    # Convert timestamp back to seconds
    final_agg_df.reset_index(inplace=True)
    final_agg_df['timestamp'] = (final_agg_df['timestamp'].astype(int) // 10**9)

    final_agg_df.to_parquet(output_file, index=False)
    print(f"Successfully created {output_file}")
    
    # print file size
    file_size = os.path.getsize(output_file)
    print(f"File size: {file_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aggregate 1-second bars to 1-minute bars.")
    parser.add_argument("ticker", help="The ticker symbol to process (e.g., AAPL).")
    args = parser.parse_args()
    
    aggregate_bars(args.ticker)