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
# Trade Distributions & Statistics
# PnL distributions, duration analysis, performance by side
# Ported from dash app distributions tab

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from scipy import stats
import os

# %%
# Load trades data
pwd = '/home/stan/src/download-polygon-aggregates/research/dash'
trades = pd.read_csv(f"{pwd}/trades.csv", parse_dates=["entry_ts", "exit_ts"]).sort_values("entry_ts")

print(f"Loaded {len(trades):,} trades")
print(f"PnL range: {trades['pnl'].min():.2f} to {trades['pnl'].max():.2f}")
print(f"Duration range: {trades['duration_s'].min():.0f}s to {trades['duration_s'].max():.0f}s")


# %%
# Helper functions

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

# Get available filter options
params_options = sorted(trades["params_hash"].astype(str).unique().tolist())
stoploss_options = sorted(trades["stop_loss"].unique().tolist())
side_options = ["ALL", "LONG", "SHORT"]

print(f"Available params_hash: {params_options[:5]}... ({len(params_options)} total)")
print(f"Available stop_loss: {stoploss_options}")

# %%
# Set analysis parameters - modify as needed
PARAMS_HASH = params_options[0] if params_options else None
STOP_LOSS = stoploss_options[0] if stoploss_options else None
SIDE = "ALL"  # "ALL", "LONG", or "SHORT"

# Filter trades
filtered_trades = filter_trades(trades, 
                               params_hash=PARAMS_HASH, 
                               stop_loss=STOP_LOSS, 
                               side=SIDE)

print(f"Filtered to {len(filtered_trades)} trades")
print(f"Parameters: params_hash={PARAMS_HASH}, stop_loss={STOP_LOSS}, side={SIDE}")

if filtered_trades.empty:
    print("No trades found for selected filters!")
else:
    print(f"PnL stats: mean={filtered_trades['pnl'].mean():.2f}, std={filtered_trades['pnl'].std():.2f}")
    print(f"Win rate: {(filtered_trades['pnl'] > 0).mean():.1%}")

# %%
# PnL Distribution Analysis
if not filtered_trades.empty:
    # Histogram with statistics
    fig_pnl = px.histogram(filtered_trades, x="pnl", nbins=50, 
                          title="PnL Distribution",
                          labels={"pnl": "PnL", "count": "Frequency"})
    
    # Add vertical lines for key statistics
    mean_pnl = filtered_trades['pnl'].mean()
    median_pnl = filtered_trades['pnl'].median()
    
    fig_pnl.add_vline(x=mean_pnl, line_dash="dash", line_color="red", 
                     annotation_text=f"Mean: {mean_pnl:.2f}")
    fig_pnl.add_vline(x=median_pnl, line_dash="dash", line_color="blue", 
                     annotation_text=f"Median: {median_pnl:.2f}")
    fig_pnl.add_vline(x=0, line_dash="solid", line_color="gray", opacity=0.5)
    
    fig_pnl.update_layout(height=500)
    fig_pnl.show(config={'scrollZoom': True})
    
    # Statistical tests
    shapiro_stat, shapiro_p = stats.shapiro(filtered_trades['pnl'].sample(min(5000, len(filtered_trades))))
    print(f"\nShapiro-Wilk normality test: stat={shapiro_stat:.4f}, p-value={shapiro_p:.4f}")
    print(f"Normal distribution: {'Yes' if shapiro_p > 0.05 else 'No'}")
    
    # Skewness and kurtosis
    skewness = stats.skew(filtered_trades['pnl'])
    kurtosis = stats.kurtosis(filtered_trades['pnl'])
    print(f"Skewness: {skewness:.3f} ({'right-skewed' if skewness > 0 else 'left-skewed' if skewness < 0 else 'symmetric'})")
    print(f"Kurtosis: {kurtosis:.3f} ({'heavy-tailed' if kurtosis > 0 else 'light-tailed'})")

