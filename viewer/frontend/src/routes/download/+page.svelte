<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  
  let files: string[] = [];
  let loading = true;
  let error: string | null = null;
  let ticker = '';
  let selectedFormat = 'parquet'; // 'parquet' or 'csv'
  let timeFormat = 'timestamp'; // time format for CSV
  let customTimeFormat = 'yyyy-MM-dd HH:mm:ss'; // for custom format input

  onMount(async () => {
    // Get ticker from URL params
    ticker = $page.url.searchParams.get('ticker') || '';

    if (!ticker) {
      error = 'No ticker specified.';
      loading = false;
      return;
    }

    await loadFiles();
  });

  async function loadFiles() {
    loading = true;
    error = null;
    
    try {
      const response = await fetch(`/api/download/files/${ticker}`);
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

  function downloadFile(filename: string) {
    let url = `/api/download/file/${ticker}/${filename}?format=${selectedFormat}`;
    
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
  
  <!-- Format selection -->
  <div class="controls">
    <div class="format-section">
      <label for="format-select">File Format:</label>
      <select id="format-select" bind:value={selectedFormat}>
        <option value="parquet">Parquet</option>
        <option value="csv">CSV</option>
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
                on:click={() => downloadFile(file)}
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

  .format-section {
    margin-bottom: 15px;
  }

  .format-section label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .format-section select {
    padding: 8px;
    font-size: 14px;
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
