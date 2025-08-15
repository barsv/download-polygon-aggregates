# Test what in update_layout causes jerky scroll zoom
# Run: python test_layout_params.py

import numpy as np
import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Generate test data
N = 60000
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

app = Dash(__name__)

# Test 1: No update_layout at all (should be smooth)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='no layout'))

# Test 2: Only margins
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='only margins'))
fig2.update_layout(margin=dict(l=0, r=0, t=10, b=0))

# Test 3: Margins + height
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y, mode='lines', name='margins + height'))
fig3.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
)

# Test 4: Full layout like in app2.py
fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=x, y=y, mode='lines', name='full layout'))
fig4.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
)

app.layout = html.Div([
    html.H1("Layout Parameters Test"),
    html.P("Test which layout parameter causes jerky scroll zoom"),
    
    html.H4("1. No update_layout"),
    dcc.Graph(figure=fig1, config={'scrollZoom': True}),
    
    html.H4("2. Only margins"),
    dcc.Graph(figure=fig2, config={'scrollZoom': True}),
    
    html.H4("3. Margins + height"),
    dcc.Graph(figure=fig3, config={'scrollZoom': True}),
    
    html.H4("4. Full layout (like app2.py)"),
    dcc.Graph(figure=fig4, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False)
