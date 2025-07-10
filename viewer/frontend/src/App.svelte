<script>
  import { onMount } from 'svelte';
  import { createChart, CandlestickSeries } from 'lightweight-charts';

  let tickers = [];
  let selectedTicker = '';
  let chartContainer;
  let chart;
  let candlestickSeries = null;
  let loading = false;
  let allBars = [];

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
          const to = oldestBar.time - 1;
          const from = to - 86400;
          await loadChartData(selectedTicker, from, to, false);
        }
        loading = false;
      }
    });

    await fetchTickers();
    if (tickers.length > 0) {
      const defaultTicker = tickers.includes('AAPL') ? 'AAPL' : tickers[0];
      selectedTicker = defaultTicker;
      searchInput = defaultTicker; // Set the input value
      await onTickerChange();
    }
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

  async function loadChartData(ticker, from, to, reset) {
    if (!ticker || !chart) return;

    let url = `/api/bars/${ticker}`;
    const params = new URLSearchParams();
    if (from) params.append('from_timestamp', from);
    if (to) params.append('to_timestamp', to);
    if (params.toString()) {
      url += `?${params.toString()}`;
    }

    const res = await fetch(url);
    const data = await res.json();

    if (data.bars && data.bars.length > 0) {
      if (reset) {
        allBars = data.bars;
      } else {
        allBars = [...data.bars, ...allBars];
      }
      candlestickSeries.setData(allBars);
    }
  }

  async function onTickerChange() {
    allBars = [];
    await loadChartData(selectedTicker, null, null, true);
  }

  let debounceTimer;
  function handleInput(event) {
    clearTimeout(debounceTimer);
    const searchTerm = event.target.value;
    selectedTicker = searchTerm.toUpperCase();
    debounceTimer = setTimeout(() => {
      fetchTickers(searchTerm);
    }, 300); // 300ms debounce
  }

  function handleSelect(event) {
    const ticker = event.target.value;
    if (tickers.includes(ticker)) {
        selectedTicker = ticker;
        onTickerChange();
    }
  }

  function handleBlur() {
    if (searchInput !== selectedTicker) {
      searchInput = selectedTicker;
    }
  }

</script>

<main>
  <h1>Polygon.io Data Viewer</h1>

  <div>
    <label for="ticker-input">Choose a ticker:</label>
    <input
      type="text"
      id="ticker-input"
      list="ticker-list"
      bind:value={searchInput}
      on:input={handleInput}
      on:change={handleSelect}
      on:focus={handleFocus}
      on:blur={handleBlur}
      placeholder="e.g. AAPL"
    />
    <datalist id="ticker-list">
      {#each tickers as ticker}
        <option value={ticker}>{ticker}</option>
      {/each}
    </datalist>
  </div>

  <div bind:this={chartContainer}></div>
</main>

<style>
  main {
    font-family: sans-serif;
    text-align: center;
  }
</style>
