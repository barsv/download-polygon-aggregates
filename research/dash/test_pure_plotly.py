# Test pure Python Plotly scroll zoom
# Run: python test_pure_plotly.py

import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Generate test data (same as before)
N = 60000
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

print(f"Generated {N} data points")

# Create figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Random Walk', line=dict(width=1)))

fig.update_layout(
    title='Pure Python Plotly Scroll Zoom Test',
    margin=dict(l=40, r=40, t=40, b=40),
    height=600,
    xaxis=dict(
        type='date',
        rangeslider=dict(visible=False)
    ),
    dragmode='zoom'
)

# This will open browser with pure plotly.js (no Dash wrapper)
print("Opening browser with pure Python Plotly...")
print("Test scroll zoom behavior in the browser")

# Enable scroll zoom in config
config = {
    'scrollZoom': True,
    'displayModeBar': True
}

fig.show(config=config)

# Keep the script running so server doesn't shut down immediately
input("Press Enter to exit...")
