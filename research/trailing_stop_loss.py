"""Trailing Stop Loss calculation utilities for research notebooks.

This module provides optimized functions for calculating profit/loss with trailing
stop-loss strategies using Numba for performance optimization.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Union, Optional, List
import numba


def generate_stop_loss_levels(max_sl: float = 1.0, sl_steps: int = 10) -> tuple[np.ndarray, np.ndarray]:
    """Generate symmetric stop-loss levels for long and short positions.
    
    Args:
        max_sl: Maximum stop-loss level as percentage (e.g., 1.0 for 1%)
        sl_steps: Number of steps to divide the range
        
    Returns:
        Tuple of (stop_loss_percents, stop_loss_levels)
        - stop_loss_percents: Array of percentages for display
        - stop_loss_levels: Array of fractions for calculations
    """
    sl_step = max_sl / sl_steps
    stop_loss_percents = np.concatenate((
        np.arange(-max_sl, 0, sl_step), 
        np.arange(sl_step, max_sl + sl_step, sl_step)
    ))
    stop_loss_levels = stop_loss_percents / 100
    return stop_loss_percents, stop_loss_levels


@numba.jit(nopython=True)
def calculate_pl_numba2(
    df_open: np.ndarray, 
    df_low: np.ndarray, 
    df_high: np.ndarray, 
    df_close: np.ndarray, 
    stop_loss_levels: np.ndarray
) -> np.ndarray:
    """Numba-optimized function for calculating P/L with trailing stop-loss.
    
    Args:
        df_open: Array of opening prices
        df_low: Array of low prices
        df_high: Array of high prices
        df_close: Array of closing prices
        stop_loss_levels: Array of stop-loss levels as fractions
        
    Returns:
        2D NumPy array with profits for each SL level
    """
    num_entries = len(df_open)
    num_sl_levels = len(stop_loss_levels)
    # Numba does not work well with list-of-dicts, so we collect results in a NumPy array
    results_np = np.empty(((num_entries - 1), num_sl_levels))  # profits for each SL level
    # Iterate over each stop-loss level
    for sl_idx in range(num_sl_levels):
        sl_level = stop_loss_levels[sl_idx]
        if sl_level == 0:
            continue
        # For long positions (sl_level < 0)
        if sl_level < 0:
            # Iterate over each entry in the experimental dataframe (except the last one)
            for i in range(num_entries - 1):
                entry_price = df_open[i]
                stop_price = entry_price * (1 + sl_level)
                exit_price = 0.0
                trade_closed = False
                # Search for the moment when stop-loss is triggered in the future
                for j in range(i + 1, num_entries):
                    future_low = df_low[j]
                    future_high = df_high[j]
                    if future_low <= stop_price:
                        exit_price = stop_price
                        trade_closed = True
                        break
                    else:
                        new_stop_price = future_high * (1 + sl_level)
                        if new_stop_price > stop_price:
                            stop_price = new_stop_price
                if not trade_closed:
                    exit_price = df_close[-1]
                results_np[sl_idx, i] = 100 * (exit_price - entry_price) / entry_price
        # For short positions (sl_level > 0)
        elif sl_level > 0:
            for i in range(num_entries - 1):
                entry_price = df_open[i]
                stop_price = entry_price * (1 + sl_level)
                exit_price = 0.0
                trade_closed = False
                # Search for the moment when stop-loss is triggered in the future
                for j in range(i + 1, num_entries):
                    future_low = df_low[j]
                    future_high = df_high[j]
                    if future_high >= stop_price:
                        exit_price = stop_price
                        trade_closed = True
                        break
                    else:
                        new_stop_price = future_low * (1 + sl_level)
                        if new_stop_price < stop_price:
                            stop_price = new_stop_price
                if not trade_closed:
                    exit_price = df_close[-1]
                results_np[sl_idx, i] = 100 * (entry_price - exit_price) / entry_price
    return results_np


def calculate_pl2(df_exp: pd.DataFrame, sl_levels: np.ndarray) -> pd.DataFrame:
    """Calculate profit/loss for all combinations of entry points and stop-loss levels.
    
    Args:
        df_exp: DataFrame with OHLC data (must have 'open', 'high', 'low', 'close' columns)
        sl_levels: Array of stop-loss levels as fractions
        
    Returns:
        2D NumPy array with profits for each SL level
    """
    df_open_np = df_exp['open'].to_numpy()
    df_low_np = df_exp['low'].to_numpy() 
    df_high_np = df_exp['high'].to_numpy()
    df_close_np = df_exp['close'].to_numpy()
    results_2d = calculate_pl_numba2(df_open_np, df_low_np, df_high_np, df_close_np, sl_levels)
    return results_2d


@numba.jit(nopython=True)
def calculate_pl_numba(
    df_open: np.ndarray, 
    df_low: np.ndarray, 
    df_high: np.ndarray, 
    df_close: np.ndarray, 
    stop_loss_levels: np.ndarray
) -> np.ndarray:
    """Numba-optimized function for calculating P/L with trailing stop-loss.
    
    Args:
        df_open: Array of opening prices
        df_low: Array of low prices
        df_high: Array of high prices
        df_close: Array of closing prices
        stop_loss_levels: Array of stop-loss levels as fractions
        
    Returns:
        2D NumPy array with columns: [index, sl_level, profit, entry_price]
    """
    num_entries = len(df_open)
    num_sl_levels = len(stop_loss_levels)
    # Numba does not work well with list-of-dicts, so we collect results in a NumPy array
    results_np = np.empty(((num_entries - 1) * num_sl_levels, 4))  # index, sl_level, profit, entry_price
    result_idx = 0

    # Iterate over each entry in the experimental dataframe (except the last one)
    for i in range(num_entries - 1):
        entry_price = df_open[i]

        # Iterate over each stop-loss level
        for sl_idx in range(num_sl_levels):
            sl_level = stop_loss_levels[sl_idx]
            if sl_level == 0:
                continue

            stop_price = entry_price * (1 + sl_level)
            exit_price = 0.0
            trade_closed = False

            # Search for the moment when stop-loss is triggered in the future
            for j in range(i + 1, num_entries):
                future_low = df_low[j]
                future_high = df_high[j]

                # For long positions (sl_level < 0)
                if sl_level < 0:
                    if future_low <= stop_price:
                        exit_price = stop_price
                        trade_closed = True
                        break
                    else:
                        new_stop_price = future_high * (1 + sl_level)
                        if new_stop_price > stop_price:
                            stop_price = new_stop_price
                # For short positions (sl_level > 0)
                elif sl_level > 0:
                    if future_high >= stop_price:
                        exit_price = stop_price
                        trade_closed = True
                        break
                    else:
                        new_stop_price = future_low * (1 + sl_level)
                        if new_stop_price < stop_price:
                            stop_price = new_stop_price

            if not trade_closed:
                exit_price = df_close[-1]

            profit = 0.0
            if sl_level < 0:
                profit = 100 * (exit_price - entry_price) / entry_price
            elif sl_level > 0:
                profit = 100 * (entry_price - exit_price) / entry_price

            results_np[result_idx, 0] = i
            results_np[result_idx, 1] = sl_level
            results_np[result_idx, 2] = profit
            results_np[result_idx, 3] = entry_price

            result_idx += 1

    return results_np[:result_idx]  # Return only the filled part of the array


def calculate_pl(df_exp: pd.DataFrame, sl_levels: np.ndarray) -> pd.DataFrame:
    """Calculate profit/loss for all combinations of entry points and stop-loss levels.
    
    Args:
        df_exp: DataFrame with OHLC data (must have 'open', 'high', 'low', 'close' columns)
        sl_levels: Array of stop-loss levels as fractions
        
    Returns:
        DataFrame with columns: ['index', 'sl_level', 'profit', 'entry_price']
    """
    df_open_np = df_exp['open'].to_numpy()
    df_low_np = df_exp['low'].to_numpy() 
    df_high_np = df_exp['high'].to_numpy()
    df_close_np = df_exp['close'].to_numpy()

    results_2d = calculate_pl_numba(df_open_np, df_low_np, df_high_np, df_close_np, sl_levels)
    
    # More readable unpacking
    i_np = results_2d[:, 0].astype(int)
    sl_level_np = results_2d[:, 1] 
    profit_np = results_2d[:, 2]
    entry_price_np = results_2d[:, 3]
    
    results_df = pd.DataFrame({
        'index': i_np,
        'sl_level': sl_level_np,
        'profit': profit_np, 
        'entry_price': entry_price_np
    })
    
    return results_df


def slice_results_by_time(
    results_df: pd.DataFrame, 
    start_idx: Optional[int] = None, 
    end_idx: Optional[int] = None, 
    num_points: Optional[int] = None
) -> pd.DataFrame:
    """Slice results by time indices (not by DataFrame rows).
    
    Args:
        results_df: Results DataFrame from calculate_pl()
        start_idx: Starting time index (not row index)
        end_idx: Ending time index (not row index)
        num_points: Alternative to end_idx, take N time points from start_idx
        
    Returns:
        Filtered DataFrame with normalized indices starting from 0
    """
    if num_points is not None:
        end_idx = start_idx + num_points if start_idx is not None else num_points
    
    mask = True
    if start_idx is not None:
        mask &= (results_df['index'] >= start_idx)
    if end_idx is not None:
        mask &= (results_df['index'] < end_idx)
    
    sliced_df = results_df[mask].copy()
    
    # Normalize indices to start from 0
    if start_idx is not None and len(sliced_df) > 0:
        sliced_df['index'] = sliced_df['index'] - start_idx
    
    return sliced_df
