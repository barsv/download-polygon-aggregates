# Minimal Dash app to isolate Plotly scroll-zoom relayout behavior
# Run: python -m research.dash.app3

import os
from datetime import datetime

import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash
import plotly.graph_objects as go

app = Dash(__name__, external_scripts=['https://cdn.plot.ly/plotly-2.26.0.min.js'])

# Встраиваем plotly.js прямо в HTML без dcc.Graph
app.layout = html.Div([
    html.Div(id="plotly-div", style={"width": "100%", "height": "500px"}),
    html.Pre(id='last', children='Loading...'),
    dcc.Location(id='url', refresh=False),  # Используем Location как триггер
])

# Client-side callback для инициализации plotly.js
app.clientside_callback(
    """
    function(pathname) {
        // Check if Plotly is loaded, if not wait a bit
        if (typeof Plotly === 'undefined') {
            return new Promise(function(resolve) {
                function checkPlotly() {
                    if (typeof Plotly !== 'undefined') {
                        resolve(initPlot());
                    } else {
                        setTimeout(checkPlotly, 100);
                    }
                }
                checkPlotly();
            });
        }
        
        return initPlot();
        
        function initPlot() {
            // Generate test data
            const N = 60000;
            const start = new Date('2024-01-01T00:00:00');
            
            const x = [];
            const y = [];
            let cumsum = 0;
            
            for (let i = 0; i < N; i++) {
                const timestamp = new Date(start.getTime() + i * 1000);
                x.push(timestamp);
                cumsum += (Math.random() - 0.5) * 1.0;
                y.push(cumsum);
            }
            
            // Create plot
            const trace = {
                x: x,
                y: y,
                type: 'scatter',
                mode: 'lines',
                name: 'Random Walk',
                line: {width: 1}
            };
            
            const layout = {
                title: 'Raw Plotly.js in Dash (external script)',
                margin: {l: 40, r: 40, t: 40, b: 40},
                height: 500,
                xaxis: {
                    type: 'date',
                    rangeslider: {visible: false}
                },
                dragmode: 'zoom'
            };
            
            const config = {
                scrollZoom: true,
                responsive: true
            };
            
            // Plot
            Plotly.newPlot('plotly-div', [trace], layout, config);
            
            return 'Raw plotly.js initialized successfully!';
        }
    }
    """,
    Output('last', 'children'),
    Input('url', 'pathname')
)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=False, dev_tools_hot_reload=False)
