# Minimal reproducible example for plotly.py issue
# 
# Issue: Jerky scroll zoom with small margins in Dash
# 
# Description: When using small margins (e.g., l=0, r=0) in Dash + plotly.py,
# scroll zoom becomes jerky due to layout recalculations triggered by tick 
# label overflow. Pure plotly.js handles this gracefully by clipping labels
# without causing jerky behavior.

import numpy as np
import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Generate test data
N = 60000  # Large dataset needed to reproduce the issue
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

app = Dash(__name__)

# Problematic case: small margins cause jerky scroll zoom
fig_jerky = go.Figure()
fig_jerky.add_trace(go.Scatter(x=x, y=y, mode='lines', name='jerky'))
fig_jerky.update_layout(
    title="JERKY: Small margins (l=0, r=0, t=10, b=0)",
    margin=dict(l=0, r=0, t=10, b=0),  # Small margins
    height=400,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Working case: larger margins work fine
fig_smooth = go.Figure()
fig_smooth.add_trace(go.Scatter(x=x, y=y, mode='lines', name='smooth'))
fig_smooth.update_layout(
    title="SMOOTH: Large margins (l=50, r=50, t=20, b=0)",
    margin=dict(l=50, r=50, t=20, b=0),  # Sufficient margins
    height=400,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

app.layout = html.Div([
    html.H1("plotly.py Issue: Jerky Scroll Zoom with Small Margins"),
    html.P([
        "Bug reproduction: ",
        html.Br(),
        "1. Use scroll wheel to zoom on both graphs",
        html.Br(),
        "2. First graph (small margins) will be jerky",
        html.Br(),
        "3. Second graph (large margins) will be smooth",
        html.Br(),
        "4. Same issue does NOT occur in pure plotly.js"
    ]),
    
    dcc.Graph(figure=fig_jerky, config={'scrollZoom': True}),
    dcc.Graph(figure=fig_smooth, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    print("Bug reproduction steps:")
    print("1. Open http://127.0.0.1:8058/")
    print("2. Use scroll wheel to zoom on both graphs")
    print("3. Notice jerky behavior on first graph")
    print("4. Compare with smooth behavior on second graph")
    print()
    print("Environment:")
    import plotly
    print(f"- plotly: {plotly.__version__}")
    
    import dash
    print(f"- dash: {dash.__version__}")
    
    app.run(debug=True, use_reloader=False, threaded=False, port=8058)
