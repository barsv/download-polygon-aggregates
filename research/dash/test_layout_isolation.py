# Test which specific layout parameters cause jerky scroll zoom
# Run: python test_layout_isolation.py

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

# Test 1: Just margin
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='just margin'))
fig1.update_layout(margin=dict(l=0, r=0, t=10, b=0))

# Test 2: Just height
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='just height'))
fig2.update_layout(height=520)

# Test 3: Just xaxis_rangeslider_visible
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y, mode='lines', name='just rangeslider'))
fig3.update_layout(xaxis_rangeslider_visible=False)

# Test 4: Just dragmode
fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=x, y=y, mode='lines', name='just dragmode'))
fig4.update_layout(dragmode='zoom')

# Test 5: margin + height only
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=x, y=y, mode='lines', name='margin + height'))
fig5.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=520)

app.layout = html.Div([
    html.H1("Individual Layout Parameter Test"),
    
    html.H4("1. Just margin"),
    dcc.Graph(figure=fig1, config={'scrollZoom': True}),
    
    html.H4("2. Just height"),
    dcc.Graph(figure=fig2, config={'scrollZoom': True}),
    
    html.H4("3. Just xaxis_rangeslider_visible=False"),
    dcc.Graph(figure=fig3, config={'scrollZoom': True}),
    
    html.H4("4. Just dragmode='zoom'"),
    dcc.Graph(figure=fig4, config={'scrollZoom': True}),
    
    html.H4("5. margin + height"),
    dcc.Graph(figure=fig5, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8051)
