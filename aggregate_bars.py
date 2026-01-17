import os
import sys
import pandas as pd
import argparse

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import settings
from filter_outliers import filter_outliers

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

            # # Filter outliers before aggregation
            # df = filter_outliers(df)
            
            # === Logging only for 2009 ===
            debug_2009 = (file_name == '2009.parquet')
            
            if debug_2009:
                
                # Check the problematic bars
                problem_timestamps = [
                    pd.Timestamp('2009-01-14 18:08:23'),
                    pd.Timestamp('2009-01-14 18:08:28'),
                ]

                for ts in problem_timestamps:
                    if ts in df.index:
                        iloc_pos = df.index.get_loc(ts)
                        # Show 3 bars before and 3 after
                        window_start = max(0, iloc_pos - 3)
                        window_end = min(len(df), iloc_pos + 4)
                        print(f"\nContext around {ts}:")
                        print(df.iloc[window_start:window_end][['open', 'high', 'low', 'close']])
                
                # Filter outliers before aggregation
                print(f"\n--- Filtering outliers for {file_name} ---")
                print(f"Before filter: {len(df)} bars")
                print(f"Sample before (first 3): \n{df[['open', 'high', 'low', 'close']].head(3)}")

                # Calculate std (same logic as in filter_outliers)
                returns = df['close'].pct_change()
                std = returns.std()
                print(f"Calculated std: {std}, is_na: {pd.isna(std)}, is_zero: {std == 0}")

                # Find extreme values before filtering
                if std > 0:
                    prev_close = df['close'].shift(1)
                    next_open = df['open'].shift(-1)
                    
                    # Check high outliers (most likely spike)
                    jump_out_high = (df['high'] - prev_close) / prev_close
                    jump_back_high = (next_open - df['high']) / df['high']
                    
                    big_jumps_out = jump_out_high.abs() > 3.0 * std
                    big_jumps_back = jump_back_high.abs() > 3.0 * std
                    opposite_signs = jump_out_high * jump_back_high < 0
                    
                    print(f"Big jumps OUT: {big_jumps_out.sum()}")
                    print(f"Big jumps BACK: {big_jumps_back.sum()}")
                    print(f"Both big AND opposite: {(big_jumps_out & big_jumps_back & opposite_signs).sum()}")
                    
                    # Show the bars with extreme jumps
                    extreme_idx = jump_out_high.abs().nlargest(3).index
                    print(f"\nTop 3 extreme bars:")
                    for idx in extreme_idx:
                        iloc_pos = df.index.get_loc(idx)
                        if iloc_pos > 0 and iloc_pos < len(df) - 1:
                            window = df.iloc[iloc_pos-1:iloc_pos+2][['open', 'high', 'low', 'close']]
                            print(f"\n{idx}:")
                            print(window)
                            print(f"jump_out: {jump_out_high.iloc[iloc_pos]:.2f}, jump_back: {jump_back_high.iloc[iloc_pos]:.2f}")

                df_before = df.copy()
                
            # Check close specifically for the bad bar
            bad_ts = pd.Timestamp('2009-01-14 18:08:23')
            if bad_ts in df.index:
                iloc_pos = df.index.get_loc(bad_ts)
                prev_c = df['close'].iloc[iloc_pos - 1] if iloc_pos > 0 else None
                next_o = df['open'].iloc[iloc_pos + 1] if iloc_pos < len(df) - 1 else None
                curr_c = df['close'].iloc[iloc_pos]
                
                print(f"\nBefore filter_outliers, bar {bad_ts}:")
                print(f"  prev_close={prev_c}, current_close={curr_c}, next_open={next_o}")
                if prev_c and next_o:
                    j_out = (curr_c - prev_c) / prev_c
                    j_back = (next_o - curr_c) / curr_c
                    print(f"  jump_out={j_out:.4f}, jump_back={j_back:.4f}")
                    print(f"  opposite_signs: {j_out * j_back < 0}")

            df = filter_outliers(df)

            # Check if it was fixed
            if bad_ts in df.index:
                iloc_pos = df.index.get_loc(bad_ts)
                print(f"\nAfter filter_outliers, bar {bad_ts}:")
                print(f"  {df.iloc[iloc_pos][['open', 'high', 'low', 'close']].to_dict()}")
                            
            # df = filter_outliers(df)
            if debug_2009:
                print(f"After filter: {len(df)} bars")

                # Check if anything changed
                changes = (df_before != df).any(axis=1).sum()
                print(f"Number of bars modified: {changes}")
                if changes > 0:
                    print(f"Sample after (first 3): \n{df[['open', 'high', 'low', 'close']].head(3)}")
                print("--- End filtering ---\n")
            
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

    # Convert timestamp back to seconds but keep it as index
    final_agg_df.index = (final_agg_df.index.astype(int) // 10**9)

    # Save with timestamp as index for faster lookups
    final_agg_df.to_parquet(output_file, index=True)
    print(f"Successfully created {output_file}")
    
    # print file size
    file_size = os.path.getsize(output_file)
    print(f"File size: {file_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aggregate 1-second bars to 1-minute bars.")
    parser.add_argument("ticker", help="The ticker symbol to process (e.g., AAPL).")
    args = parser.parse_args()
    
    aggregate_bars(args.ticker)