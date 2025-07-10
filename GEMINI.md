# Gemini Project Knowledge Base

## Project Overview

This project consists of two main parts:
1. A collection of Python scripts to download financial data from polygon.io.
2. A web-based data viewer to visualize the downloaded data.

## Key Information

*   **Data Storage:** All downloaded data is stored in the `../polygon-data` directory, which is outside the main project directory. The agent cannot access this directory directly, but the backend scripts can.
*   **Bar Data Structure:** Time-series data (bars) is stored in `.parquet` files, organized by resolution, ticker, and year. For example: `../polygon-data/bars/1second/AAPL/2023.parquet`.

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