# %%
# Duration Distribution Analysis
if not filtered_trades.empty:
    # Convert duration to minutes for better readability
    filtered_trades['duration_min'] = filtered_trades['duration_s'] / 60
    
    fig_duration = px.histogram(filtered_trades, x="duration_min", nbins=50,
                               title="Trade Duration Distribution",
                               labels={"duration_min": "Duration (minutes)", "count": "Frequency"})
    
    # Add statistics
    mean_duration = filtered_trades['duration_min'].mean()
    median_duration = filtered_trades['duration_min'].median()
    
    fig_duration.add_vline(x=mean_duration, line_dash="dash", line_color="red",
                          annotation_text=f"Mean: {mean_duration:.1f}min")
    fig_duration.add_vline(x=median_duration, line_dash="dash", line_color="blue",
                          annotation_text=f"Median: {median_duration:.1f}min")
    
    fig_duration.update_layout(height=500)
    fig_duration.show(config={'scrollZoom': True})
    
    print(f"Duration stats:")
    print(f"Mean: {mean_duration:.1f} minutes")
    print(f"Median: {median_duration:.1f} minutes")
    print(f"Min: {filtered_trades['duration_min'].min():.1f} minutes")
    print(f"Max: {filtered_trades['duration_min'].max():.1f} minutes")
    print(f"Std: {filtered_trades['duration_min'].std():.1f} minutes")

# %%
# PnL by Side Comparison (if both sides exist)
if 'side' in filtered_trades.columns and len(filtered_trades['side'].unique()) > 1:
    # Box plot
    fig_violin = px.violin(filtered_trades, y="pnl", color="side", box=True, points="outliers",
                          title="PnL Distribution by Side")
    fig_violin.update_layout(height=500)
    fig_violin.show(config={'scrollZoom': True})
    
    # Side-by-side statistics
    side_stats = filtered_trades.groupby('side')['pnl'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max', 
        lambda x: (x > 0).mean()  # win rate
    ]).round(3)
    side_stats.columns = ['Count', 'Mean', 'Median', 'Std', 'Min', 'Max', 'Win_Rate']
    
    print("\nPnL Statistics by Side:")
    display(side_stats)
    
    # Statistical test for difference
    if len(filtered_trades['side'].unique()) == 2:
        sides = filtered_trades['side'].unique()
        group1 = filtered_trades[filtered_trades['side'] == sides[0]]['pnl']
        group2 = filtered_trades[filtered_trades['side'] == sides[1]]['pnl']
        
        t_stat, t_p = stats.ttest_ind(group1, group2)
        mann_stat, mann_p = stats.mannwhitneyu(group1, group2, alternative='two-sided')
        
        print(f"\nStatistical Tests ({sides[0]} vs {sides[1]}):")
        print(f"T-test: stat={t_stat:.3f}, p-value={t_p:.4f}")
        print(f"Mann-Whitney U: stat={mann_stat:.1f}, p-value={mann_p:.4f}")
        print(f"Significant difference: {'Yes' if min(t_p, mann_p) < 0.05 else 'No'}")

# %%
# PnL vs Duration Scatter Plot
if not filtered_trades.empty:
    # Color by side if available
    color_col = 'side' if 'side' in filtered_trades.columns else None
    
    fig_scatter = px.scatter(filtered_trades, x="duration_min", y="pnl", 
                            color=color_col,
                            title="PnL vs Trade Duration",
                            labels={"duration_min": "Duration (minutes)", "pnl": "PnL"},
                            opacity=0.6)
    
    # Add horizontal line at y=0
    fig_scatter.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    fig_scatter.update_layout(height=500)
    fig_scatter.show(config={'scrollZoom': True})
    
    # Correlation analysis
    correlation = filtered_trades['pnl'].corr(filtered_trades['duration_min'])
    print(f"\nCorrelation between PnL and Duration: {correlation:.3f}")
    
    # Linear regression
    from sklearn.linear_model import LinearRegression
    X = filtered_trades[['duration_min']]
    y = filtered_trades['pnl']
    model = LinearRegression().fit(X, y)
    r_squared = model.score(X, y)
    
    print(f"R-squared: {r_squared:.3f}")
    print(f"Slope: {model.coef_[0]:.4f} (PnL change per minute)")

