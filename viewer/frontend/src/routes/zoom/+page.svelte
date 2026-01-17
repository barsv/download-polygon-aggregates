
<script lang="ts">
  import { onMount } from 'svelte';
  import CanvasChart from '$lib/zoom/CanvasChart.svelte';
  import { fetchViewportData, fetchTickerMeta, type Bar } from '$lib/zoom/api';
  import TickerSearch from '$lib/TickerSearch.svelte';

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
           // Check URL params
           const params = new URLSearchParams(window.location.search);
           const urlTicker = params.get('ticker');
           const urlFrom = params.get('from');
           const urlTo = params.get('to');
           
           if (urlTicker) {
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
              // Default behavior: AAPL
              selectedTicker = "AAPL";
              await resetToLatest();
           }
       } catch (e) {
           error = "Failed to initialize";
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
  
   function onTickerChange(newTicker: string) {
       selectedTicker = newTicker;
       resetToLatest();
   }
</script>

<svelte:head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <title>Infinite Zoom | {selectedTicker}</title>
</svelte:head>

<main>
    <div class="toolbar">
        <div class="toolbar-content">
            <div class="left-controls">
                <div class="logo">
                     <span class="logo-text">INFINITE</span>
                     <span class="logo-sub">ZOOM</span>
                </div>
                <TickerSearch value={selectedTicker} onchange={onTickerChange} />
                
                <div class="info">
                    <span class="pill">{(endTime - startTime).toFixed(0)}s</span>
                    {#if isLoading} <span class="loading-indicator"></span> {/if}
                    {#if error} <span class="error">{error}</span> {/if}
                </div>
            </div>

            <div class="right-controls">
                <a href="/?ticker={selectedTicker}" class="nav-link">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                    Standard View
                </a>
            </div>
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
        background: #0f0f12;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
        overflow: hidden;
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
        width: 100%;
    }
    .toolbar {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: calc(100% - 40px);
        max-width: 1200px;
        z-index: 100;
        pointer-events: none;
    }
    .toolbar-content {
        background: rgba(30, 30, 35, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 8px 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        pointer-events: auto;
    }
    .left-controls {
        display: flex;
        align-items: center;
        gap: 24px;
    }
    .logo {
        display: flex;
        flex-direction: column;
        line-height: 1;
        margin-right: 10px;
    }
    .logo-text {
        font-weight: 800;
        font-size: 14px;
        letter-spacing: 1px;
        color: #4a90e2;
    }
    .logo-sub {
        font-size: 10px;
        font-weight: 400;
        color: #888;
        letter-spacing: 2.5px;
    }
    .right-controls {
        display: flex;
        align-items: center;
    }
    .nav-link {
        text-decoration: none;
        color: #fff;
        font-weight: 500;
        font-size: 13px;
        padding: 8px 16px;
        border-radius: 8px;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .nav-link:hover {
        background: rgba(74, 144, 226, 0.15);
        border-color: rgba(74, 144, 226, 0.3);
        transform: translateY(-1px);
    }
    .chart-wrapper {
        flex-grow: 1;
        position: relative;
        min-height: 0;
        width: 100%;
    }
    .info {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .pill {
        background: rgba(255, 255, 255, 0.05);
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        color: #aaa;
        font-variant-numeric: tabular-nums;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .loading-indicator {
        width: 14px;
        height: 14px;
        border: 2px solid rgba(74, 144, 226, 0.3);
        border-top-color: #4a90e2;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    .error {
        color: #ff5555;
        font-size: 12px;
    }
</style>
