# Multi-stage Docker build for Polygon.io Data Viewer
FROM node:20-alpine AS frontend-builder

# Set working directory for frontend build
WORKDIR /app/frontend

# Copy frontend package files
COPY viewer/frontend/package*.json ./
RUN npm install

# Copy frontend source code
COPY viewer/frontend/ ./

# Build the frontend
RUN npm run build

# Python backend stage
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python source code from project root
COPY aggregate_bars.py api_key.py load_ticker_details.py settings.py utils.py ./
COPY viewer/backend/ ./viewer/backend/

# Copy built frontend from previous stage
COPY --from=frontend-builder /app/frontend/build ./viewer/frontend/build

# Create necessary directories
RUN mkdir -p /data/polygon-data

# Expose port
EXPOSE 8000

# Copy startup script
COPY viewer/docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh

# Default command
CMD ["./docker-entrypoint.sh"]
