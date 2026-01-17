
<script lang="ts">
  import { onMount } from 'svelte';
  import CanvasChart from './lib/CanvasChart.svelte';
  import { fetchTickers, fetchViewportData, fetchTickerMeta, type Bar } from './lib/api';

  let tickers: string[] = [];
  let selectedTicker = "AAPL";
  let bars: Bar[] = [];
  
  // Default range: Last 24 hours (will be updated dynamically)
  let endTime = Date.now() / 1000;
  let startTime = endTime - 24 * 60 * 60;
  
  let isLoading = false;
  let error = "";
  
  // Debounce and Throttle logic
  let debounceTimer: ReturnType<typeof setTimeout>;
  let lastLoadTime = 0;
  const LOAD_THROTTLE = 200; // Minimum ms between loads during interaction
  
  let abortController: AbortController | null = null;
  
  onMount(async () => {
      try {
          tickers = await fetchTickers();
          
          // Check URL params
          const params = new URLSearchParams(window.location.search);
          const urlTicker = params.get('ticker');
          const urlFrom = params.get('from');
          const urlTo = params.get('to');
          
          if (urlTicker && tickers.includes(urlTicker)) {
              selectedTicker = urlTicker;
              if (urlFrom && urlTo) {
                   const f = parseFloat(urlFrom);
                   const t = parseFloat(urlTo);
                   if (!isNaN(f) && !isNaN(t) && t > f) {
                       startTime = f;
                       endTime = t;
                       await loadData();
                       return;
                   }
              }
              // If ticker present but no time, reset to latest
              await resetToLatest();
          } else {
             // Default behavior: try AAPL first, otherwise take the first in list
             if (tickers.length > 0) {
                 if (tickers.includes("AAPL")) {
                     selectedTicker = "AAPL";
                 } else {
                     selectedTicker = tickers[0];
                 }
             }
             await resetToLatest();
          }
      } catch (e) {
          error = "Failed to load tickers";
      }
  });

  function updateUrl() {
      const params = new URLSearchParams();
      params.set('ticker', selectedTicker);
      params.set('from', startTime.toFixed(0));
      params.set('to', endTime.toFixed(0));
      const newUrl = `${window.location.pathname}?${params.toString()}`;
      history.replaceState(null, '', newUrl);
  }

  async function resetToLatest() {
     isLoading = true;
     try {
         const meta = await fetchTickerMeta(selectedTicker);
         if (meta.last_timestamp) {
             endTime = meta.last_timestamp;
             startTime = endTime - 24 * 60 * 60; // 24h window
             await loadData();
         } else {
             error = "No data available for this ticker";
             bars = [];
             updateUrl();
         }
     } catch(e) {
         error = "Failed to load ticker metadata";
     } finally {
         isLoading = false;
     }
  }

  function handleViewportChange(newStart: number, newEnd: number) {
      startTime = newStart;
      endTime = newEnd;
      updateUrl();
      
      const now = Date.now();
      
      // Clear trailing debounce
      clearTimeout(debounceTimer);
      
      // Throttle check
      if (now - lastLoadTime > LOAD_THROTTLE) {
          // Fire immediately
          loadData();
      } else {
          // Schedule trailing
          debounceTimer = setTimeout(loadData, 300);
      }
  }
  
  async function loadData() {
      if (!selectedTicker) return;
      
      // Cancel previous request
      if (abortController) {
          abortController.abort();
      }
      abortController = new AbortController();
      const signal = abortController.signal;
      
      lastLoadTime = Date.now();
      isLoading = true;
      
      try {
          const width = window.innerWidth;
          const data = await fetchViewportData(selectedTicker, startTime, endTime, width, signal);
          bars = data;
          error = "";
      } catch (e: any) {
          if (e.name === 'AbortError') {
              // Ignore aborted requests
          } else {
              console.error(e);
          }
      } finally {
          // Only unset loading if this was the active controller (simple check)
          if (!signal.aborted) {
             isLoading = false;
          }
      }
  }
  
  function onTickerChange() {
      // When changing ticker, we should probably reset to its latest data
      resetToLatest();
  }
</script>

<main>
    <div class="toolbar">
        <select bind:value={selectedTicker} on:change={onTickerChange}>
            {#each tickers as ticker}
                <option value={ticker}>{ticker}</option>
            {/each}
        </select>
        
        <div class="info">
            <span>Frame: {(endTime - startTime).toFixed(0)}s</span>
            {#if isLoading} <span class="loading">Loading...</span> {/if}
            {#if error} <span class="error">{error}</span> {/if}
        </div>
    </div>
    
    <div class="chart-wrapper">
        <CanvasChart {bars} {startTime} {endTime} onViewportChange={handleViewportChange} />
    </div>
</main>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
        background: #1e1e1e;
        color: #ddd;
        font-family: sans-serif;
        overflow: hidden; /* No scrollbars on body */
        width: 100%;
        height: 100%;
    }
    :global(*) {
        box-sizing: border-box;
    }
    main {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100%; /* Fix: 100vw can cause overflow with scrollbars */
    }
    .toolbar {
        padding: 10px;
        background: #252526;
        border-bottom: 1px solid #333;
        display: flex;
        gap: 20px;
        align-items: center;
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        flex-shrink: 0; /* Prevent shrinking */
    }
    .chart-wrapper {
        flex-grow: 1;
        position: relative;
        min-height: 0; /* Fix: flex child overflow issue */
        width: 100%;
    }
    select {
        background: #333;
        color: white;
        border: 1px solid #555;
        padding: 5px;
        font-size: 14px;
    }
    .loading {
        color: #eca529;
        font-size: 0.8em;
    }
    .error {
        color: #ff5555;
    }
</style>
