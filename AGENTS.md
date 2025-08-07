# Repository Guidelines

## Project Structure & Module Organization
- Root: Python scripts for data download and processing (e.g., `download_bars.py`, `aggregate_bars.py`).
- Data: Configured in `settings.py` via `DATA_DIR` → default `../polygon-data` (outside repo).
- Viewer: Full-stack viewer in `viewer/` (FastAPI backend + SvelteKit frontend, Dockerized).
- Research: Notebooks and prototypes in `research/`.
- Docs: Additional notes in `documentation/`.

## Build, Test, and Development Commands
- Setup env: `python -m venv venv && pip install -r requirements.txt`.
- Configure keys: put Polygon API key in `api_key.txt` (and optional `api_key_id.txt` for flat files) at repo root.
- Download examples:
  - Minute/second bars: `python download_bars.py` (default runs 1s SPY). 
  - All tickers history: `python download_tickers_history.py` → writes to `../polygon-data/tickers/`.
  - Ticker details: `python download_ticker_overview.py` then `python save_tickers_first_last_active.py`.
  - Aggregate 1s→1m: `python aggregate_bars.py AAPL` → `../polygon-data/bars/1minute/AAPL.parquet`.
- Viewer (local):
  - Backend: `python -m uvicorn viewer.backend.main:app --reload --port 8000`.
  - Frontend: `cd viewer/frontend && npm install && npm run dev` (Vite dev proxies `/api` → `http://localhost:8000`).

## Coding Style & Naming Conventions
- Python: 4-space indentation, `snake_case` for files/functions, module-level constants in `UPPER_SNAKE_CASE`.
- Logging: prefer `logging` with `utils.setup_logger()` over `print` in long-running scripts.
- Paths: write only under `settings.ABSOLUTE_DATA_DIR` (e.g., `bars/1second/{TICKER}/{YEAR}.parquet`).

## Testing Guidelines
- No formal test suite; validate by spot-runs and file checks.
- Sanity checks:
  - After a run, verify files exist, e.g., `../polygon-data/bars/1second/SPY/2024.parquet`.
  - Aggregation: confirm `../polygon-data/bars/1minute/{T}.parquet` is created and readable.
  - Viewer API: `curl 'http://localhost:8000/api/bars/SPY?interval=1min'` returns OHLC JSON.

## Commit & Pull Request Guidelines
- Commits: short, imperative, and scoped (e.g., `aggregate: create 1m from 1s`, `viewer: add download endpoint`).
- PRs: include purpose, how to run, sample output/paths touched, and any data prerequisites; link issues when applicable.
- Avoid mixing data dumps with code changes; exclude secrets and large artifacts.

## Security & Configuration Tips
- Secrets: keep `api_key.txt` and `api_key_id.txt` local and untracked; never commit keys.
- Data location: adjust `DATA_DIR` in `settings.py` if needed; ensure the target directory is writable.
- Rate limits: download scripts implement basic retries; prefer narrower date ranges when experimenting.
