# Copilot Instructions for Polygon.io Data Pipeline

## Project Overview
This is a financial data pipeline that downloads, processes, and visualizes OHLC (Open/High/Low/Close) market data from polygon.io. The system consists of data downloaders, aggregation scripts, and a web-based chart viewer.

## Architecture Components

### 1. Data Download Scripts (Project Root)
- **Core Pattern**: Each downloader is standalone - no script dependencies required
- **Key Files**: `download_bars.py`, `download_trades.py`, `download_tickers_history.py`
- **Storage**: All data stored in `../polygon-data/` (outside project for size/indexing reasons)
- **API Integration**: Uses `polygon-api-client` with API key from `api_key.txt`

### 2. Data Processing Pipeline
- **Raw Data**: 1-second bars stored as yearly parquet files per ticker: `bars/1second/{ticker}/{year}.parquet`
- **Aggregated Data**: 1-minute bars created by `aggregate_bars.py`: `bars/1minute/{ticker}.parquet`
- **Index Strategy**: Minute bars use timestamp as index; second bars use timestamp as column
- **Critical Detail**: The project uses PyArrow (`pyarrow.parquet`) for performance - pandas fallbacks were removed

### 3. Web Viewer (`viewer/`)
- **Backend**: FastAPI server (`backend/main.py`) serving OHLC data APIs
- **Frontend**: Svelte + lightweight-charts for interactive candlestick visualization
- **Data Flow**: Frontend requests N bars before/after timestamp (not time ranges) to handle weekend gaps

## Critical Developer Patterns

### Performance-Optimized Data Loading
```python
# currently the project uses PyArrow for parquet reading
table = pq.read_table(file_path, columns=['open', 'high', 'low', 'close'])
df = table.to_pandas()

# Consistent API: both data functions return pre-filtered DataFrame with 'time' column
def _get_minutes_df() -> pd.DataFrame:  # Returns with 'time' column
def _get_seconds_df() -> pd.DataFrame:  # Returns with 'time' column
```

### Timestamp-Based Navigation
```python
# Used searchsorted() for efficient timestamp filtering (not boolean indexing)
idx = df['timestamp'].searchsorted(to_timestamp, side='right')
df = df.iloc[max(0, idx - LIMIT):idx]
```

### Frontend Data Loading Strategy
```javascript
// Request N bars before timestamp (not time ranges) to handle market gaps
const params = new URLSearchParams();
if (timestamp) params.append('timestamp', timestamp);
params.append('direction', direction); // 'backward', 'forward', 'both'
```

## File Structure & Data Conventions

### Configuration
- **Settings**: `settings.py` - centralized config (data directory, date ranges)
- **API Keys**: `api_key.txt` (required), `api_key_id.txt` (optional for flat files)
- **Dependencies**: `requirements.txt` includes `polygon-api-client`, `pyarrow`, `fastapi`

### Data Storage Structure
```
../polygon-data/
├── bars/
│   ├── 1second/{ticker}/{year}.parquet  # Raw data by year
│   └── 1minute/{ticker}.parquet          # Aggregated with timestamp index
└── tickers/
    └── ticker_details.csv                # Market cap sorted ticker list
```

## Development Workflows

### Running the Viewer
```bash
# Backend
cd viewer/backend && python main.py

# Frontend  
cd viewer/frontend && npm run dev
```

### Data Download Workflow
```python
# Download bars for specific tickers (standalone operation)
python download_bars.py

# Aggregate to minute bars (creates indexed parquet)
from aggregate_bars import aggregate_bars
aggregate_bars('AAPL')
```

### Performance Debugging
- **LIMIT = 3000**: Controls bars per API response (configured in backend/main.py)
- **Memory Pattern**: The project processes data year-by-year to manage large datasets
- **Column Filtering**: The codebase typically specifies required columns in parquet reads

## Integration Points

### API Endpoints (`/api/bars/{ticker}`)
- **Parameters**: `from_timestamp`, `to_timestamp`, `resolution` (1second/1minute)
- **Response**: `{"ticker": str, "bars": [{"time": int, "open": float, ...}]}`
- **Error Handling**: Returns `{"error": str}` for missing data

### Chart Integration (Svelte Frontend)
- **Library**: `lightweight-charts` for OHLC visualization
- **Data Loading**: Dynamic loading on scroll with `barsInLogicalRange()` trigger
- **State Management**: `allBars` array maintains complete dataset client-side

## Project-Specific Conventions

1. **Symmetric Architecture**: Both `_get_minutes_df()` and `_get_seconds_df()` return identical column structure
2. **No Debug Logging**: Production code should not include timing/performance logs
3. **Timestamp Handling**: The frontend expects data in ascending order for compatibility
4. **Path Resolution**: Project modules are imported using `sys.path.append()` from subdirectories
5. **Error Boundaries**: Data loading functions return `None` for missing data, not exceptions
6. **CSS Styling**: Use CSS classes in `<style>` blocks, avoid inline styles except when containing variables or logic that cannot be extracted

## Frontend Development Standards

### Svelte Component Styling
```svelte
<!-- GOOD: Use CSS classes -->
<input class="multiplier-input" type="number" bind:value={multiplier} />

<style>
  .multiplier-input {
    width: 60px;
  }
</style>

<!-- BAD: Avoid inline styles -->
<input style="width: 60px;" type="number" bind:value={multiplier} />
```

### When Inline Styles Are Acceptable
- Dynamic values that change based on component state
- Calculated positions or dimensions
- Color values from variables that cannot be easily extracted to CSS
