# Debug dcc.Graph internals
# Run: python debug_dcc_graph.py

import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import json

# Generate test data
N = 60000  # Same as problematic app2.py
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y', line=dict(width=1)))
fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
)

app = Dash(__name__)

app.layout = html.Div([
    html.H3("dcc.Graph Debug"),
    html.Pre(id='graph-props', style={'background': '#f0f0f0', 'padding': '10px'}),
    
    # Try different configurations
    html.H4("Standard dcc.Graph:"),
    dcc.Graph(id='g1', figure=fig, config={'scrollZoom': True}),
    
    html.H4("dcc.Graph without uirevision:"),  
    dcc.Graph(id='g2', figure=fig, config={'scrollZoom': True}),
    
    html.H4("dcc.Graph with minimal layout:"),
    dcc.Graph(id='g3', config={'scrollZoom': True}),
])

# Minimal figure for g3
minimal_fig = go.Figure()
minimal_fig.add_trace(go.Scatter(x=x[:1000], y=y[:1000], mode='lines', name='minimal'))
minimal_fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

@app.callback(
    [Output('g2', 'figure'), Output('g3', 'figure')],
    [Input('g1', 'id')]  # Trigger on app load
)
def update_graphs(dummy):
    # g2: Same figure but recreate without copy
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y', line=dict(width=1)))
    # Explicitly don't set uirevision
    
    return fig2, minimal_fig

# Log what's happening in dcc.Graph
app.clientside_callback(
    """
    function(id) {
        // Get the actual plotly config and layout that dcc.Graph created
        setTimeout(function() {
            const g1 = document.getElementById('g1');
            const g2 = document.getElementById('g2');
            const g3 = document.getElementById('g3');
            
            let debug_info = 'dcc.Graph Debug Info:\\n\\n';
            
            if (g1 && g1.layout) {
                debug_info += 'G1 Layout keys: ' + Object.keys(g1.layout).join(', ') + '\\n';
                debug_info += 'G1 Config: ' + JSON.stringify(g1.config || {}, null, 2) + '\\n\\n';
            }
            
            if (g2 && g2.layout) {
                debug_info += 'G2 Layout keys: ' + Object.keys(g2.layout).join(', ') + '\\n';
                debug_info += 'G2 Config: ' + JSON.stringify(g2.config || {}, null, 2) + '\\n\\n';
            }
            
            if (g3 && g3.layout) {
                debug_info += 'G3 Layout keys: ' + Object.keys(g3.layout).join(', ') + '\\n';
                debug_info += 'G3 Config: ' + JSON.stringify(g3.config || {}, null, 2) + '\\n\\n';
            }
            
            debug_info += 'Plotly version: ' + (typeof Plotly !== 'undefined' ? Plotly.version : 'unknown');
            
            return debug_info;
        }, 500);
        
        return 'Loading debug info...';
    }
    """,
    Output('graph-props', 'children'),
    Input('g1', 'id')
)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False)
