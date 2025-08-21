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

# %%
# Price & Trades Analysis
# Interactive visualization of OHLC data with trade entries and exits

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly_resampler import FigureResampler, FigureWidgetResampler
from plotly_resampler.aggregation import MinMaxLTTB
import os
import sys

# Add research directory to path
sys.path.append('/home/stan/src/download-polygon-aggregates/research')
from data_downloader import get_filename

# %%
# Load OHLC bars and trades data
# Configuration
ticker = 'AAPL'
interval = '5s'
year = '2024'

# Load OHLC data
pwd = '/home/stan/src/download-polygon-aggregates/research/data'
filename = get_filename(ticker, interval, year)
bars = pd.read_parquet(f'{pwd}/../{filename}')
bars['timestamp'] = pd.to_datetime(bars['timestamp'], unit='s')

# Load trades data
trades = pd.read_csv(f"{pwd}/trades.csv", parse_dates=["entry_ts", "exit_ts"]).sort_values("entry_ts")

print(f"Loaded {len(bars):,} bars and {len(trades):,} trades")
print(f"Data period: {bars['timestamp'].min()} to {bars['timestamp'].max()}")
print(f"Trades period: {trades['entry_ts'].min()} to {trades['exit_ts'].max()}")


# %%
# Helper functions for filtering trades and creating charts

def filter_trades(trades_df, params_hash=None, stop_loss=None, side="ALL"):
    """Filter trades by parameters"""
    df = trades_df.copy()
    
    if params_hash is not None:
        df = df[df["params_hash"].astype(str) == str(params_hash)]
    
    if stop_loss is not None:
        df = df[df["stop_loss"] == stop_loss]
    
    if side == "LONG":
        df = df[df["side"].str.lower() == "long"]
    elif side == "SHORT":
        df = df[df["side"].str.lower() == "short"]
    
    return df

def create_price_chart(bars_df, trades_df):
    from plotly_resampler import FigureWidgetResampler
    import plotly.graph_objects as go
    import numpy as np
    import pandas as pd

    bars_df = bars_df.copy()
    if not np.issubdtype(bars_df["timestamp"].dtype, np.datetime64):
        bars_df["timestamp"] = pd.to_datetime(bars_df["timestamp"])
    ts = bars_df["timestamp"].values

    # Base widget + resampler wrapper
    base = go.FigureWidget()
    fig = FigureWidgetResampler(base)

    # main line only
    fig.add_trace(go.Scattergl(mode="lines", name="Close"), hf_x=ts, hf_y=bars_df["close"])

    # (optional) trades overlay — как у тебя

    fig.update_layout(
        height=600, margin=dict(l=50, r=50, t=20, b=20),
        xaxis_rangeslider_visible=False, hovermode="x unified", dragmode="pan",
    )
    fig.update_yaxes(autorange=True, fixedrange=False)

    # keep wheel zoom
    fig._config = {**(getattr(fig, "_config", {}) or {}), "scrollZoom": True}

    # ---------- Auto Y on zoom/pan ----------
    def _extract_xrange(delta):
        # delta может быть dict ИЛИ списком патчей — поддержим оба
        if isinstance(delta, list) and delta and isinstance(delta[-1], dict):
            delta = delta[-1]
        if not isinstance(delta, dict):
            return None
        x0 = delta.get("xaxis.range[0]")
        x1 = delta.get("xaxis.range[1]")
        if x0 is not None and x1 is not None:
            return (pd.to_datetime(x0), pd.to_datetime(x1))
        rng = delta.get("xaxis.range")
        if isinstance(rng, (list, tuple)) and len(rng) == 2:
            return (pd.to_datetime(rng[0]), pd.to_datetime(rng[1]))
        if delta.get("xaxis.autorange") is True:
            return (bars_df["timestamp"].min(), bars_df["timestamp"].max())
        return None

    def _apply_visible_y_range(xr):
        if not xr:
            return
        x0, x1 = xr
        vis = bars_df[(bars_df["timestamp"] >= x0) & (bars_df["timestamp"] <= x1)]
        if vis.empty:
            return
        y_min = float(vis["low"].min())
        y_max = float(vis["high"].max())
        if not np.isfinite(y_min) or not np.isfinite(y_max) or y_min == y_max:
            return
        pad = (y_max - y_min) * 0.05
        with fig.batch_update():
            fig.layout.yaxis.range = [y_min - pad, y_max + pad]

    def _relayout_observer(change):
        xr = _extract_xrange(change.get("new"))
        _apply_visible_y_range(xr)

    # 👉 ВАЖНО: наблюдатель вешаем на БАЗОВЫЙ FigureWidget, не на fig!
    base.observe(_relayout_observer, names=["_js2py_layoutDelta"], type="change")

    # Одноразовый первичный автоскейл по всему диапазону (приятнее на старте)
    _apply_visible_y_range((bars_df["timestamp"].min(), bars_df["timestamp"].max()))

    return fig



