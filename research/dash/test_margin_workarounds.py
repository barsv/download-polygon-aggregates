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

# Test potential workarounds for tiny margins
workarounds = [
    ("Baseline: tiny margins (l=0,r=0,t=10,b=0)", {
        'margin': dict(l=0, r=0, t=10, b=0)
    }),
    
    ("fixedrange=True (disable zoom on axes)", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_fixedrange': False,  # Keep zoom
        'yaxis_fixedrange': False   # Keep zoom
    }),
    
    ("Custom tick format (shorter labels)", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_tickformat': '%H:%M',  # Shorter time format
        'yaxis_tickformat': '.1f'     # Shorter number format
    }),
    
    ("Hide tick labels but keep ticks", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_showticklabels': False,
        'yaxis_showticklabels': False
    }),
    
    ("Smaller tick font", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_tickfont_size': 8,
        'yaxis_tickfont_size': 8
    }),
    
    ("automargin=False + tiny margins", {
        'margin': dict(l=0, r=0, t=10, b=0),
        'xaxis_automargin': False,
        'yaxis_automargin': False
    })
]

figures = []
for title, layout_params in workarounds:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
    
    base_layout = {
        'height': 520,
        'xaxis_rangeslider_visible': False,
        'dragmode': 'zoom'
    }
    base_layout.update(layout_params)
    
    fig.update_layout(**base_layout)
    figures.append((title, fig))

app.layout = html.Div([
    html.H1("Workarounds for Tiny Margins Jerky Scroll"),
    html.P("Testing different approaches to fix jerky scroll with minimal margins"),
] + [
    html.Div([
        html.H4(f"{i}. {title}"),
        dcc.Graph(figure=fig, config={'scrollZoom': True})
    ]) for i, (title, fig) in enumerate(figures, 1)
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8057)
