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
# Equity Curve Analysis
# Portfolio performance over time, cumulative PnL tracking
# Ported from dash app equity tab

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import os

# %%
# Load trades data
pwd = '/home/stan/src/download-polygon-aggregates/research/dash'
trades = pd.read_csv(f"{pwd}/trades.csv", parse_dates=["entry_ts", "exit_ts"]).sort_values("entry_ts")

print(f"Loaded {len(trades):,} trades")
print(f"Date range: {trades['entry_ts'].min()} to {trades['exit_ts'].max()}")
print(f"Total PnL: {trades['pnl'].sum():.2f}")


# %%
# Helper functions for filtering and equity calculation

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

def make_equity_curve(df_trades):
    """Create equity curve from trades"""
    if df_trades.empty:
        return pd.DataFrame(columns=['timestamp', 'equity'])
    
    eq = df_trades[["exit_ts", "pnl"]].copy()
    eq = eq.rename(columns={"exit_ts": "timestamp"})
    eq["equity"] = eq["pnl"].cumsum()
    return eq.sort_values('timestamp')

def create_equity_chart(df_trades, title="Equity Curve"):
    """Create equity curve chart"""
    eq = make_equity_curve(df_trades)
    
    if eq.empty:
        fig = go.Figure()
        fig.add_annotation(text="No trades for selection", 
                          xref="paper", yref="paper",
                          x=0.5, y=0.5, showarrow=False)
        return fig
    
    fig = go.Figure()
    
    # Main equity line
    fig.add_trace(go.Scatter(
        x=eq["timestamp"], 
        y=eq["equity"], 
        mode="lines", 
        name="Equity",
        line=dict(width=2, color="blue")
    ))
    
    # Add zero line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    # Highlight drawdown periods (negative equity)
    negative_periods = eq[eq['equity'] < 0]
    if not negative_periods.empty:
        fig.add_trace(go.Scatter(
            x=negative_periods["timestamp"], 
            y=negative_periods["equity"], 
            mode="lines", 
            name="Drawdown",
            line=dict(width=3, color="red"),
            opacity=0.7
        ))
    
    fig.update_layout(
        title=title,
        height=500,
        xaxis_title="Time",
        yaxis_title="Cumulative PnL",
        showlegend=True
    )
    
    return fig

# Get available filter options
params_options = sorted(trades["params_hash"].astype(str).unique().tolist())
stoploss_options = sorted(trades["stop_loss"].unique().tolist())
side_options = ["ALL", "LONG", "SHORT"]

print(f"Available params_hash: {params_options[:5]}... ({len(params_options)} total)")
print(f"Available stop_loss: {stoploss_options}")

# %%
# Overall equity curve (all trades)
fig_all = create_equity_chart(trades, "Overall Equity Curve - All Trades")
fig_all.show(config={'scrollZoom': True})

eq_all = make_equity_curve(trades)
if not eq_all.empty:
    print(f"Final equity: {eq_all['equity'].iloc[-1]:.2f}")
    print(f"Max equity: {eq_all['equity'].max():.2f}")
    print(f"Min equity: {eq_all['equity'].min():.2f}")
    print(f"Max drawdown: {eq_all['equity'].max() - eq_all['equity'].min():.2f}")

# %%
# Custom equity analysis - modify parameters
PARAMS_HASH = params_options[0] if params_options else None  # Change as needed
STOP_LOSS = stoploss_options[0] if stoploss_options else None # Change as needed
SIDE = "ALL"  # "ALL", "LONG", or "SHORT"

# Filter trades
filtered_trades = filter_trades(trades, 
                               params_hash=PARAMS_HASH, 
                               stop_loss=STOP_LOSS, 
                               side=SIDE)

print(f"Filtered to {len(filtered_trades)} trades")
print(f"Parameters: params_hash={PARAMS_HASH}, stop_loss={STOP_LOSS}, side={SIDE}")

