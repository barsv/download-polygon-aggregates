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

      // if the user scrolls to the beginning of the chart, load more data
      if (barsInfo !== null && barsInfo.barsBefore < 50) {
        loading = true;
        const oldestBar = allBars[0];
        if (oldestBar) {
          const to = oldestBar.time - 1; // a second before the oldest bar
          const from = to - 86400; // load 1 day before
          await loadChartData(selectedTicker, from, to, false);
        }
        loading = false;
      }
    });

    const res = await fetch('/api/tickers');
    const data = await res.json();
    tickers = data.tickers;
    if (tickers.length > 0) {
      selectedTicker = tickers[0];
      await onTickerChange();
    }
  });

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

</script>

<main>
  <h1>Polygon.io Data Viewer</h1>

  <div>
    <label for="ticker-select">Choose a ticker:</label>
    <select id="ticker-select" bind:value={selectedTicker} on:change={onTickerChange}>
      {#each tickers as ticker}
        <option value={ticker}>{ticker}</option>
      {/each}
    </select>
  </div>

  <div bind:this={chartContainer}></div>
</main>

<style>
  main {
    font-family: sans-serif;
    text-align: center;
  }
</style>
