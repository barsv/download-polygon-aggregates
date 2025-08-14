import numpy as np
import sys, os
import pandas as pd
import random
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count

from data_downloader import download, get_filename
from pattern_analysis import get_alpha_lambda, get_rmse, create_window
from pattern_searcher import PatternSearcher
from trailing_stop_loss import generate_stop_loss_levels
from trailing_stop_loss import calculate_pl
from checkpoints import load_ckpt, save_ckpt

ticker = 'AAPL'
interval = '5s'
year = '2024'
# Set the random seed for reproducibility
random.seed(42)
# Force fixed-point notation instead of scientific notation
np.set_printoptions(suppress=True, precision=6)

print('loading prices')
# download data to the file on disk.
filename = get_filename(ticker, interval, year)
if not os.path.exists(filename):
	download(ticker, interval, year)
# read data from the file on disk.
filename = get_filename(ticker, interval, year)
df = pd.read_parquet(filename)

m = 60 # window size

print('creating the pattern searcher')
# Instantiate the optimized PatternSearcher with the 'open' column and fixed template length
searcher = PatternSearcher(df['open'], template_length=m)

print('generating TSL ranges')
max_sl = 0.3
sl_steps = 30
stop_loss_percents, stop_loss_levels = generate_stop_loss_levels(max_sl, sl_steps)

print('calculating PL')
tsl_profits = calculate_pl(df, stop_loss_levels)

all_indices = np.arange(len(df['open']), dtype=np.int64)
np.random.shuffle(all_indices)
all_indices

print('loading a checkpoint')
# try to load a saved checkpoint
ckpt = load_ckpt()
results = []
if ckpt:
    results = ckpt.get('results', [])
    start_from = ckpt.get('start_from', 0)
    seen = ckpt.get('seen', np.zeros(len(df), dtype=int))
else:
    results = []
    start_from = 0
    seen = np.zeros(len(df), dtype=int)

print('backtesting')
N = 100 #len(all_indices) - start_from #1000
checkpoint_interval = 100
processed_count = 0  # Track processed patterns separately
tqdm.write(f'starting from {start_from}')
tqdm.write(f'processing {N} patterns, saving checkpoints every {checkpoint_interval} iterations')
for i in tqdm(range(start_from, start_from + N)):
    start_index = all_indices[i]
    # Skip if index is too close to end of data to create full window
    if start_index >= len(df) - m:
        start_from += 1
        continue
    # # (optional) optimization to not analyse similar points
    # if seen[start_index] > 0:
    #     continue
    pattern = create_window(df, start_index, m)
    r = searcher.search(pattern) # correlations
    r_limit = 0.98
    above_limit_mask = np.abs(r) > r_limit
    # start points of similar windows
    similar_starts = np.where(above_limit_mask)[0]
    if len(similar_starts) > 100:
        # entry points for trading (after pattern ends)
        entry_points = similar_starts + m
        profits_means = tsl_profits[:, entry_points].mean(axis=1)
        profits_max = max(profits_means)
        profits_stds = tsl_profits[:, entry_points].std(axis=1)
        #               index 0      index 1      index 2              index 3        index 4
        results.append((start_index, profits_max, len(similar_starts), profits_means, profits_stds))
    # if there is only one point with r > r_limit then it's the start_index with r == 1
    if len(similar_starts) == 1:
        # only one match (the pattern itself), mark just this index
        seen[start_index] = 1
    else:
        # multiple matches, mark all highly correlated patterns
        high_corr_mask = np.abs(r) > 0.98
        high_corr_starts = np.where(high_corr_mask)[0]
        seen[high_corr_starts] = 1
    start_from += 1
    processed_count += 1
    # Save checkpoint every N iterations
    if processed_count % checkpoint_interval == 0:
        tqdm.write(f'saving intermediate checkpoint at iteration {i}')
        checkpoint_data = {
            'results': results,
            'start_from': start_from,
            'seen': seen
        }
        save_ckpt(checkpoint_data)

for best in sorted(results, key=lambda x: x[1], reverse=True)[:3]:
    print(f'start_index = {best[0]}, max mean profit = {best[1]}, similar points = {best[2]}')
    print(f'mean tsl profits:\n{best[3]}')

print('saving the checkpoint')
checkpoint_data = {
    'results_pickle': results,
    'start_from': start_from,
    'seen': seen
}
save_ckpt(checkpoint_data)
print('completed')