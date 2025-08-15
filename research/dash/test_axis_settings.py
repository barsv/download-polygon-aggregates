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

# Test different axis rendering modes and settings
test_cases = [
    ("Baseline: small margins (JERKY)", {
        'margin': dict(l=0, r=0, t=10, b=0)
    }),
    
    ("automargin=False", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_automargin': False,
        'yaxis_automargin': False
    }),
    
    ("fixedrange=True (disable axis zoom)", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_fixedrange': True,
        'yaxis_fixedrange': True
    }),
    
    ("layer='below traces' (axis behind)", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_layer': 'below traces',
        'yaxis_layer': 'below traces'
    }),
    
    ("constrain='domain'", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_constrain': 'domain',
        'yaxis_constrain': 'domain'
    }),
    
    ("constraintoward='center'", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_constraintoward': 'center',
        'yaxis_constraintoward': 'center'
    }),
    
    ("scaleanchor + scaleratio", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'yaxis_scaleanchor': 'x',
        'yaxis_scaleratio': 1
    }),
    
    ("tick mode=linear, dtick=auto", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_tickmode': 'linear',
        'yaxis_tickmode': 'linear'
    }),
    
    ("side='top'+'right' (move ticks)", {
        'margin': dict(l=0, r=0, t=30, b=0),  # Need top margin
        'xaxis_side': 'top',
        'yaxis_side': 'right'
    }),
    
    ("overlaying (floating axes)", {
        'margin': dict(l=0, r=0, t=10, b=0),
        # Skip this test - needs proper axis setup
    })
]

figures = []
for title, layout_params in test_cases:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
    
    base_layout = {
        'height': 400,
        'xaxis_rangeslider_visible': False,
        'dragmode': 'zoom'
    }
    base_layout.update(layout_params)
    
    fig.update_layout(**base_layout)
    figures.append((title, fig))

app.layout = html.Div([
    html.H1("Testing Plotly Axis Rendering Settings"),
    html.P("Looking for settings that prevent jerky scroll with small margins"),
] + [
    html.Div([
        html.H4(f"{i}. {title}"),
        dcc.Graph(figure=fig, config={'scrollZoom': True})
    ]) for i, (title, fig) in enumerate(figures, 1)
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8059)
