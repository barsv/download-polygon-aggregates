# ---
# jupyter:
#   jupytext:
#     hide_notebook_metadata: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# HoloViews + Datashader: Price with Trades (interactive)
# - Fast line rendering for millions of points via Datashader
# - Zoom/pan with stable layout (no jitter)
# - Trades overlay filtered by visible x-range

# %%
import os
import pandas as pd
import numpy as np

import holoviews as hv
import hvplot.pandas  # noqa: F401 - registers .hvplot
from holoviews.operation.datashader import datashade, dynspread
from holoviews.streams import RangeX

# Jupyter+HoloViews (Bokeh backend)
hv.extension("bokeh")

# Add project research path to import helpers
import sys
sys.path.append('/home/stan/src/download-polygon-aggregates/research')
from data_downloader import get_filename  # noqa: E402


# %%
# Configuration
ticker = 'AAPL'
interval = '5s'
year = '2024'

# Data locations (mirrors price_trades.py approach)
pwd = '/home/stan/src/download-polygon-aggregates/research/data'
bars_path = os.path.join(pwd, '..', get_filename(ticker, interval, year))
trades_path = os.path.join(pwd, 'trades.csv')

print(f"Bars path: {os.path.abspath(bars_path)}")
print(f"Trades path: {os.path.abspath(trades_path)}")


# %%
# Load OHLC bars
bars = pd.read_parquet(bars_path)
# Normalize timestamps to timezone-naive (ns) to satisfy datashader
if np.issubdtype(bars['timestamp'].dtype, np.number):
    ts = pd.to_datetime(bars['timestamp'], unit='s', utc=True)
else:
    ts = pd.to_datetime(bars['timestamp'], utc=True)
# Drop timezone info while keeping UTC instants
bars['timestamp'] = ts.dt.tz_convert('UTC').dt.tz_localize(None)
bars = bars.sort_values('timestamp').reset_index(drop=True)

print(f"Loaded bars: {len(bars):,} rows from {bars['timestamp'].min()} to {bars['timestamp'].max()}")


# %%
# Load trades (optional)
if os.path.exists(trades_path):
    trades = pd.read_csv(trades_path, parse_dates=["entry_ts", "exit_ts"]).sort_values("entry_ts")
    # Normalize trade timestamps to timezone-naive
    trades['entry_ts'] = pd.to_datetime(trades['entry_ts'], utc=True).dt.tz_convert('UTC').dt.tz_localize(None)
    trades['exit_ts'] = pd.to_datetime(trades['exit_ts'], utc=True).dt.tz_convert('UTC').dt.tz_localize(None)
    # Normalize column names if needed
    if 'side' in trades.columns:
        trades['side'] = trades['side'].astype(str).str.lower()
    print(f"Loaded trades: {len(trades):,} rows from {trades['entry_ts'].min()} to {trades['exit_ts'].max()}")
else:
    # Empty placeholder to keep overlay logic simple
    trades = pd.DataFrame(columns=['trade_id','side','entry_ts','entry_price','exit_ts','exit_price','pnl'])
    print("Trades file not found — overlay disabled until you provide research/data/trades.csv")


# %%
# Base price curve (close line) -> Datashader for fast rendering
curve = hv.Curve(bars, kdims='timestamp', vdims='close')
# Use default aggregator; passing None triggers a validation error
shaded = dynspread(datashade(curve, width=1200, height=500))

# Visible x-range stream (drives dynamic overlays)
rng = RangeX(source=shaded)


# %%
# Dynamic view: recompute trades overlay and set ylim based on visible window
def _view(x_range):
    # X window
    if x_range is None:
        x0, x1 = bars['timestamp'].min(), bars['timestamp'].max()
    else:
        x0, x1 = pd.to_datetime(x_range[0]), pd.to_datetime(x_range[1])

    # Visible OHLC range -> y limits
    vis = bars[(bars['timestamp'] >= x0) & (bars['timestamp'] <= x1)]
    if vis.empty:
        y0, y1 = float(bars['close'].min()), float(bars['close'].max())
    else:
        cols_low = [c for c in ['low','close'] if c in vis.columns]
        cols_high = [c for c in ['high','close'] if c in vis.columns]
        y_min = float(np.nanmin(vis[cols_low].min()))
        y_max = float(np.nanmax(vis[cols_high].max()))
        pad = (y_max - y_min) * 0.05 if np.isfinite(y_max - y_min) else 0.0
        y0, y1 = y_min - pad, y_max + pad

    # Trades overlay within window
    if trades.empty:
        points = hv.Points([])
    else:
        dt = trades if x_range is None else trades[(trades['entry_ts'] >= x0) & (trades['entry_ts'] <= x1)]
        buys = dt[dt['side'] == 'long'] if 'side' in dt.columns else dt.iloc[0:0]
        sells = dt[dt['side'] == 'short'] if 'side' in dt.columns else dt.iloc[0:0]
        p_buys = hv.Points(buys, kdims=['entry_ts','entry_price']).opts(color='green', size=6, marker='triangle', alpha=0.9) if not buys.empty else hv.Points([])
        p_sells = hv.Points(sells, kdims=['entry_ts','entry_price']).opts(color='red', size=6, marker='inverted_triangle', alpha=0.9) if not sells.empty else hv.Points([])
        points = p_buys * p_sells

    return (shaded * points).opts(ylim=(y0, y1))

plot = hv.DynamicMap(_view, streams=[rng]).opts(
    hv.opts.Overlay(
        width=1200, height=500, toolbar='above',
        tools=['xwheel_zoom','xpan','reset','crosshair','hover'],
        active_tools=['xwheel_zoom'],
        show_grid=True,
        framewise=True,
    ),
    hv.opts.Curve(line_color='#3b7dd8'),
)

plot


# %% [markdown]
# Notes
# - Wheel zoom (x-only) and pan are enabled; borders are fixed to avoid layout jitter.
# - Datashader rasterizes the price curve for speed. Trades are drawn as vector glyphs only for the visible window.
# - Provide trades at research/data/trades.csv with columns:
#   trade_id, side in {long,short}, entry_ts, entry_price, exit_ts, exit_price, pnl, ...
# - To sync this .py with a .ipynb, use tools/jupytext_sync.sh
