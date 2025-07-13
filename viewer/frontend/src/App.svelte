<script>
  import { onMount } from 'svelte';
  import { createChart, CandlestickSeries } from 'lightweight-charts';

  let tickers = [];
  let selectedTicker = '';
  let chartContainer;
  let chart;
  let candlestickSeries = null;
  let loading = false;
  let error = null;
  let allBars = [];
  let resolution = '1second';

  let searchInput = '';

  onMount(async () => {
    chart = createChart(chartContainer, {
      width: 800,
      height: 600,
      layout: {
        backgroundColor: '#ffffff',
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
        mode: 'normal',
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
      if (loading || allBars.length === 0) return;

      const barsInfo = candlestickSeries.barsInLogicalRange(newVisibleLogicalRange);

      if (barsInfo !== null && barsInfo.barsBefore < 50) {
        loading = true;
        const oldestBar = allBars[0];
        if (oldestBar) {
          // Передаем точный timestamp самого старого бара для оптимизации
          const timestamp = oldestBar.time;
          await loadChartData(selectedTicker, timestamp, "backward");
        }
        loading = false;
      }
    });

    await fetchTickers();
    if (tickers.length > 0) {
      const defaultTicker = tickers.includes('AAPL') ? 'AAPL' : tickers[0];
      selectedTicker = defaultTicker;
      searchInput = defaultTicker; // Set the input value
      await onTickerChange(true); // Initial load, direction 'both'
    }

    // Resize chart when container changes size
    const resizeObserver = new ResizeObserver(entries => {
      if (entries.length > 0) {
        const { width, height } = entries[0].contentRect;
        chart.resize(width, height - 5);
      }
    });
    resizeObserver.observe(chartContainer);

    // Cleanup observer on component destroy
    return () => resizeObserver.disconnect();
  });

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
    loading = true;
    error = null;
    try {
      let url = `/api/bars/${ticker}`;
      const params = new URLSearchParams();
      if (timestamp) {
        params.append('timestamp', timestamp);
      }
      params.append('direction', direction); // Add direction parameter
      params.append('resolution', resolution);
      if (params.toString()) {
        url += `?${params.toString()}`;
      }

      const res = await fetch(url);
      const data = await res.json();

      if (data.error) {
        throw new Error(data.error);
      }

      if (data.bars && data.bars.length > 0) {
        if (direction === "backward") {
          allBars = [...data.bars, ...allBars];
        } else if (direction === "forward") {
          allBars = [...allBars, ...data.bars];
        } else if (direction === "both") {
          // For "both" or initial load, replace allBars
          allBars = data.bars;
        }
        candlestickSeries.setData(allBars);
      }
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  async function onTickerChange(initialLoad = false) {
    allBars = [];
    if (initialLoad) {
      await loadChartData(selectedTicker, null, "both");
    } else {
      await loadChartData(selectedTicker, null, "backward");
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
      window.open(`/download.html?ticker=${selectedTicker}`, '_blank');
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
        <option value="1minute">1 Minute</option>
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

  .right-controls {
    /* No specific styles needed for now */
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
