# Polygon.io Data Viewer

FastAPI backend + SvelteKit frontend for exploring local Polygon parquet data. Docker is no longer used; see legacy notes below if needed.

## Quick Start (Local Dev)

Prereqs
- Data prepared in `../../polygon-data/` (use root scripts like `download_bars.py`).
- Python env: `python -m venv venv && pip install -r requirements.txt`.
- Frontend deps: `cd viewer/frontend && npm install`.

Run
- Backend: `cd viewer/backend && python -m uvicorn main:app --reload --port 8000`
- Frontend: `cd viewer/frontend && npm run dev`
- Vite dev server proxies `/api` → `http://localhost:8000` (see `vite.config.ts`).

## Build Frontend
```bash
cd viewer/frontend
npm run build
```
Outputs static site to `viewer/frontend/build` (SvelteKit). Adjust adapter if you change deployment targets.

## Production Deployment

The application is deployed on a local server (laptop) with an 8TB external drive for data.

### 1. Update Code
On the server, pull the latest changes:
```bash
git pull
```

### 2. Frontend Deployment (Nginx)
1. Build the frontend:
   ```bash
   cd viewer/frontend
   npm run build
   ```
2. Copy the build to the web directory:
   ```bash
   sudo cp -r build/* /var/www/barsv.com/
   ```
3. Ensure Nginx is configured (see `viewer/nginx_prod.conf`).

### 3. Backend Deployment (systemd)
1. The backend runs as a systemd service.
2. The service file is located at `viewer/polygon-backend.service`.
3. To install/update the service:
   ```bash
   sudo cp viewer/polygon-backend.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable polygon-backend
   ```
4. To restart the backend after code updates:
   ```bash
   sudo systemctl restart polygon-backend
   ```
5. To check logs:
   ```bash
   journalctl -u polygon-backend -f
   ```

### 4. DDNS (Porkbun)
If the server IP is dynamic, the DDNS script updates the `barsv.com` DNS record:
- Config: `viewer/porkbun/porkbun.env` (API keys).
- The script is triggered via crontab (see `viewer/porkbun/install.sh`).

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
