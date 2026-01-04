<script lang="ts">
  import { onMount } from 'svelte';
  import { createChart, CandlestickSeries, CrosshairMode, type IChartApi, type ISeriesApi } from 'lightweight-charts';
  import { goto } from '$app/navigation';
  import TickerSearch from '$lib/TickerSearch.svelte';

  let selectedTicker = $state('');
  let chartContainer = $state<HTMLDivElement>();
  let chart = $state<IChartApi>();
  let candlestickSeries = $state<ISeriesApi<'Candlestick'> | null>(null);
  let loading = $state(false);
  let visibleRangeChanging = $state(false);
  let error = $state<string | null>(null);
  let allBars = $state<any[]>([]);
  let interval = $state('10s');

  // Update secondsVisible on chart when interval changes
  function updateSecondsVisible() {
    if (!chart) return;
    // Show seconds on the time axis for second-based intervals
    const secondIntervals = ['1s', '5s', '10s', '15s', '30s'];
    const showSeconds = secondIntervals.includes(interval);
    chart.timeScale().applyOptions({ secondsVisible: showSeconds });
  }

  // Svelte reactive block: update secondsVisible when interval changes
  $effect(updateSecondsVisible);
  let noMoreBackward = $state(false);
  let noMoreForward = $state(false);
  let filterOutliers = $state(true);

  onMount(() => {
    if (!chartContainer) return;
    
    chart = createChart(chartContainer, {
      width: 800,
      height: 600,
      layout: {
        textColor: 'rgba(33, 56, 77, 1)',
      },
      grid: {
        vertLines: {
          color: 'rgba(197, 203, 206, 0.5)',
        },
        horzLines: {
          color: 'rgba(197, 203, 206, 0.5)',
        },
      },
      crosshair: {
        mode: CrosshairMode.Normal,
      },
      rightPriceScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
      },
      timeScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
        timeVisible: true,
        secondsVisible: false, // initial value, will be updated reactively
      },
    });

    candlestickSeries = chart.addSeries(CandlestickSeries, {
      upColor: '#26a69a',
      downColor: '#ef5350',
      borderDownColor: '#ef5350',
      borderUpColor: '#26a69a',
      wickDownColor: '#ef5350',
      wickUpColor: '#26a69a',
    });

    chart.timeScale().subscribeVisibleLogicalRangeChange(async (newVisibleLogicalRange) => {
      // if another handler is already processing then don't start a new one
      if (visibleRangeChanging) return;
      visibleRangeChanging = true;
      // try/finally to restore the flag
      try {
        const barsInfo = newVisibleLogicalRange ? candlestickSeries?.barsInLogicalRange(newVisibleLogicalRange) : null;
        if (barsInfo && barsInfo.barsBefore < 50) {
          const oldestBar = allBars[0];
          if (oldestBar) {
            const timestamp = oldestBar.time;
            await loadChartData(selectedTicker, timestamp, "backward");
          }
        } else if (barsInfo && barsInfo.barsAfter < 50) {
          const newestBar = allBars[allBars.length - 1];
          if (newestBar) {
            // load data after the newest bar
            const timestamp = newestBar.time;
            await loadChartData(selectedTicker, timestamp, "forward");
          }
        }
      } catch (e: any) {
        console.error('Error during visible range change:', e);
        error = e.message || 'An error occurred while updating the visible range.';
      } finally {
        // dirty hack is needed because after setData the visible range gets updated not immediately. don't know why.
        // without timeout it loads data twice while scrolling.
        setTimeout(() => {
          visibleRangeChanging = false;
        }, 50); // Reset the flag after a short delay
      }
    });

    // Resize chart when container changes size
    const resizeObserver = new ResizeObserver(entries => {
      if (entries.length > 0 && chart) {
        const { width, height } = entries[0].contentRect;
        chart.resize(width, height - 5);
      }
    });
    if (chartContainer) {
      resizeObserver.observe(chartContainer);
    }

    // Initialize app after chart is created
    init();

    // Cleanup observer on component destroy
    return () => resizeObserver.disconnect();
  });

  async function init() {
    // Set default ticker
    const defaultTicker = 'AAPL';
    selectedTicker = defaultTicker;
    await onTickerChange();
  }

  async function loadChartData(ticker: string, timestamp: number | null = null, direction = "backward") {
    if (!ticker || !chart) return;
    if (noMoreBackward && direction === "backward") return;
    if (noMoreForward && direction === "forward") return;
    loading = true;
    error = null;
    try {
      let url = `/api/bars/${ticker}`;
      const params = new URLSearchParams();
      if (timestamp) {
        params.append('timestamp', timestamp.toString());
      }
      params.append('direction', direction);
      
      // Use interval directly in API call
      params.append('interval', interval);
      
      // Add filter_outliers parameter
      params.append('filter_outliers', filterOutliers.toString());
      
      if (params.toString()) {
        url += `?${params.toString()}`;
      }

      const res = await fetch(url);
      const data = await res.json();

      if (data.error) {
        error = data.error;
      }

      if (data.bars && data.bars.length > 0) {
        if (direction === "backward") {
          allBars = [...data.bars, ...allBars];
        } else if (direction === "forward") {
          allBars = [...allBars, ...data.bars];
        } else if (direction === "both") {
          // For "both" or initial load, replace allBars
          allBars = data.bars;
          // "both" is requested only on ticker change
          noMoreBackward = false;
          noMoreForward = false;
        }
        const ts = chart.timeScale();
        const oldRange = ts.getVisibleRange();
        candlestickSeries?.setData(allBars);
        if (oldRange) {
            ts.setVisibleRange({
                from: oldRange.from,
                to:   oldRange.to,
            });
        }
      } else {
        // if there is no data from the backend then set the flags to not request it again
        if (direction === "backward") {
          noMoreBackward = true;
        } else if (direction === "forward") {
          noMoreForward = true;
        } else {
          noMoreBackward = true;
          noMoreForward = true;
        }
      }
    } catch (e: any) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  async function onTickerChange() {
    if (!chart) return;
    
    // Try to get current visible time range before clearing data
    let centerTimestamp = null;
    let visibleBars = 0;
    try {
      const visibleRange = chart.timeScale().getVisibleRange();
      if (visibleRange) {
        centerTimestamp = Math.floor((visibleRange.from as number) + ((visibleRange.to as number) - (visibleRange.from as number)) / 2);
      }
      const visibleLogicalRange = chart.timeScale().getVisibleLogicalRange();
      if (visibleLogicalRange) {
        visibleBars = visibleLogicalRange.to - visibleLogicalRange.from;
      }
    } catch (e) {
      console.warn('Could not get visible range:', e);
    }
    
    allBars = [];
    
    // Load data around the center timestamp, or latest if no center found
    await loadChartData(selectedTicker, centerTimestamp, "both");
    
    if (allBars.length === 0) {
      return;
    }
    const visibleBarsHalf = visibleBars ? Math.floor(visibleBars / 2) : 500;
    // After loading data, center the chart on the timestamp if we have it
    if (centerTimestamp) {
      try {
        // Find the position of centerTimestamp in allBars
        let centerIndex = -1;
        for (let i = 0; i < allBars.length; i++) {
          if (allBars[i].time >= centerTimestamp) {
            centerIndex = i;
            break;
          }
        }
        
        // If exact timestamp not found, use the closest one
        if (centerIndex === -1) {
          centerIndex = allBars.length - 1;
        }
        const startIndex = Math.max(0, centerIndex - visibleBarsHalf);
        const endIndex = Math.min(allBars.length - 1, centerIndex + visibleBarsHalf);
        
        const fromTime = allBars[startIndex].time;
        const toTime = allBars[endIndex].time;
        
        if (chart) {
          chart.timeScale().setVisibleRange({
            from: fromTime,
            to: toTime
          });
        }
      } catch (e) {
        console.warn('Could not set visible range:', e);
      }
    }
    else {
      // on first page load show last 1000 bars and add space on the right for 50 future bars
      try {
        const totalBars = allBars.length;
        const barsToShow = Math.min(1000, totalBars);
        const startIndex = Math.max(0, totalBars - barsToShow);
        
        if (totalBars > 0 && chart) {
          const fromTime = allBars[startIndex].time;
          const toTime = allBars[totalBars - 1].time;
          
          chart.timeScale().setVisibleRange({
            from: fromTime,
            to: toTime
          });
          
          // Use scrollToPosition to position the chart with some space on the right
          setTimeout(() => {
            // Scroll to a position that leaves some space on the right
            // Negative values scroll towards the end (more recent data)
            chart?.timeScale().scrollToPosition(50, false);
          }, 100);
        }
      } catch (e) {
        console.warn('Could not set initial visible range:', e);
      }
    }
  }

  function handleTickerChange(newTicker: string) {
    selectedTicker = newTicker;
    onTickerChange();
  }

  function openDownloadPage() {
    if (selectedTicker) {
      goto(`/download?ticker=${selectedTicker}&interval=${interval}`);
    }
  }
</script>

<svelte:head>
  <title>Polygon Data Viewer</title>
</svelte:head>

<main>
  <div class="header">
    <div class="left-controls">
      <TickerSearch value={selectedTicker} onchange={handleTickerChange} />
      <select bind:value={interval} onchange={onTickerChange}>
        <option value="1s">1 Second</option>
        <option value="5s">5 Seconds</option>
        <option value="10s">10 Seconds</option>
        <option value="15s">15 Seconds</option>
        <option value="30s">30 Seconds</option>
        <option value="1min">1 Minute</option>
        <option value="5min">5 Minutes</option>
        <option value="15min">15 Minutes</option>
        <option value="30min">30 Minutes</option>
        <option value="1h">1 Hour</option>
        <option value="4h">4 Hours</option>
        <option value="12h">12 Hours</option>
        <option value="1d">1 Day</option>
        <option value="1w">1 Week</option>
      </select>
      <label class="checkbox-label">
        <input type="checkbox" bind:checked={filterOutliers} onchange={onTickerChange} />
        Filter outliers
      </label>
      {#if loading}
        <div class="status-indicator">Loading...</div>
      {:else if error}
        <div class="status-indicator error">{error}</div>
      {/if}
    </div>
    <div class="right-controls">
      <button onclick={openDownloadPage} class="download-button">Download</button>
    </div>
  </div>

  <div bind:this={chartContainer} class="chart-container"></div>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    font-family: sans-serif;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }

  .left-controls {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 14px;
    cursor: pointer;
    user-select: none;
  }

  .checkbox-label input[type="checkbox"] {
    cursor: pointer;
  }

  .status-indicator {
    font-style: italic;
  }

  .error {
    color: red;
  }

  .chart-container {
    flex-grow: 1;
    width: 100%;
  }
</style>
