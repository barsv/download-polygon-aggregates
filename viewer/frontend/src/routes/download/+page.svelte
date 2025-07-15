<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  
  let files: string[] = [];
  let loading = true;
  let error: string | null = null;
  let ticker = '';

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

  function downloadFile(filename: string, format: string) {
    const url = `/api/download/file/${ticker}/${filename}?format=${format}`;
    window.open(url, '_blank');
  }
</script>

<svelte:head>
  <title>Download Files{ticker ? ` for ${ticker}` : ''}</title>
</svelte:head>

<main class="container">
  <h1>Download Files {ticker ? ` for ${ticker}` : ''}</h1>
  
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
                class="download-button parquet"
                on:click={() => downloadFile(file, 'parquet')}
              >
                Download Parquet
              </button>
              <button 
                class="download-button csv"
                on:click={() => downloadFile(file, 'csv')}
              >
                Download CSV
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
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
    font-size: 14px;
    transition: background-color 0.2s;
  }

  .download-button:hover {
    background-color: #0056b3;
  }

  .download-button.csv {
    background-color: #28a745;
  }

  .download-button.csv:hover {
    background-color: #1e7e34;
  }

  .error {
    color: red;
    font-weight: bold;
  }
</style>