# Create equity chart
fig_filtered = create_equity_chart(filtered_trades, 
                                  f"Equity Curve - {SIDE} trades, SL={STOP_LOSS}")
fig_filtered.show(config={'scrollZoom': True})

# %%
# Equity statistics and metrics
eq_filtered = make_equity_curve(filtered_trades)

if not eq_filtered.empty:
    # Calculate drawdown series
    running_max = eq_filtered['equity'].expanding().max()
    drawdown = eq_filtered['equity'] - running_max
    
    # Calculate key metrics
    metrics = {
        'Total Trades': len(filtered_trades),
        'Final Equity': eq_filtered['equity'].iloc[-1],
        'Total Return': eq_filtered['equity'].iloc[-1],
        'Max Equity': eq_filtered['equity'].max(),
        'Min Equity': eq_filtered['equity'].min(),
        'Max Drawdown': drawdown.min(),
        'Max Drawdown %': (drawdown.min() / running_max.max() * 100) if running_max.max() > 0 else 0,
        'Win Rate': (filtered_trades['pnl'] > 0).mean(),
        'Avg Trade PnL': filtered_trades['pnl'].mean(),
        'Best Trade': filtered_trades['pnl'].max(),
        'Worst Trade': filtered_trades['pnl'].min(),
        'Profit Factor': filtered_trades[filtered_trades['pnl'] > 0]['pnl'].sum() / abs(filtered_trades[filtered_trades['pnl'] < 0]['pnl'].sum()) if (filtered_trades['pnl'] < 0).any() else float('inf'),
    }
    
    metrics_df = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
    display(metrics_df)
    
    # Show periods of drawdown
    if drawdown.min() < 0:
        print("\nDrawdown periods:")
        dd_periods = eq_filtered[drawdown < -0.01]  # Show significant drawdowns
        if not dd_periods.empty:
            print(f"Longest drawdown period: {dd_periods['timestamp'].min()} to {dd_periods['timestamp'].max()}")
            print(f"Days in drawdown: {(dd_periods['timestamp'].max() - dd_periods['timestamp'].min()).days}")
else:
    print("No trades found for selected filters")

# %%
# Compare equity curves by side (Long vs Short)
if len(stoploss_options) > 0:
    fig_comparison = go.Figure()
    
    for side in ["LONG", "SHORT"]:
        side_trades = filter_trades(trades, 
                                   params_hash=PARAMS_HASH, 
                                   stop_loss=STOP_LOSS, 
                                   side=side)
        if not side_trades.empty:
            eq_side = make_equity_curve(side_trades)
            fig_comparison.add_trace(go.Scatter(
                x=eq_side["timestamp"], 
                y=eq_side["equity"], 
                mode="lines", 
                name=f"{side} Equity",
                line=dict(width=2)
            ))
    
    fig_comparison.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig_comparison.update_layout(
        title="Equity Comparison: Long vs Short",
        height=500,
        xaxis_title="Time",
        yaxis_title="Cumulative PnL"
    )
    fig_comparison.show(config={'scrollZoom': True})

# %%
# Rolling performance metrics (if enough trades)
if len(filtered_trades) > 50:
    eq_filtered['rolling_30'] = eq_filtered['equity'].rolling(window=30, min_periods=1).apply(lambda x: x.iloc[-1] - x.iloc[0])
    
    fig_rolling = go.Figure()
    fig_rolling.add_trace(go.Scatter(
        x=eq_filtered["timestamp"], 
        y=eq_filtered["rolling_30"], 
        mode="lines", 
        name="30-Trade Rolling PnL",
        line=dict(width=2, color="orange")
    ))
    
    fig_rolling.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig_rolling.update_layout(
        title="Rolling Performance (30-trade windows)",
        height=400,
        xaxis_title="Time",
        yaxis_title="Rolling PnL"
    )
    fig_rolling.show(config={'scrollZoom': True})
else:
    print("Not enough trades for rolling analysis (need >50)")
