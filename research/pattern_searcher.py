"""Pattern searching utilities using optimized normalized cross-correlation.

This module provides the PatternSearcher class for efficient pattern matching
in time series data using FFT-based correlation and precomputed statistics.
"""
from __future__ import annotations

import numpy as np
from scipy import signal
from typing import List, Optional, Tuple, Union, Dict, Any


class PatternSearcher:
    """
    An optimized class to pre-calculate cumulative sums and rolling window statistics
    for pattern searching using Normalized Cross-Correlation with fixed template length.
    """
    
    def __init__(self, series, template_length: int):
        """
        Initializes the PatternSearcher with a time series and fixed template length.
        Precomputes all rolling window statistics for efficiency.

        Args:
            series: The time series data (pandas Series or NumPy array).
            template_length: Fixed length of all templates that will be searched.
        """
        # Convert the series to a NumPy array with float64 dtype for numerical stability
        self.series = np.asarray(series, dtype=np.float64)
        self.n = len(self.series)
        self.m = template_length
        
        if self.m > self.n:
            raise ValueError("Template length is greater than series length.")

        # Pre-calculate cumulative sums
        self.cum_sum_x = np.cumsum(self.series)
        self.cum_sum_x_sq = np.cumsum(self.series**2)
        
        # --- Pre-calculate all rolling window statistics for the series ---
        # Rolling sum of x for each window
        self.sum_x = self.cum_sum_x[self.m-1:] - np.concatenate(([0], self.cum_sum_x[:-self.m]))
        # Rolling sum of x^2 for each window  
        self.sum_x_sq = self.cum_sum_x_sq[self.m-1:] - np.concatenate(([0], self.cum_sum_x_sq[:-self.m]))
        
        # Denominator term for x for each window (precomputed)
        self.denom_x = self.m * self.sum_x_sq - self.sum_x**2
        # Avoid division by zero for windows with no variance
        self.denom_x[self.denom_x <= 1e-10] = 1  # Set to 1 to avoid NaN, result will be 0 anyway
        
        # Number of valid windows
        self.num_windows = len(self.sum_x)

    def search(self, template) -> Optional[np.ndarray]:
        """
        Finds correlation coefficients for a template pattern within the time series
        using optimized Normalized Cross-Correlation.

        Args:
            template: The pattern template to search for (pandas Series or NumPy array).
                     Must have length equal to template_length specified in constructor.

        Returns:
            NumPy array of correlation coefficients for all valid windows,
            or None if the template has zero variance.
        """
        # Convert the template to a NumPy array with float64 dtype
        template = np.asarray(template, dtype=np.float64)
        
        if len(template) != self.m:
            raise ValueError(f"Template length {len(template)} does not match expected length {self.m}")

        # --- Calculate terms for the template (y) ---
        sum_y = template.sum()
        sum_y_sq = (template**2).sum()
        # Denominator term for y, which is constant
        denom_y = self.m * sum_y_sq - sum_y**2

        if denom_y <= 1e-10:  # Use a small epsilon for floating point comparison
            print("Template has zero variance, cannot perform matching.")
            return None

        # --- Calculate cross-correlation term sum(xy) using FFT ---
        # This is the sum(x*y) term, calculated efficiently using FFT
        sum_xy = signal.fftconvolve(self.series, template[::-1], mode='valid')

        # --- Calculate Correlation Coefficient (r) for all windows ---
        # Numerator term (using precomputed sum_x)
        num = self.m * sum_xy - self.sum_x * sum_y
        # Denominator term (using precomputed denom_x)
        denom = np.sqrt(self.denom_x * denom_y)

        r = num / denom

        return r
    
    def get_rs_above(self, template, r_limit: float) -> Optional[List[Tuple[int, float]]]:
        """
        Get correlation results above the given r_limit.
        
        Args:
            template: The pattern template to search for.
            r_limit: The minimum correlation threshold (can be negative for negative correlations).
        
        Returns:
            List of tuples (index, correlation_value) where absolute correlation >= r_limit,
            or None if search failed.
        """
        r = self.search(template)
        if r is None:
            return None
        
        # Find indices where absolute correlation is above the limit
        above_limit_mask = np.abs(r) >= r_limit
        above_limit_indices = np.where(above_limit_mask)[0]
        above_limit_values = r[above_limit_indices]
        
        # Return as list of tuples (index, correlation_value)
        return list(zip(above_limit_indices, above_limit_values))

    def get_sorted_r(self, template, return_top_k: Optional[int] = None) -> Optional[List[Tuple[int, float]]]:
        """
        Get sorted correlation results with optional optimization for top-K results.
        
        Args:
            template: The pattern template to search for.
            return_top_k: If specified, return only the top K results using argpartition
                         for better performance. If None, return all results sorted.
        
        Returns:
            List of tuples (index, correlation_value) sorted by absolute correlation.
        """
        r = self.search(template)
        if r is None:
            return None
            
        # OPTIMIZATION: Use argpartition for top-K selection instead of full sorting
        if return_top_k is not None and return_top_k < len(r):
            # Use argpartition to find top-K efficiently (O(n) vs O(n log n))
            abs_r = np.abs(r)
            top_k_indices = np.argpartition(abs_r, -return_top_k)[-return_top_k:]
            # Sort only the top-K results
            sorted_within_top = np.argsort(abs_r[top_k_indices])[::-1]
            final_indices = top_k_indices[sorted_within_top]
            top_r_values = r[final_indices]
            return list(zip(final_indices, top_r_values))
        else:
            # Full sorting (original behavior)
            top_indices = np.argsort(np.abs(r))[::-1]
            top_r_values = r[top_indices]
            return list(zip(top_indices, top_r_values))
            
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the searcher for debugging/monitoring.
        
        Returns:
            Dictionary with searcher statistics.
        """
        memory_usage_mb = (
                self.series.nbytes + 
                self.cum_sum_x.nbytes + 
                self.cum_sum_x_sq.nbytes +
                self.sum_x.nbytes +
                self.sum_x_sq.nbytes +
                self.denom_x.nbytes
            ) / 1024**2
        return {
            'series_length': self.n,
            'template_length': self.m, 
            'num_windows': self.num_windows,
            'memory_usage_mb': f'{memory_usage_mb:.2f}'
        }
