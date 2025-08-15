# Test setting layout via Figure constructor vs update_layout
# Run: python test_figure_constructor.py

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

# Test 1: Via update_layout (jerky)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='update_layout'))
fig1.update_layout(
    margin=dict(l=0, r=0, t=10, b=0), 
    height=520, 
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Test 2: Via Figure constructor layout parameter (maybe smooth?)
fig2 = go.Figure(
    data=[go.Scatter(x=x, y=y, mode='lines', name='constructor layout')],
    layout=go.Layout(
        margin=dict(l=0, r=0, t=10, b=0),
        height=520,
        xaxis_rangeslider_visible=False,
        dragmode='zoom'
    )
)

# Test 3: Via Figure constructor layout dict (maybe smooth?)
fig3 = go.Figure(
    data=[go.Scatter(x=x, y=y, mode='lines', name='constructor dict')],
    layout={
        'margin': dict(l=0, r=0, t=10, b=0),
        'height': 520,
        'xaxis': {'rangeslider': {'visible': False}},
        'dragmode': 'zoom'
    }
)

app.layout = html.Div([
    html.H1("Figure Constructor vs update_layout Test"),
    
    html.H4("1. update_layout (should be jerky)"),
    dcc.Graph(figure=fig1, config={'scrollZoom': True}),
    
    html.H4("2. Figure constructor with Layout object"),
    dcc.Graph(figure=fig2, config={'scrollZoom': True}),
    
    html.H4("3. Figure constructor with layout dict"),
    dcc.Graph(figure=fig3, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False)