def get_zoomed_trades(trades, fig):
    """Get trades filtered by current zoom range on the chart"""
    
    if fig is None:
        print("No chart available")
        return trades
    
    # Get current visible range from the chart
    current_range = fig.layout.xaxis.range
    
    if not current_range:
        return trades
    
    if len(trades) == 0:
        return trades
    
    # Convert range to datetime objects
    start_time = pd.to_datetime(current_range[0])
    end_time = pd.to_datetime(current_range[1])
    
    # Filter trades by entry time within visible range
    zoomed_trades = trades[
        (trades["entry_ts"] >= start_time) & 
        (trades["entry_ts"] <= end_time)
    ]
    return zoomed_trades

def show_trades_table(trades, fig):
    """Show trades table for current zoom range"""
    zoomed_trades = get_zoomed_trades(trades, fig)
    
    if len(zoomed_trades) == 0:
        print("No trades in current zoom range")
        return
    
    trades_display = zoomed_trades[[
        'trade_id', 'side', 'entry_ts', 'entry_price', 
        'exit_ts', 'exit_price', 'pnl', 'pnl_pct', 
        'stop_loss', 'duration_s'
    ]].round(5)
    display(trades_display)

    print(f"Trades in zoom range: {len(zoomed_trades)}")
    print(f"Total PnL: {zoomed_trades['pnl'].sum():.2f}")
    print(f"Win rate: {(zoomed_trades['pnl'] > 0).mean():.1%}")
    print(f"Avg PnL: {zoomed_trades['pnl'].mean():.2f}")

# Get available filter options
params_options = sorted(trades["params_hash"].astype(str).unique().tolist())
stoploss_options = sorted(trades["stop_loss"].unique().tolist())
side_options = ["ALL", "LONG", "SHORT"]

print(f"Available params_hash: {params_options[:5]}... ({len(params_options)} total)")
print(f"Available stop_loss: {stoploss_options}")
print(f"Available sides: {side_options}")

# %%
PARAMS_HASH = params_options[0]
STOP_LOSS = stoploss_options[0]
SIDE = "ALL"

custom_trades = []
def apply_filters():
    global custom_trades
    custom_trades = filter_trades(trades, 
                                params_hash=PARAMS_HASH, 
                                stop_loss=STOP_LOSS, 
                                side=SIDE)



# %%
PARAMS_HASH = params_options[0]
STOP_LOSS = stoploss_options[0]
SIDE = "ALL" # "ALL", "LONG", or "SHORT"

apply_filters()
fg = create_price_chart(bars, [])
fg  # Display the chart

# %%
show_trades_table(custom_trades, fg)  # Shows only trades in zoomed range

# %%
# Quick statistics summary
if not custom_trades.empty:
    stats = {
        'Total Trades': len(custom_trades),
        'Total PnL': custom_trades['pnl'].sum(),
        'Win Rate': (custom_trades['pnl'] > 0).mean(),
        'Average PnL': custom_trades['pnl'].mean(),
        'Best Trade': custom_trades['pnl'].max(),
        'Worst Trade': custom_trades['pnl'].min(),
        'Avg Duration (s)': custom_trades['duration_s'].mean(),
        'Long Trades': (custom_trades['side'].str.lower() == 'long').sum(),
        'Short Trades': (custom_trades['side'].str.lower() == 'short').sum(),
    }
    
    stats_df = pd.DataFrame(list(stats.items()), columns=['Metric', 'Value'])
    display(stats_df)
else:
    print("No trades found for selected filters")
