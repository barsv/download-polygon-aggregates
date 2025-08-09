"""Pattern analysis utilities for research notebooks.

This module centralizes mathematical functions used for pattern matching and 
correlation analysis across research notebooks.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Optional, Tuple, Union


def get_alpha_lambda(
    a0: Union[np.ndarray, pd.Series], 
    a: Union[np.ndarray, pd.Series], 
    sum_a0: Optional[float] = None
) -> Tuple[float, float]:
    """Calculate linear transformation coefficients to match pattern a to a0.
    
    Computes alpha and lambda such that: a0 ≈ alpha * a + lambda
    This is used for rescaling patterns to match a reference pattern.
    
    Args:
        a0: Reference pattern (target).
        a: Pattern to be transformed.
        sum_a0: Precomputed sum of a0 for optimization when reusing a0.
        
    Returns:
        Tuple of (alpha, lambda) coefficients. Returns (nan, nan) if 
        transformation is not possible (e.g., when pattern has no variance).
        
    Note:
        sum_a0 parameter is for speed optimization when you have 1 a0 and many a patterns.
    """
    m = len(a)
    sum_a = a.sum()
    if sum_a0 is None:
        sum_a0 = a0.sum()
    sum_a_sq = (a**2).sum()
    sum_a_a0 = (a * a0).sum()

    divider = m * sum_a_sq - sum_a**2
    if divider == 0:
        # Pattern has no variance, transformation not possible
        return np.nan, np.nan

    alpha = (m * sum_a_a0 - sum_a * sum_a0) / divider
    lmbda = (sum_a0 - alpha * sum_a) / m
    return alpha, lmbda


def get_rmse(
    a0: Union[np.ndarray, pd.Series], 
    a: Union[np.ndarray, pd.Series]
) -> float:
    """Calculate root mean square error of linear fit between two patterns.

    Computes the RMSE after applying optimal linear transformation to match 
    pattern a to reference pattern a0.

    Args:
        a0: Reference pattern (target).
        a: Pattern to be compared.

    Returns:
        Root mean square error after optimal linear transformation.
        Returns 1e9 (large number) if transformation is not possible.
    """
    alpha, lmbda = get_alpha_lambda(a0, a)
    if np.isnan(alpha):
        return 1e9  # Large number when transformation not possible
    
    a_transformed = alpha * a + lmbda
    return np.sqrt(np.mean((a0 - a_transformed)**2))


def create_window(
    df: pd.DataFrame, 
    index: int, 
    window_size: int
) -> np.ndarray:
    """Extract a window of 'open' prices from DataFrame with proper dtype.
    
    Args:
        df: DataFrame containing 'open' column.
        index: Starting index for the window.
        window_size: Number of bars to include in window.
        
    Returns:
        NumPy array of 'open' prices as float64.
        
    Note:
        astype(np.float64) is needed because later calculations like
        `m * sum_a_sq - sum_a**2` would be zero in float32 due to 
        floating-point precision issues.
    """
    return df.loc[index:index + window_size - 1]['open'].astype(np.float64).values
