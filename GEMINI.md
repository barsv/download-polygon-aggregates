# Gemini Project Knowledge Base

## Project Overview

This project consists of two main parts:
1. A collection of Python scripts to download financial data from polygon.io.
2. A web-based data viewer to visualize the downloaded data.

## Key Information

*   **Data Storage:** All downloaded data is stored in the `../polygon-data` directory, which is outside the main project directory. The agent cannot access this directory directly, but the backend scripts can.
*   **Bar Data Structure:** Time-series data (bars) is stored in `.parquet` files, organized by resolution, ticker, and year. For example: `../polygon-data/bars/1second/AAPL/2023.parquet`.
*   **Dir structure** 
  polygon-data ls
bars  condition-codes  exchanges  flatfiles  raw_daily  stock_data  tickers
➜  polygon-data cd ..
➜  src cd polygon-data
➜  polygon-data pwd
/home/stan/src/polygon-data
➜  polygon-data cd ../download-polygon-aggregates
➜  download-polygon-aggregates git:(main) ✗ ls
api_key_id.txt  documentation         download_condition_codes.py  download_ticker_overview.py  download_trades.py  requirements.txt                   settings.py  utils.py
api_key.py      download_all_bars.py  download_exchanges.py        download_tickers_history.py  __pycache__         research                           tmp.txt      venv
api_key.txt     download_bars.py      download_raw_daily.py        download_ticker_types.py     README.md           save_tickers_first_last_active.py  todo.md      viewer
➜  download-polygon-aggregates git:(main) ✗ cd ../polygon-data
➜  polygon-data ls
bars  condition-codes  exchanges  flatfiles  raw_daily  stock_data  tickers
➜  polygon-data cd tickers
➜  tickers ls
ticker_details.csv             tickers_history_active.csv    tickers_renames.csv  unique_active_dates.csv
tickers_first_last_active.csv  tickers_history_inactive.csv  ticker_types.csv     unique_inactive_dates.csv
➜  tickers cd ../bars
➜  bars ls
1minute  1second
➜  bars cd 1second
➜  1second ls
AAPL  SPY
➜  1second tree
.
├── AAPL
│   ├── 2003.parquet
│   ├── 2004.parquet
│   ├── 2005.parquet
│   ├── 2006.parquet
│   ├── 2007.parquet
│   ├── 2008.parquet
│   ├── 2009.parquet
│   ├── 2010.parquet
│   ├── 2011.parquet
│   ├── 2012.parquet
│   ├── 2013.parquet
│   ├── 2014.parquet
│   ├── 2015.parquet
│   ├── 2016.parquet
│   ├── 2017.parquet
│   ├── 2018.parquet
│   ├── 2019.parquet
│   ├── 2020.parquet
│   ├── 2021.parquet
│   ├── 2022.parquet
│   ├── 2023.parquet
│   ├── 2024.parquet
│   └── 2025.parquet
└── SPY
    ├── 2024.parquet
    └── 2025.parquet

2 directories, 25 files
➜  1second


## Viewer Application

The viewer is located in the `viewer/` directory and has a separate frontend and backend.

*   **Backend:**
    *   **Framework:** FastAPI (Python).
    *   **Location:** `viewer/backend/main.py`.
    *   **APIs:**
        *   `/api/tickers`: Provides a list of all available tickers, sorted by market cap. It lazy-loads `ticker_details.csv` on the first request.
        *   `/api/bars/{ticker}`: Provides bar data for a given ticker. It accepts `from_timestamp` and `to_timestamp` query parameters to fetch data for specific time ranges. It intelligently reads only the necessary yearly `.parquet` files based on the requested range. For the initial load, it returns the last 2000 data points from the most recent year.

*   **Frontend:**
    *   **Framework:** Svelte with `lightweight-charts`.
    *   **Location:** `viewer/frontend/src/App.svelte`.
    *   **Functionality:** Displays candlestick charts. It implements dynamic data loading: it initially loads the most recent data, and as the user scrolls back in time, it automatically fetches older data from the backend in 1-day chunks.
