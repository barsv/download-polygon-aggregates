from dash import Dash, html, Input, Output, clientside_callback, ClientsideFunction
import numpy as np
import pandas as pd
import json

# Generate test data
N = 60000
start = pd.Timestamp('2024-01-01 00:00:00')
x = pd.date_range(start=start, periods=N, freq='s')
rng = np.random.default_rng(42)
y = np.cumsum(rng.normal(loc=0.0, scale=0.5, size=N))

# Convert to JSON-serializable format
data = {
    'x': [t.isoformat() for t in x],
    'y': y.tolist()
}

app = Dash(__name__, external_scripts=[
    'https://cdn.plot.ly/plotly-2.24.1.min.js'
])

app.layout = html.Div([
    html.H1("Raw plotly.js in Dash with Margins Test"),
    
    html.H3("1. No margins"),
    html.Div(id='plot1', style={'width': '100%', 'height': '400px'}),
    
    html.H3("2. With margins (l=0,r=0,t=10,b=0)"),
    html.Div(id='plot2', style={'width': '100%', 'height': '400px'}),
    
    html.H3("3. Full config: margins + height"),
    html.Div(id='plot3', style={'width': '100%', 'height': '520px'}),
    
    # Store data
    html.Div(id='data-store', children=json.dumps(data), style={'display': 'none'})
])

# Clientside callback to create plots with raw plotly.js
clientside_callback(
    """
    function(data_json) {
        const data = JSON.parse(data_json);
        
        const trace = {
            x: data.x,
            y: data.y,
            type: 'scatter',
            mode: 'lines',
            name: 'data'
        };
        
        const config = {
            scrollZoom: true,
            displayModeBar: true
        };
        
        // Plot 1: No margins
        const layout1 = {
            title: 'No margins',
            xaxis: {rangeslider: {visible: false}},
            dragmode: 'zoom'
        };
        
        Plotly.newPlot('plot1', [trace], layout1, config);
        
        // Plot 2: With margins
        const layout2 = {
            title: 'With margins',
            margin: {l: 0, r: 0, t: 10, b: 0},
            xaxis: {rangeslider: {visible: false}},
            dragmode: 'zoom'
        };
        
        Plotly.newPlot('plot2', [trace], layout2, config);
        
        // Plot 3: Full config
        const layout3 = {
            title: 'Full config',
            margin: {l: 0, r: 0, t: 10, b: 0},
            height: 520,
            xaxis: {rangeslider: {visible: false}},
            dragmode: 'zoom'
        };
        
        Plotly.newPlot('plot3', [trace], layout3, config);
        
        return 'Plots created';
    }
    """,
    Output('plot1', 'title'),  # Dummy output
    Input('data-store', 'children')
)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, port=8052)
