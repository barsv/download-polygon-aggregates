# Test uirevision impact on scroll zoom
# Run: python test_uirevision.py

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

# Test different uirevision settings
fig_with_uirevision = go.Figure()
fig_with_uirevision.add_trace(go.Scatter(x=x, y=y, mode='lines', name='with uirevision'))
fig_with_uirevision.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=400,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    uirevision='test',  # This causes jerky scroll zoom
    title='WITH uirevision (should be jerky)'
)

fig_without_uirevision = go.Figure()
fig_without_uirevision.add_trace(go.Scatter(x=x, y=y, mode='lines', name='without uirevision'))
fig_without_uirevision.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=400,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    # NO uirevision - this should be smooth
    title='WITHOUT uirevision (should be smooth)'
)

app.layout = html.Div([
    html.H1("uirevision Impact Test"),
    html.P("Test scroll zoom on both graphs. The first should be jerky, the second smooth."),
    
    dcc.Graph(figure=fig_with_uirevision, config={'scrollZoom': True}),
    html.Hr(),
    dcc.Graph(figure=fig_without_uirevision, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False)
