# Polygon.io Data Viewer

FastAPI backend + SvelteKit frontend for exploring local Polygon parquet data. Docker is no longer used; see legacy notes below if needed.

## Quick Start (Local Dev)

Prereqs
- Data prepared in `../../polygon-data/` (use root scripts like `download_bars.py`).
- Python env: `python -m venv venv && pip install -r requirements.txt`.
- Frontend deps: `cd viewer/frontend && npm install`.

Run
- Backend: `python -m uvicorn viewer.backend.main:app --reload --port 8000`
- Frontend: `cd viewer/frontend && npm run dev`
- Vite dev server proxies `/api` → `http://localhost:8000` (see `vite.config.ts`).

## Build Frontend
```bash
cd viewer/frontend
npm run build
```
Outputs static site to `viewer/frontend/build` (SvelteKit). Adjust adapter if you change deployment targets.

## Production via Nginx
- Serve built frontend as static files and proxy `/api` to the backend.
- Example TLS config: `viewer/nginx_prod.conf` (uses `root /var/www/barsv.com` and proxies to `127.0.0.1:8000`).
- Start backend with a process manager (systemd/supervisor) bound to `127.0.0.1:8000`.

## Data Layout
```
polygon-data/
├── bars/
│   ├── 1second/{TICKER}/{YEAR}.parquet
│   └── 1minute/{TICKER}.parquet
└── tickers/ticker_details.csv
```

## Legacy (Deprecated) Docker
Docker files were moved to `legacy/docker/` for reference and are not maintained. Prefer local dev + Nginx in production.
