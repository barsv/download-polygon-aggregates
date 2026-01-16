import pandas as pd

def filter_outliers(df: pd.DataFrame, threshold: float = 3.0) -> pd.DataFrame:
    """
    Replace bad ticks using spike-and-return pattern detection.
    
    For each O/H/L/C value, check if it spikes from prev_close and returns to next_open.
    Using prev_close and next_open as anchors guarantees different ticks.
    
    A value is a bad tick if:
    1. Jump from prev_close to value exceeds threshold sigma
    2. Jump from value to next_open also exceeds threshold sigma
    3. These two jumps are in opposite directions (spike and return)
    
    Args:
        df: DataFrame with OHLC data
        threshold: Z-score threshold for both jumps (default 3.0 sigma)
    
    Returns:
        DataFrame with outliers replaced by flat bars (O=H=L=C=prev_close)
    """
    if df is None or len(df) < 3:
        return df
    
    df = df.copy()
    
    # Calculate global std from close-to-close returns
    returns = df['close'].pct_change()
    # calculate std via mad so that it will work when there are several huge outliers.
    # std = returns.std()
    # median = returns.median()
    # mad = (returns - median).abs().median()
    # std = mad * 1.4826  # Convert MAD to std equivalent
    
    # Remove extreme returns before calculating std
    returns_clipped = returns.clip(lower=returns.quantile(0.01), upper=returns.quantile(0.99))
    std = returns_clipped.std()
    
    if std == 0 or pd.isna(std):
        return df
    
    # Anchors: prev_close and next_open (guaranteed different ticks)
    prev_close = df['close'].shift(1)
    next_open = df['open'].shift(-1)
    
    def is_spike_return(value):
        """Check if value spikes from prev_close and returns to next_open."""
        jump_out = (value - prev_close) / prev_close
        jump_back = (next_open - value) / value
        return (
            (jump_out.abs() > threshold * std) & 
            (jump_back.abs() > threshold * std) & 
            (jump_out * jump_back < 0)  # Opposite signs
        )
    
    # Check all OHLC values
    open_outlier = is_spike_return(df['open'])
    high_outlier = is_spike_return(df['high'])
    low_outlier = is_spike_return(df['low'])
    close_outlier = is_spike_return(df['close'])
    
    # If any OHLC value is an outlier, replace the whole bar
    is_outlier = open_outlier | high_outlier | low_outlier | close_outlier
    
    # Replace outlier bars with flat bars (O=H=L=C=prev_close)
    if is_outlier.any():
        print(f"[filter_outliers] Found {is_outlier.sum()} outlier bars out of {len(df)}")
        prev_close_fill = prev_close.fillna(df['open'])
        
        df.loc[is_outlier, 'open'] = prev_close_fill[is_outlier]
        df.loc[is_outlier, 'high'] = prev_close_fill[is_outlier]
        df.loc[is_outlier, 'low'] = prev_close_fill[is_outlier]
        df.loc[is_outlier, 'close'] = prev_close_fill[is_outlier]
    else:
        print(f"[filter_outliers] No outliers found in {len(df)} bars")

    return df
