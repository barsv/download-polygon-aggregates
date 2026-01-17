
export interface Bar {
    time: number;
    open: number;
    high: number;
    low: number;
    close: number;
}

export interface ViewportResponse {
    ticker: string;
    bars: Bar[];
}

export async function fetchTickers(): Promise<string[]> {
    const res = await fetch('/api/tickers');
    const data = await res.json();
    return data.tickers || [];
}

export async function fetchViewportData(ticker: string, start: number, end: number, width: number, signal?: AbortSignal): Promise<Bar[]> {
    // start and end are unix timestamps (seconds)
    const url = `/api/viewport/${ticker}?start_timestamp=${Math.floor(start)}&end_timestamp=${Math.floor(end)}&screen_width_pixels=${Math.floor(width)}`;
    const res = await fetch(url, { signal });
    if (!res.ok) {
        throw new Error('Failed to fetch data');
    }
    const data = await res.json();
    return data.bars || [];
}

export async function fetchTickerMeta(ticker: string): Promise<{ last_timestamp: number }> {
    const res = await fetch(`/api/meta/${ticker}`);
    if (!res.ok) throw new Error("Failed to fetch meta");
    return await res.json();
}