# %%
# Time-based Analysis
if not filtered_trades.empty:
    # Add time features
    filtered_trades['hour'] = filtered_trades['entry_ts'].dt.hour
    filtered_trades['day_of_week'] = filtered_trades['entry_ts'].dt.day_name()
    filtered_trades['month'] = filtered_trades['entry_ts'].dt.month_name()
    
    # PnL by hour of day
    hourly_pnl = filtered_trades.groupby('hour')['pnl'].agg(['mean', 'count']).reset_index()
    
    fig_hourly = px.bar(hourly_pnl, x='hour', y='mean', 
                       title="Average PnL by Hour of Day",
                       labels={"hour": "Hour", "mean": "Average PnL"})
    fig_hourly.add_hline(y=0, line_dash="dash", line_color="gray")
    fig_hourly.update_layout(height=400)
    fig_hourly.show(config={'scrollZoom': True})
    
    # PnL by day of week  
    daily_pnl = filtered_trades.groupby('day_of_week')['pnl'].agg(['mean', 'count']).reset_index()
    # Reorder days
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_pnl['day_of_week'] = pd.Categorical(daily_pnl['day_of_week'], categories=day_order, ordered=True)
    daily_pnl = daily_pnl.sort_values('day_of_week')
    
    fig_daily = px.bar(daily_pnl, x='day_of_week', y='mean',
                      title="Average PnL by Day of Week", 
                      labels={"day_of_week": "Day", "mean": "Average PnL"})
    fig_daily.add_hline(y=0, line_dash="dash", line_color="gray")
    fig_daily.update_layout(height=400)
    fig_daily.show(config={'scrollZoom': True})
    
    print("Best performing hours:")
    print(hourly_pnl.nlargest(3, 'mean')[['hour', 'mean', 'count']])
    
    print("\nBest performing days:")
    print(daily_pnl.nlargest(3, 'mean')[['day_of_week', 'mean', 'count']])

# %%
# Win/Loss Streaks Analysis
if not filtered_trades.empty:
    # Calculate win/loss streaks
    filtered_trades_sorted = filtered_trades.sort_values('entry_ts').copy()
    filtered_trades_sorted['is_win'] = filtered_trades_sorted['pnl'] > 0
    filtered_trades_sorted['streak_id'] = (filtered_trades_sorted['is_win'] != filtered_trades_sorted['is_win'].shift()).cumsum()
    
    streaks = filtered_trades_sorted.groupby('streak_id').agg({
        'is_win': ['first', 'count'],
        'pnl': 'sum',
        'entry_ts': ['first', 'last']
    }).reset_index()
    
    streaks.columns = ['streak_id', 'is_win', 'length', 'total_pnl', 'start_time', 'end_time']
    
    win_streaks = streaks[streaks['is_win']]['length']
    loss_streaks = streaks[~streaks['is_win']]['length']
    
    print("Streak Analysis:")
    print(f"Longest winning streak: {win_streaks.max() if not win_streaks.empty else 0} trades")
    print(f"Longest losing streak: {loss_streaks.max() if not loss_streaks.empty else 0} trades")
    print(f"Average winning streak: {win_streaks.mean():.1f} trades" if not win_streaks.empty else "No winning streaks")
    print(f"Average losing streak: {loss_streaks.mean():.1f} trades" if not loss_streaks.empty else "No losing streaks")
    
    # Histogram of streak lengths
    fig_streaks = go.Figure()
    
    if not win_streaks.empty:
        fig_streaks.add_trace(go.Histogram(x=win_streaks, name="Win Streaks", opacity=0.7, nbinsx=20))
    
    if not loss_streaks.empty:
        fig_streaks.add_trace(go.Histogram(x=loss_streaks, name="Loss Streaks", opacity=0.7, nbinsx=20))
    
    fig_streaks.update_layout(
        title="Distribution of Win/Loss Streak Lengths",
        xaxis_title="Streak Length (trades)",
        yaxis_title="Frequency",
        height=400
    )
    fig_streaks.show(config={'scrollZoom': True})
