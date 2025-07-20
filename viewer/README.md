# Polygon.io Data Viewer - Docker Setup

This directory contains the Docker configuration for the Polygon.io Data Viewer application, which combines a FastAPI backend with a SvelteKit frontend for visualizing financial market data.

## Quick Start

### Prerequisites

1. **Docker** and **Docker Compose** installed
2. **Data**: Download data first using the project's download scripts to create `../../polygon-data/` directory structure

### Running the Application

**On Linux/macOS:**
```bash
./run.sh
```

**On Windows:**
```cmd
run.bat
```

**Manual Docker Compose:**
```bash
docker-compose up --build
```

## Application Access

- **Main Application**: http://localhost:8000
- **Production with Nginx**: http://localhost:80 (use `docker-compose --profile production up`)

## Architecture

### Container Structure
- **polygon-viewer**: Combined FastAPI backend + SvelteKit frontend
- **nginx** (optional): Production reverse proxy

### Data Processing
- Reads second-level data from parquet files
- Automatically creates minute-level aggregates when needed
- Writes aggregated data back to the data directory

### Data Volumes
- `../../polygon-data` → `/data/polygon-data` (read-write for aggregation)

### Ports
- **8000**: FastAPI application (backend + frontend)
- **80**: Nginx reverse proxy (production mode)

## Directory Structure

```
viewer/
├── Dockerfile              # Multi-stage build (Node.js + Python)
├── docker-compose.yml      # Container orchestration
├── docker-entrypoint.sh    # Container startup script
├── nginx.conf             # Production reverse proxy config
├── run.sh                 # Unix launcher script
├── run.bat                # Windows launcher script
├── .dockerignore          # Docker build exclusions
└── README.md              # This file
```

## Development vs Production

### Development Mode (Default)
```bash
docker-compose up --build
```
- Direct access to FastAPI on port 8000
- CORS enabled for development
- Auto-reload enabled

### Production Mode
```bash
docker-compose --profile production up --build
```
- Nginx reverse proxy on port 80
- Optimized static file serving
- Production-ready configuration

## Troubleshooting

### Common Issues

1. **Port 8000 already in use**:
   ```bash
   docker-compose down
   # Or change port in docker-compose.yml
   ```

2. **Data not found**:
   - Run the data download scripts from the project root first
   - Ensure data files are in correct structure:
     ```
     polygon-data/
     ├── bars/
     │   ├── 1second/{ticker}/{year}.parquet
     │   └── 1minute/{ticker}.parquet
     └── tickers/ticker_details.csv
     ```

3. **API key issues**:
   - The viewer only reads local parquet files and doesn't require API keys
   - Check container logs: `docker-compose logs polygon-viewer`

### Checking Logs
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs polygon-viewer

# Follow logs
docker-compose logs -f
```

### Container Shell Access
```bash
docker-compose exec polygon-viewer bash
```

## Configuration

### Environment Variables
- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `8000`)

### Volume Mounts
Modify `docker-compose.yml` to change data locations:
```yaml
volumes:
  - /your/data/path:/data/polygon-data
```

## Building for Different Platforms

### For ARM64 (Apple Silicon)
```bash
docker buildx build --platform linux/arm64 -t polygon-viewer .
```

### For AMD64 (Intel/AMD)
```bash
docker buildx build --platform linux/amd64 -t polygon-viewer .
```

### Multi-platform
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t polygon-viewer .
```
