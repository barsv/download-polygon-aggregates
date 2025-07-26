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
  .ticker-search input {
    padding: 8px;
    font-size: 14px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
</style>
