from dash import Dash, dcc, html, Input, Output, clientside_callback, no_update
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

# Create problematic figure with small margins
fig_jerky = go.Figure()
fig_jerky.add_trace(go.Scatter(x=x, y=y, mode='lines', name='data'))
fig_jerky.update_layout(
    title="Small margins with clientside callback debouncing",
    margin=dict(l=0, r=0, t=30, b=0),  # Small margins that cause jerky behavior
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    uirevision='main-graph'  # Preserve UI state
)

app.layout = html.Div([
    html.H1("Clientside Callback Solution for Jerky Scroll Zoom"),
    html.P([
        "Testing Gemini's idea: Block automargin-only relayout events during scroll zoom ",
        "to prevent jerky behavior while keeping axes visible."
    ]),
    
    dcc.Graph(
        id='main-graph',
        figure=fig_jerky,
        config={'scrollZoom': True}
    ),
    
    # Debug output to see what's happening
    html.Div(id='debug-output', style={'margin': '20px', 'padding': '10px', 'background': '#f0f0f0'}),
    html.Div(id='dummy-output', style={'display': 'none'})  # Dummy output for callback
])

# Clientside callback to debounce relayout events during scroll zoom
clientside_callback(
    """
    function(relayoutData) {
        if (!relayoutData) {
            return [dash_clientside.no_update, 'No relayout data'];
        }
        
        console.log('Relayout event:', relayoutData);
        
        // Store the timeout ID and latest relayout data in window object
        window.relayoutTimeout = window.relayoutTimeout || null;
        window.latestRelayoutData = relayoutData;
        
        const keys = Object.keys(relayoutData);
        
        // Check if this is likely an automargin change during zoom
        const hasRangeChange = keys.some(k => 
            k.includes('range') && !k.includes('autorange')
        );
        const hasMarginChange = keys.some(k => 
            k.includes('margin') || k.includes('automargin')
        );
        
        // If this looks like automargin during zoom, debounce it
        if (hasMarginChange && !hasRangeChange) {
            console.log('Debouncing automargin relayout...');
            
            // Clear previous timeout
            if (window.relayoutTimeout) {
                clearTimeout(window.relayoutTimeout);
            }
            
            // Set new timeout - wait for zoom to finish
            window.relayoutTimeout = setTimeout(function() {
                console.log('Timeout fired, applying final relayout:', window.latestRelayoutData);
                // In a real implementation, we'd need to manually trigger the relayout here
                // For now, just log it
            }, 150); // 150ms delay
            
            return [
                dash_clientside.no_update, 
                'DEBOUNCED automargin relayout (waiting for zoom to finish...)'
            ];
        }
        
        // For regular zoom events, clear any pending timeout and allow immediately
        if (hasRangeChange) {
            if (window.relayoutTimeout) {
                clearTimeout(window.relayoutTimeout);
                window.relayoutTimeout = null;
            }
            console.log('Range change - allowing immediately:', relayoutData);
            return [
                relayoutData,
                'ALLOWED range change: ' + JSON.stringify(relayoutData)
            ];
        }
        
        // Other events pass through
        console.log('Other relayout - allowing:', relayoutData);
        return [
            relayoutData,
            'ALLOWED other relayout: ' + JSON.stringify(relayoutData)
        ];
    }
    """,
    [Output('dummy-output', 'children'), Output('debug-output', 'children')],
    Input('main-graph', 'relayoutData'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    print("Testing clientside callback solution...")
    print("1. Open http://127.0.0.1:8060/")
    print("2. Try scroll zoom - should be smoother")
    print("3. Watch debug output to see what events are blocked")
    
    app.run(debug=True, use_reloader=False, threaded=False, port=8060)
