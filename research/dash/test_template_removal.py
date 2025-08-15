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

# Test 1: Python plotly with template (jerky)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='with template'))
fig1.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Test 2: Python plotly WITHOUT template (maybe smooth?)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='no template'))
fig2.update_layout(
    template=None,  # Remove template!
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Test 3: Python plotly with minimal template
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y, mode='lines', name='minimal template'))
fig3.update_layout(
    template='none',  # Minimal template
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

app.layout = html.Div([
    html.H1("Template vs No Template Test"),
    
    html.H4("1. With default template (should be jerky)"),
    dcc.Graph(figure=fig1, config={'scrollZoom': True}),
    
    html.H4("2. template=None"),
    dcc.Graph(figure=fig2, config={'scrollZoom': True}),
    
    html.H4("3. template='none'"),
    dcc.Graph(figure=fig3, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8053)
