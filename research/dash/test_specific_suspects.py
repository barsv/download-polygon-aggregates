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

# Test different suspects for jerky behavior
suspects = [
    # 1. automargin
    {'name': 'automargin=False', 'layout': {'xaxis_automargin': False, 'yaxis_automargin': False}},
    
    # 2. zerolinewidth 
    {'name': 'zerolinewidth=1', 'layout': {'xaxis_zerolinewidth': 1, 'yaxis_zerolinewidth': 1}},
    
    # 3. No gridcolor
    {'name': 'no gridcolor', 'layout': {'xaxis_gridcolor': None, 'yaxis_gridcolor': None}},
    
    # 4. No template data (colorscales etc)
    {'name': 'simple template', 'layout': {'template': {
        'layout': {
            'colorway': ['#636efa'],
            'paper_bgcolor': 'white',
            'plot_bgcolor': '#E5ECF6'
        }
    }}},
]

figures = []
for i, suspect in enumerate(suspects, 1):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=suspect['name']))
    
    layout_params = {
        'margin': dict(l=0, r=0, t=10, b=0),
        'height': 520,
        'xaxis_rangeslider_visible': False,
        'dragmode': 'zoom'
    }
    layout_params.update(suspect['layout'])
    
    fig.update_layout(**layout_params)
    figures.append((suspect['name'], fig))

# Add baseline with template='none' for comparison
fig_baseline = go.Figure()
fig_baseline.add_trace(go.Scatter(x=x, y=y, mode='lines', name='template=none'))
fig_baseline.update_layout(
    template='none',
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom'
)
figures.append(('template=none (baseline)', fig_baseline))

app.layout = html.Div([
    html.H1("Debugging Specific Template Properties"),
    html.P("Test each to see which ones cause jerky scroll zoom:"),
] + [
    html.Div([
        html.H4(f"{i}. {name}"),
        dcc.Graph(figure=fig, config={'scrollZoom': True})
    ]) for i, (name, fig) in enumerate(figures, 1)
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8055)
