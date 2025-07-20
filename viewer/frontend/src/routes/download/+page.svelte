<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import TickerSearch from '$lib/TickerSearch.svelte';
  
  let files = $state<string[]>([]);
  let loading = $state(true);
  let error = $state<string | null>(null);
  let ticker = $state('');
  let selectedFormat = $state('parquet');
  let timeFormat = $state('timestamp');
  let customTimeFormat = $state('yyyy-MM-dd HH:mm:ss');
  let selectedInterval = $state('1s');

  onMount(async () => {
    // Get ticker from URL params
    ticker = $page.url.searchParams.get('ticker') || '';
    
    // Get interval from URL params (passed from main chart page)
    const urlInterval = $page.url.searchParams.get('interval');
    if (urlInterval) {
      selectedInterval = urlInterval;
    }

    if (!ticker) {
      error = 'No ticker specified.';
      loading = false;
      return;
    }

    await loadFiles();
  });

  async function loadFiles() {
    if (!ticker) return;
    
    loading = true;
    error = null;
    
    try {
      const params = new URLSearchParams();
      if (selectedInterval !== '1s') {
        params.append('interval', selectedInterval);
      }
      
      let url = `/api/download/files/${ticker}`;
      if (params.toString()) {
        url += `?${params.toString()}`;
      }
      
      const response = await fetch(url);
      const data = await response.json();

      if (data.error) {
        error = data.error;
        return;
      }

      files = data.files || [];
    } catch (e) {
      error = `Failed to load files: ${e instanceof Error ? e.message : 'Unknown error'}`;
    } finally {
      loading = false;
    }
  }

  function handleTickerChange(newTicker: string) {
    ticker = newTicker;
    loadFiles();
  }

  function handleIntervalChange() {
    loadFiles();
  }

  function downloadFile(filename: string) {
    let url = `/api/download/file/${ticker}/${filename}?format=${selectedFormat}`;
    
    // Add interval parameter if not default
    if (selectedInterval !== '1s') {
      url += `&interval=${selectedInterval}`;
    }
    
    // Add time format parameters for CSV
    if (selectedFormat === 'csv' && timeFormat !== 'timestamp') {
      const formatToUse = timeFormat === 'custom' ? customTimeFormat : timeFormat;
      url += `&time_format=${encodeURIComponent(formatToUse)}`;
    }
    
    window.open(url, '_blank');
  }
</script>

<svelte:head>
  <title>Download Files{ticker ? ` for ${ticker}` : ''}</title>
</svelte:head>

<main class="container">
  <h1>Download Files {ticker ? ` for ${ticker}` : ''}</h1>
  
  <div class="controls">
    <!-- Ticker selection -->
    <div class="ticker-section">
      <label for="ticker-input">Ticker:</label>
      <TickerSearch value={ticker} onchange={handleTickerChange} />
    </div>
    
    <!-- Format selection -->
    <div class="format-section">
      <label for="format-select">File Format:</label>
      <select id="format-select" bind:value={selectedFormat}>
        <option value="parquet">Parquet</option>
        <option value="csv">CSV</option>
      </select>
    </div>
    
    <!-- Interval selection -->
    <div class="interval-section">
      <label for="interval">Interval:</label>
      <select id="interval" bind:value={selectedInterval} onchange={handleIntervalChange}>
        <option value="1s">1 second</option>
        <option value="5s">5 seconds</option>
        <option value="10s">10 seconds</option>
        <option value="30s">30 seconds</option>
        <option value="1min">1 minute</option>
        <option value="5min">5 minutes</option>
        <option value="15min">15 minutes</option>
        <option value="30min">30 minutes</option>
        <option value="1h">1 hour</option>
        <option value="4h">4 hours</option>
        <option value="1d">1 day</option>
      </select>
    </div>
    
    <!-- Time format options for CSV only -->
    {#if selectedFormat === 'csv'}
      <div class="time-format-section">
        <div class="time-format-input">
          <label for="time-format">Time Format:</label>
          <select bind:value={timeFormat}>
            <option value="timestamp">Timestamp (seconds)</option>
            <option value="yyyy-MM-dd HH:mm:ss">2024-01-15 14:30:25</option>
            <option value="yyyy-MM-dd HH:mm:ss.fff">2024-01-15 14:30:25.123</option>
            <option value="yyyy-MM-dd'T'HH:mm:ss">2024-01-15T14:30:25</option>
            <option value="yyyy-MM-dd'T'HH:mm:ss.fff'Z'">2024-01-15T14:30:25.123Z</option>
            <option value="yyyy-MM-dd">2024-01-15</option>
            <option value="MM/dd/yyyy HH:mm:ss">01/15/2024 14:30:25</option>
            <option value="custom">Custom format...</option>
          </select>
          {#if timeFormat === 'custom'}
            <input 
              type="text" 
              bind:value={customTimeFormat}
              placeholder="e.g. yyyy-MM-dd HH:mm:ss"
              class="custom-format-input"
            />
          {/if}
        </div>
      </div>
    {/if}
  </div>
  
  <div class="file-list-container">
    {#if loading}
      <p>Loading files...</p>
    {:else if error}
      <p class="error">Error: {error}</p>
    {:else if files.length > 0}
      <ul class="file-list">
        {#each files as file}
          <li class="file-item">
            <span class="filename">{file}</span>
            <div class="download-links">
              <button 
                class="download-button"
                onclick={() => downloadFile(file)}
              >
                Download {selectedFormat.toUpperCase()}
              </button>
            </div>
          </li>
        {/each}
      </ul>
    {:else}
      <p>No files found for this ticker.</p>
    {/if}
  </div>
</main>

<style>
  .container {
    padding: 20px;
  }

  h1 {
    font-size: 18px;
  }

  .controls {
    margin-bottom: 20px;
    padding: 15px;
  }

  .ticker-section {
    margin-bottom: 15px;
  }

  .ticker-section label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .format-section {
    margin-bottom: 15px;
  }

  .format-section label,
  .interval-section label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .format-section select,
  .interval-section select {
    padding: 8px;
    font-size: 14px;
  }

  .interval-section {
    margin-bottom: 15px;
  }

  .time-format-section {
    padding-top: 15px;
  }

  .time-format-input label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .time-format-input select {
    padding: 8px;
    border: 1px solid #ccc;
    font-size: 14px;
    margin-bottom: 10px;
  }

  .custom-format-input {
    padding: 8px;
    border: 1px solid #ccc;
    font-size: 14px;
    width: 250px;
  }

  .file-list {
    list-style: none;
  }

  .file-item {
    padding: 10px 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }

  .filename {
    flex-grow: 1;
  }

  .download-links {
    display: flex;
    gap: 10px;
  }

  .download-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 8px 12px;
    cursor: pointer;
    text-decoration: none;
    font-size: 14px;
    transition: background-color 0.2s;
  }

  .download-button:hover {
    background-color: #0056b3;
  }

  .error {
    color: red;
    font-weight: bold;
  }
</style>
