#!/bin/bash

# Build and run script for Polygon.io Data Viewer

echo "Building Polygon.io Data Viewer Docker container..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "Error: Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if data directory exists
if [ ! -d "../../polygon-data" ]; then
    echo "Error: ../../polygon-data directory not found."
    echo "Please run data download scripts first to create the data structure."
    exit 1
fi

echo "Building and starting containers..."
docker-compose up --build

echo "Application should be available at:"
echo "  - Main application: http://localhost:8000"
echo "  - With Nginx (production): http://localhost:80 (use: docker-compose --profile production up)"
