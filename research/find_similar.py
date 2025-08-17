# This script searches for repeating price patterns in historical stock data.
# It identifies similar windows using correlation and saves checkpointed results for further analysis.
# The script is optimized for large datasets and reproducible research.
import numpy as np
import os
import pandas as pd
import random
from tqdm import tqdm

from data_downloader import download, get_filename
from pattern_analysis import create_window
from pattern_searcher import PatternSearcher
from checkpoints import load_ckpt, save_ckpt

ticker = 'AAPL'
interval = '5s'
year = '2024'
pattern_length = 60 # how many time points in the pattern.

# Set the random seed for reproducibility
random.seed(42)
np.random.seed(42) # seed for numpy
# Force fixed-point notation instead of scientific notation in prints
np.set_printoptions(suppress=True, precision=6)

print('loading prices')
filename = get_filename(ticker, interval, year)
if not os.path.exists(filename):
    # download data to the file on disk.
	download(ticker, interval, year)
# read data from the file on disk.
df = pd.read_parquet(filename)

print('creating the pattern searcher')
# Instantiate the optimized PatternSearcher with the 'open' column and fixed template length
searcher = PatternSearcher(df['open'], template_length=pattern_length)

# (optional) shuffle all indices in the df. this is to analyze incomplete results when i don't want to wait till the end
# but want to have the analysed points to be uniformly selected from the whole dataset rather than to check first points.
all_indices = np.arange(len(df['open']), dtype=np.int64)
np.random.shuffle(all_indices)

print('loading a checkpoint')
pwd = os.path.dirname(os.path.abspath(__file__)) # path to the current script
ckpt_dir = f'{pwd}/data/ckpt_{ticker}_{year}_{interval}'
ckpt = load_ckpt(ckpt_dir)
if ckpt:
    results = ckpt.get('results', [])
    start_from = ckpt.get('start_from', 0)
else:
    results = []
    start_from = 0

print('starting search')
N = len(all_indices) - start_from #1000
checkpoint_interval = 1000
processed_count = 0  # Track processed patterns separately for checkpoint saves.
tqdm.write(f'starting from {start_from}')
tqdm.write(f'processing {N} patterns, saving checkpoints every {checkpoint_interval} iterations')
for i in tqdm(range(start_from, start_from + N)):
    pattern_position = all_indices[i]
    # Skip if pattern position is too close to the end of data (not enough points to create a full-length window)
    if pattern_position >= len(df) - pattern_length:
        start_from += 1
        continue
    pattern = create_window(df, pattern_position, pattern_length)
    r = searcher.search(pattern) # correlations
    r_limit = 0.98
    above_limit_mask = r > r_limit
    # starting points of similar windows
    similar_starts = np.where(above_limit_mask)[0]
    if len(similar_starts) > 100:
        results.append((pattern_position, len(similar_starts)))
    start_from += 1
    processed_count += 1
    # Save checkpoint every N iterations
    if processed_count % checkpoint_interval == 0:
        tqdm.write(f'saving intermediate checkpoint at iteration {i}')
        checkpoint_data = {
            'results': results,
            'start_from': start_from,
        }
        save_ckpt(checkpoint_data, ckpt_dir)

print('saving the last checkpoint')
checkpoint_data = {
    'results_pickle': results,
    'start_from': start_from,
}
save_ckpt(checkpoint_data, ckpt_dir)

for best in sorted(results, key=lambda x: x[1], reverse=True)[:5]:
    print(f'start_index = {best[0]}, similar points = {best[1]}')
print('completed')