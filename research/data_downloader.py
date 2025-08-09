"""Lightweight downloader utilities for research notebooks.

This module centralizes the `download` logic used across research notebooks so it
can be reused without copy-pasting cells. It keeps behavior identical to the
existing notebooks and avoids side effects at import time.
"""
from __future__ import annotations

import os
from typing import Optional

import requests
from tqdm import tqdm


def get_filename(ticker: str, interval: str, year: Optional[str]) -> str:
    """Return local parquet path used by notebooks.

    Note: Matches existing convention exactly, including when `year` is None.
    """
    return f"data/{ticker}_{interval}_{year}.parquet"


def _build_url(ticker: str, interval: str, year: Optional[str]) -> str:
    """Compose remote URL for seconds vs minute+ files on barsv.com."""
    if year:
        # Seconds data is partitioned by year.
        return (
            f"https://barsv.com/api/download/file/{ticker}/{year}?format=parquet&interval={interval}"
        )
    # Minute+ data uses a flat path.
    return (
        f"https://barsv.com/api/download/file/{ticker}/{ticker}_{interval}?interval={interval}&format=parquet"
    )


def download(ticker: str, interval: str, year: Optional[str]) -> str:
    """Download a parquet file with a progress bar.

    Args:
        ticker: Ticker symbol, e.g. "AAPL".
        interval: Interval string, e.g. "1m", "5s".
        year: Year string like "2024" for seconds data, or None for minute+.

    Returns:
        The path to the downloaded file.
    """
    filename = get_filename(ticker, interval, year)
    url = _build_url(ticker, interval, year)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)

    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    total_size = int(resp.headers.get("content-length", 0))

    with open(filename, "wb") as f, tqdm(
        desc=filename,
        total=total_size,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in resp.iter_content(chunk_size=1024):
            if not chunk:
                continue
            size = f.write(chunk)
            bar.update(size)

    return filename
