from dash import Dash, dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Generate test data
N = 60000
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

app = Dash(__name__)

# Solution: automargin=False + manual tick configuration
fig_fixed = go.Figure()
fig_fixed.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
fig_fixed.update_layout(
    title="automargin=False + manual axis config = smooth zoom + visible axes",
    margin=dict(l=0, r=0, t=30, b=0),  # Small margins
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    
    # Disable automargin but configure axes manually
    xaxis_automargin=False,
    yaxis_automargin=False,
    
    # Manual axis configuration to ensure visibility
    xaxis=dict(
        showticklabels=True,
        tickfont=dict(size=10),
        tickmode='auto',
        showgrid=True,
        side='bottom',  # Explicitly set side
        # Position the axis to be visible despite zero margins
        anchor='free',
        position=0  # At bottom of plot area
    ),
    yaxis=dict(
        showticklabels=True, 
        tickfont=dict(size=10),
        tickmode='auto',
        showgrid=True,
        side='left',   # Explicitly set side
        # Position the axis to be visible
        anchor='free',
        position=0  # At left of plot area
    )
)

# Comparison: baseline jerky version
fig_jerky = go.Figure()
fig_jerky.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
fig_jerky.update_layout(
    title="Baseline: small margins with automargin=True (jerky)",
    margin=dict(l=0, r=0, t=30, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
    # automargin=True by default
)

app.layout = html.Div([
    html.H1("Manual Axis Configuration Solution"),
    html.P([
        "Testing: automargin=False + manual axis positioning to get ",
        "smooth zoom while keeping axes visible"
    ]),
    
    html.H3("Fixed version: automargin=False + manual config"),
    dcc.Graph(figure=fig_fixed, config={'scrollZoom': True}),
    
    html.H3("Baseline: automargin=True (for comparison)"),
    dcc.Graph(figure=fig_jerky, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    print("Testing manual axis configuration solution...")
    print("1. Open http://127.0.0.1:8062/")
    print("2. Compare scroll zoom smoothness between both graphs")
    print("3. First graph should be smooth AND have visible axes")
    
    app.run(debug=True, use_reloader=False, threaded=False, port=8062)
