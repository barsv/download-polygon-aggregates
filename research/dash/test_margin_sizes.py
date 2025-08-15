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

# Test different margin scenarios
test_cases = [
    ("Tiny margins (l=0,r=0,t=10,b=0) - SHOULD BE JERKY", dict(l=0, r=0, t=10, b=0)),
    ("Small margins (l=10,r=10,t=20,b=10)", dict(l=10, r=10, t=20, b=10)),
    ("Medium margins (l=40,r=40,t=40,b=40) - Pure plotly size", dict(l=40, r=40, t=40, b=40)),
    ("Large margins (l=60,r=60,t=50,b=30)", dict(l=60, r=60, t=50, b=30)),
]

figures = []
for title, margins in test_cases:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
    fig.update_layout(
        title=title,
        margin=margins,
        height=520,
        xaxis_rangeslider_visible=False,
        dragmode='zoom'
    )
    figures.append(fig)

app.layout = html.Div([
    html.H1("Margin Size vs Jerky Scroll Test"),
    html.P("Test hypothesis: tiny margins cause tick labels to overflow and trigger layout recalculation"),
] + [
    html.Div([
        html.H4(f"{i}. {test_cases[i-1][0]}"),
        dcc.Graph(figure=fig, config={'scrollZoom': True})
    ]) for i, fig in enumerate(figures, 1)
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8056)
