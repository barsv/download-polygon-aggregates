#!/bin/bash

# Docker entrypoint script for Polygon.io Data Viewer

echo "Starting Polygon.io Data Viewer..."

# Set default environment variables if not provided
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

echo "Starting backend on ${HOST}:${PORT}..."

# Start the FastAPI backend
cd /app/viewer/backend
python -m uvicorn main:app --host ${HOST} --port ${PORT}
