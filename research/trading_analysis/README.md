# Trading Analysis Notebooks

Analysis of trading strategy results, ported from Dash app to separate Jupyter notebooks for research and post-download analytics.

## Notebooks

### 1. `price_trades.ipynb`
- Visualization of OHLC data with trade entry/exit markers
- Interactive charts using plotly + FigureResampler for large datasets
- Filtering by parameters: `params_hash`, `stop_loss`, `side`
- Display modes: line (for performance) and candles
- Trades table and quick stats

### 2. `equity_curve.ipynb`
- Equity curve (cumulative PnL over time)
- Drawdown analysis
- Comparison of Long vs Short positions
- Rolling performance metrics
- Key indicators: profit factor, max drawdown, win rate

### 3. `distributions.ipynb`
- PnL and trade duration distributions
- Statistical tests (normality, skewness, kurtosis)
- Performance analysis by time (hour of day, day of week)
- Win/loss streak analysis
- Correlation analysis: PnL vs duration

## Usage

1. Open the desired notebook
2. Change parameters in the relevant code cell:
   - `PARAMS_HASH` - strategy parameter hash
   - `STOP_LOSS` - stop-loss level
   - `SIDE` - direction ("ALL", "LONG", "SHORT")
3. Run cells sequentially for analysis

## Advantages over Dash

- Deeper analysis with extra statistics
- Easy modification and experimentation
- Save analysis results
- Separate notebooks for different aspects (better navigation)
- Easy to add custom analysis

## Data

- OHLC bars: loaded via `data_downloader.get_filename()`
- Trades: `../dash/trades.csv`
- All parameters are easily changed at the top of each notebook
