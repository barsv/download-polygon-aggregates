import numpy as np
import pandas as pd
import plotly.graph_objects as go
import json

# Generate test data
N = 1000  # Smaller for easier JSON inspection
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

# Create figure with margins (the problematic case)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Get the JSON that Python plotly creates
python_plotly_json = fig.to_json()

print("=== PYTHON PLOTLY JSON (with margins) ===")
print("Length:", len(python_plotly_json))

# Parse and pretty print just the layout part
fig_dict = json.loads(python_plotly_json)
layout_json = json.dumps(fig_dict['layout'], indent=2)

print("\n=== LAYOUT SECTION ===")
print(layout_json)

# Save to file for easier inspection
with open('research/dash/python_plotly_layout.json', 'w') as f:
    f.write(layout_json)

print("\nSaved layout to research/dash/python_plotly_layout.json")
print("\nNow compare this with the simple layout we used in raw plotly.js:")
print("""
{
  "margin": {"l": 0, "r": 0, "t": 10, "b": 0},
  "height": 520,
  "xaxis": {"rangeslider": {"visible": false}},
  "dragmode": "zoom"
}
""")
