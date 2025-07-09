<script>
  import { onMount } from 'svelte';
  import { createChart, CandlestickSeries } from 'lightweight-charts';

  let tickers = [];
  let selectedTicker = ''
  let chartContainer;
  let chart;
  let candlestickSeries = null;

  onMount(async () => {
    // Create the chart
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
      },
    });

    // Fetch the list of tickers
    const res = await fetch('/api/tickers');
    const data = await res.json();
    tickers = data.tickers;
    if (tickers.length > 0) {
        selectedTicker = tickers[0];
        loadChartData(selectedTicker);
    }
  });

  async function loadChartData(ticker) {
    if (!ticker || !chart) return;

    // Remove the old series if it exists
    if (candlestickSeries) {
      chart.removeSeries(candlestickSeries);
    }

    const res = await fetch(`/api/bars/${ticker}`);
    const data = await res.json();

    if (data.bars && data.bars.length > 0) {
        candlestickSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#26a69a',
            downColor: '#ef5350',
            borderDownColor: '#ef5350',
            borderUpColor: '#26a69a',
            wickDownColor: '#ef5350',
            wickUpColor: '#26a69a',
            priceFormat: {
                type: 'price',
                precision: 6,
                minMove: 0.000001,
            },
        });
        candlestickSeries.setData(data.bars);
    }
  }

  function onTickerChange(event) {
    selectedTicker = event.target.value;
    loadChartData(selectedTicker);
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
