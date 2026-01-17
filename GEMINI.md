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

## Commit Message Guidelines

*   Always use one-line commit messages. They should be concise and summarize the changes effectively.

*   **Backend:**
    *   **Framework:** FastAPI (Python).
    *   **Location:** `viewer/backend/main.py`.
    *   **Service Logic**: `viewer/backend/main_service.py` handles data loading and viewport aggregation.
    *   **Running Backend**: Execute from project root: `export PYTHONPATH=$PYTHONPATH:$(pwd)/viewer/backend && python3 -m uvicorn main:app --port 8000 --app-dir viewer/backend`.
    *   **Data Availability**: In dev environment, only some tickers (AAPL, SPY) have full data. Others (like NVDA) may return "No data" even if they are in the ticker list.
    *   **APIs:**
        *   `/api/tickers`: Sorted by market cap.
        *   `/api/bars/{ticker}`: Used by Standard Viewer (Lightweight Charts).
        *   `/api/viewport/{ticker}`: Used by Infinite Zoom for high-resolution canvas rendering.

*   **Frontend:**
    *   **Framework:** SvelteKit.
    *   **Location:** `viewer/frontend`.
    *   **Routes:**
        *   `/`: Standard Viewer (Lightweight Charts).
        *   `/zoom`: Infinite Zoom Viewer (Custom Canvas Engine).
    *   **Components:**
        *   `src/lib/zoom/`: Contains `CanvasChart.svelte` and `ChartEngine.ts` for the infinite zoom logic.
    *   **Navigation**: Views are linked in the header; the selected ticker is passed via `?ticker=` URL parameter for a seamless transition.

## Technical Lessons & Constraints

*   **Smart Border Fetching (Failed Experiment)**: 
    *   Attempted to fetch "anchor" points outside the viewport to close gaps (weekends). 
    *   **Failure Cause**: Fragility in `pandas` vs `pyarrow` indexing and `KeyError` during metadata extraction for certain years. 
    *   **Current Solution**: Reverted to a simple **50% date range buffer**. It's stable but may show gaps on weekends. **Do not attempt to re-implement without a strictly typed data model.**
*   **Python Execution Environment**: 
    *   Backend must be run with `PYTHONPATH=$(pwd)/viewer/backend` and `--app-dir viewer.backend` from the project root.
    *   Failing to do so leads to `ModuleNotFoundError` for `main_service`.
*   **Port Conflicts**: 
    *   Vite (Frontend) defaults to 5173, but it can shift to 5174 if port is occupied by "zombie" processes. 
    *   Use `fuser -k PORT/tcp` to clean up before restarting.
