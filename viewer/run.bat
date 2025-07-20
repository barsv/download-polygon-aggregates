@echo off
REM Build and run script for Polygon.io Data Viewer on Windows

echo Building Polygon.io Data Viewer Docker container...

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Docker is not installed. Please install Docker Desktop first.
    exit /b 1
)

REM Check if docker-compose is available
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    docker compose version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Error: Docker Compose is not available. Please install Docker Compose first.
        exit /b 1
    )
)

REM Check if data directory exists
if not exist "..\..\polygon-data" (
    echo Error: ..\..\polygon-data directory not found.
    echo Please run data download scripts first to create the data structure.
    exit /b 1
)

echo Building and starting containers...
docker-compose up --build

echo.
echo Application should be available at:
echo   - Main application: http://localhost:8000
echo   - With Nginx (production): http://localhost:80 (use: docker-compose --profile production up)
