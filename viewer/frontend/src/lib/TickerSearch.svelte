<script lang="ts">
  import { onMount, onDestroy } from 'svelte';

  let { value = '', placeholder = 'e.g. AAPL', onchange }: {
    value?: string;
    placeholder?: string;
    onchange?: (ticker: string) => void;
  } = $props();

  let tickers = $state<string[]>([]);
  let searchInput = $state(value);
  let debounceTimer = $state<number>(0);

  // Update searchInput when value prop changes externally
  $effect(() => {
    searchInput = value;
  });

  async function fetchTickers(searchTerm = ''): Promise<string[]> {
    let url = '/api/tickers';
    if (searchTerm) {
      url += `?search=${searchTerm}`;
    }
    const res = await fetch(url);
    const data = await res.json();
    return data.tickers || [];
  }

  onMount(async () => {
    tickers = await fetchTickers();
  });

  onDestroy(() => {
    clearTimeout(debounceTimer);
  });

  function handleFocus(event: Event) {
    const target = event.target as HTMLInputElement;
    target.select();
  }

  function handleInput(event: Event) {
    clearTimeout(debounceTimer);
    const target = event.target as HTMLInputElement;
    const searchTerm = target.value;
    searchInput = searchTerm.toUpperCase();
    
    debounceTimer = setTimeout(async () => {
      tickers = await fetchTickers(searchTerm);
    }, 300);
  }

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      handleSelection();
    }
  }

  function handleSelection() {
    // When selecting ticker (blur, change, enter) - if entered ticker is in the list, select it
    if (tickers.includes(searchInput) && searchInput !== value) {
      onchange?.(searchInput);
    } else if (searchInput !== value) {
      // Otherwise revert to previous value
      searchInput = value;
    }
  }

  function handleBlur() {
    handleSelection();
  }
</script>

<div class="ticker-search">
  <input
    type="text"
    list="ticker-list"
    bind:value={searchInput}
    oninput={handleInput}
    onkeydown={handleKeydown}
    onfocus={handleFocus}
    onblur={handleBlur}
    onchange={handleSelection}
    {placeholder}
  />
  <datalist id="ticker-list">
    {#each tickers as ticker}
      <option value={ticker}>{ticker}</option>
    {/each}
  </datalist>
</div>

<style>
  .ticker-search {
    position: relative;
    display: flex;
    align-items: center;
  }
  .ticker-search input {
    padding: 8px 12px;
    font-size: 14px;
    width: 140px;
    background: rgba(255, 255, 255, 0.05);
    color: inherit;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 6px;
    outline: none;
    transition: all 0.2s ease;
    font-weight: 500;
  }
  .ticker-search input:focus {
    border-color: #4a90e2;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
    width: 180px;
  }
  .ticker-search input::placeholder {
    color: rgba(255, 255, 255, 0.3);
  }
</style>
