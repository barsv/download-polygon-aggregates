from dash import Dash, dcc, html
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import pandas as pd

# Generate test data
N = 60000
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

app = Dash(__name__)

# Get default template and modify it
default_template = pio.templates['plotly']

# Test 1: Default template (jerky, but nice axes)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='default template'))
fig1.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

# Test 2: Override automargin directly
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='no automargin'))
fig2.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    xaxis_automargin=False,  # Override automargin
    yaxis_automargin=False
)

# Test 3: Simple template with just colors and basic axis styles
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y, mode='lines', name='minimal template'))
minimal_template = {
    'layout': {
        'colorway': ['#636efa', '#EF553B', '#00cc96'],
        'font': {'color': '#2a3f5f'},
        'paper_bgcolor': 'white',
        'plot_bgcolor': '#E5ECF6',
        'xaxis': {
            'gridcolor': 'white',
            'linecolor': 'white',
            'ticks': '',
            'zerolinecolor': 'white'
        },
        'yaxis': {
            'gridcolor': 'white', 
            'linecolor': 'white',
            'ticks': '',
            'zerolinecolor': 'white'
        }
    }
}
fig3.update_layout(
    template=minimal_template,
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)

app.layout = html.Div([
    html.H1("Template Debugging - What Causes Jerky Scroll?"),
    
    html.H4("1. Default template (jerky but nice axes)"),
    dcc.Graph(figure=fig1, config={'scrollZoom': True}),
    
    html.H4("2. Default template without automargin"),
    dcc.Graph(figure=fig2, config={'scrollZoom': True}),
    
    html.H4("3. Minimal template (just colors + basic axis styles)"),
    dcc.Graph(figure=fig3, config={'scrollZoom': True}),
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8054)
