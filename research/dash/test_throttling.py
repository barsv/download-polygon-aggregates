from dash import Dash, dcc, html, Input, Output, clientside_callback, State
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
    title="Throttled relayout events - should be smoother",
    margin=dict(l=0, r=0, t=30, b=0),  # Small margins
    height=520,
    xaxis_rangeslider_visible=False,
    dragmode='zoom',
    uirevision='main-graph'
)

app.layout = html.Div([
    html.H1("Throttling Solution for Jerky Scroll Zoom"),
    html.P([
        "Testing throttling approach: Limit relayout event frequency during scroll zoom."
    ]),
    
    dcc.Graph(
        id='main-graph',
        figure=fig_jerky,
        config={'scrollZoom': True}
    ),
    
    html.Div(id='debug-output', style={'margin': '20px', 'padding': '10px', 'background': '#f0f0f0'}),
    
    # Store for managing throttling state
    dcc.Store(id='throttle-store', data={'last_event_time': 0, 'throttle_ms': 100})
])

# Clientside callback with throttling
clientside_callback(
    """
    function(relayoutData, throttleState) {
        if (!relayoutData) {
            return [window.dash_clientside.no_update, throttleState, 'No relayout data'];
        }
        
        const now = Date.now();
        const lastEventTime = throttleState.last_event_time || 0;
        const throttleMs = throttleState.throttle_ms || 100;
        
        const timeSinceLastEvent = now - lastEventTime;
        
        console.log('Relayout event at', now, 'last was', lastEventTime, 'diff:', timeSinceLastEvent);
        
        // If too soon since last event, throttle it
        if (timeSinceLastEvent < throttleMs) {
            console.log('THROTTLED - too soon since last event');
            return [
                window.dash_clientside.no_update, 
                throttleState,
                'THROTTLED relayout (too soon: ' + timeSinceLastEvent + 'ms)'
            ];
        }
        
        // Update the last event time
        const newThrottleState = {
            ...throttleState,
            last_event_time: now
        };
        
        console.log('ALLOWED relayout:', relayoutData);
        return [
            relayoutData, 
            newThrottleState,
            'ALLOWED relayout at ' + now + ': ' + JSON.stringify(relayoutData)
        ];
    }
    """,
    [Output('main-graph', 'figure'), Output('throttle-store', 'data'), Output('debug-output', 'children')],
    Input('main-graph', 'relayoutData'),
    State('throttle-store', 'data'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    print("Testing throttling solution...")
    print("1. Open http://127.0.0.1:8061/")
    print("2. Try scroll zoom - should be smoother due to throttling")
    print("3. Watch debug output to see throttling in action")
    
    app.run(debug=True, use_reloader=False, threaded=False, port=8061)
