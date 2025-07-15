<script lang="ts">
  import { onMount } from 'svelte';
  import { createChart, CandlestickSeries, CrosshairMode } from 'lightweight-charts';
  import { goto } from '$app/navigation';

  let tickers = []; // tickers for the dropdown
  let searchInput = ''; // input to search tickers
  let selectedTicker = ''; // currently selected ticker
  let chartContainer; // div to hold the chart
  let chart; // chart instance
  let candlestickSeries = null; // candlestick series for the chart
  let loading = false; // flag to show 'Loading...' status while fetching data
  let visibleRangeChanging = false; // flag to prevent multiple ajax handler executions on scrolling
  let error = null; // error message to display if something goes wrong
  let allBars = []; // array of chart candlestick bars
  let resolution = '1second';
  let noMoreBackward = false; // scrolling backward has reached the end
  let noMoreForward = false; // scrolling forward has reached the end

  onMount(() => {
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
        secondsVisible: false,
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
        const barsInfo = candlestickSeries.barsInLogicalRange(newVisibleLogicalRange);

        if (barsInfo !== null && barsInfo.barsBefore < 50) {
          const oldestBar = allBars[0];
          if (oldestBar) {
            const timestamp = oldestBar.time;
            await loadChartData(selectedTicker, timestamp, "backward");
          }
        } else if (barsInfo !== null && barsInfo.barsAfter < 50) {
          const newestBar = allBars[allBars.length - 1];
          if (newestBar) {
            // load data after the newest bar
            const timestamp = newestBar.time;
            await loadChartData(selectedTicker, timestamp, "forward");
          }
        }
      } catch (e) {
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
      if (entries.length > 0) {
        const { width, height } = entries[0].contentRect;
        chart.resize(width, height - 5);
      }
    });
    resizeObserver.observe(chartContainer);

    // Initialize app after chart is created
    init();

    // Cleanup observer on component destroy
    return () => resizeObserver.disconnect();
  });

  async function init() {
    await fetchTickers();
    if (tickers.length > 0) {
      const defaultTicker = tickers.includes('AAPL') ? 'AAPL' : tickers[0];
      selectedTicker = defaultTicker;
      searchInput = defaultTicker; // Set the input value
      await onTickerChange();
    }
  }

  function handleFocus(event) {
    event.target.select();
  }

  async function fetchTickers(searchTerm = '') {
    let url = '/api/tickers';
    if (searchTerm) {
      url += `?search=${searchTerm}`;
    }
    const res = await fetch(url);
    const data = await res.json();
    tickers = data.tickers || [];
  }

  async function loadChartData(ticker, timestamp = null, direction = "backward") {
    if (!ticker || !chart) return;
    if (noMoreBackward && direction === "backward") return;
    if (noMoreForward && direction === "forward") return;
    loading = true;
    error = null;
    try {
      let url = `/api/bars/${ticker}`;
      const params = new URLSearchParams();
      if (timestamp) {
        params.append('timestamp', timestamp);
      }
      params.append('direction', direction);
      
      // Map resolution to period and multiplier for backend
      const resolutionMap = {
        '1second': { period: 'second', multiplier: 1 },
        '5second': { period: 'second', multiplier: 5 },
        '10second': { period: 'second', multiplier: 10 },
        '15second': { period: 'second', multiplier: 15 },
        '30second': { period: 'second', multiplier: 30 },
        '1minute': { period: 'minute', multiplier: 1 },
        '5minute': { period: 'minute', multiplier: 5 },
        '15minute': { period: 'minute', multiplier: 15 },
        '30minute': { period: 'minute', multiplier: 30 },
        '60minute': { period: 'hour', multiplier: 1 },
        '240minute': { period: 'hour', multiplier: 4 },
        '720minute': { period: 'hour', multiplier: 12 },
        '1440minute': { period: 'day', multiplier: 1 },
        '10080minute': { period: 'week', multiplier: 1 }
      };
      
      const config = resolutionMap[resolution] || { period: 'second', multiplier: 1 };
      params.append('period', config.period);
      params.append('multiplier', config.multiplier.toString());
      
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
        candlestickSeries.setData(allBars);
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
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  async function onTickerChange() {
    // Try to get current visible time range before clearing data
    let centerTimestamp = null;
    try {
      const visibleLogicalRange = chart.timeScale().getVisibleRange();
      if (visibleLogicalRange) {
        centerTimestamp = Math.floor(visibleLogicalRange.from + (visibleLogicalRange.to - visibleLogicalRange.from) / 2);
      }
    } catch (e) {
      console.warn('Could not get visible range:', e);
    }
    
    allBars = [];
    
    // Load data around the center timestamp, or latest if no center found
    await loadChartData(selectedTicker, centerTimestamp, "both");
    
    // After loading data, center the chart on the timestamp if we have it
    if (centerTimestamp && allBars.length > 0) {
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
        
        // Calculate window: ±500 bars from center
        const startIndex = Math.max(0, centerIndex - 500);
        const endIndex = Math.min(allBars.length - 1, centerIndex + 500);
        
        const fromTime = allBars[startIndex].time;
        const toTime = allBars[endIndex].time;
        
        chart.timeScale().setVisibleRange({
          from: fromTime,
          to: toTime
        });
      } catch (e) {
        console.warn('Could not set visible range:', e);
      }
    }
  }

  let debounceTimer;
  function handleInput(event) {
    clearTimeout(debounceTimer);
    const searchTerm = event.target.value;
    searchInput = searchTerm.toUpperCase(); // Update searchInput directly
    debounceTimer = setTimeout(() => {
      fetchTickers(searchTerm);
    }, 300); // 300ms debounce
  }

  function handleBlur() {
    if (searchInput !== selectedTicker) {
      searchInput = selectedTicker;
    }
  }

  function openDownloadPage() {
    if (selectedTicker) {
      goto(`/download?ticker=${selectedTicker}`);
    }
  }

  // Reactive statement to handle ticker selection immediately
  $: {
    if (tickers.includes(searchInput) && searchInput !== selectedTicker) {
      selectedTicker = searchInput;
      onTickerChange();
    }
  }
</script>

<svelte:head>
  <title>Polygon Data Viewer</title>
</svelte:head>

<main>
  <div class="header">
    <div class="left-controls">
      <input
        type="text"
        id="ticker-input"
        list="ticker-list"
        bind:value={searchInput}
        on:input={handleInput}
        on:focus={handleFocus}
        on:blur={handleBlur}
        placeholder="e.g. AAPL"
      />
      <select bind:value={resolution} on:change={onTickerChange}>
        <option value="1second">1 Second</option>
        <option value="5second">5 Seconds</option>
        <option value="10second">10 Seconds</option>
        <option value="15second">15 Seconds</option>
        <option value="30second">30 Seconds</option>
        <option value="1minute">1 Minute</option>
        <option value="5minute">5 Minutes</option>
        <option value="15minute">15 Minutes</option>
        <option value="30minute">30 Minutes</option>
        <option value="60minute">1 Hour</option>
        <option value="240minute">4 Hours</option>
        <option value="720minute">12 Hours</option>
        <option value="1440minute">1 Day</option>
        <option value="10080minute">1 Week</option>
      </select>
      {#if loading}
        <div class="status-indicator">Loading...</div>
      {:else if error}
        <div class="status-indicator error">{error}</div>
      {/if}
    </div>
    <div class="right-controls">
      <button on:click={openDownloadPage} class="download-button">Download</button>
    </div>
    <datalist id="ticker-list">
      {#each tickers as ticker}
        <option value={ticker}>{ticker}</option>
      {/each}
    </datalist>
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
