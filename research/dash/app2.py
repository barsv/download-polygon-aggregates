# Minimal Dash app to isolate Plotly scroll-zoom relayout behavior
# Run: python -m research.dash.app2

import os
from datetime import datetime

import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash
import plotly.graph_objects as go

# --- Generate a simple time series ---
N = 60000  # ~ 60k points
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')  # 1-second grid
# Random walk
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

fig = go.Figure()
fig.add_trace(go.Scattergl(x=x, y=y, mode='lines', name='y'))
fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    uirevision='minimal-example',
    dragmode='zoom',
)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='g', figure=fig, config={'scrollZoom': True}),
    html.Pre(id='last'),
])

# Simple logger

def log(msg: str) -> None:
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{ts} {msg}")

# Keep only a small UI echo of the latest range; do not modify the figure from the server
@app.callback(
    Output('last', 'children'),
    Input('g', 'relayoutData'),
    prevent_initial_call=True,
)
def on_relayout(relayout):
    if not relayout:
        return dash.no_update
    log('relayout')
    x0 = relayout.get('xaxis.range[0]')
    x1 = relayout.get('xaxis.range[1]')
    if x0 and x1:
        log(f"relayout x0={x0}")
        return f"x0={x0}\nx1={x1}"
    return dash.no_update


if __name__ == '__main__':
    # Threaded=False to reduce variability; but behavior should reproduce either way
    app.run(debug=True, use_reloader=False, threaded=False, dev_tools_hot_reload=False)
