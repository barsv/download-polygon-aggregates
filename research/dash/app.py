# app.py
# pip install dash==2.* plotly==5.* pandas numpy plotly-resampler==0.9.*
import pandas as pd
import numpy as np
from datetime import timedelta
import os

from dash import Dash, dcc, html, Input, Output, State, dash_table
import plotly.graph_objects as go
import plotly.express as px
import dash

# Plotly-resampler imports (required)
from plotly_resampler import FigureResampler, FigureWidgetResampler, register_plotly_resampler
from plotly_resampler.aggregation import MinMaxLTTB

from research.data_downloader import get_filename

# ---------- Load your data ----------
ticker = 'AAPL'
interval = '5s'
year = '2024'
pwd = os.path.dirname(os.path.abspath(__file__))
filename = get_filename(ticker, interval, year)
bars = pd.read_parquet(f'{pwd}/../{filename}')
bars['timestamp'] = pd.to_datetime(bars['timestamp'], unit='s')
# bars = pd.read_csv("bars.csv", parse_dates=["timestamp"]).sort_values("timestamp")
trades = pd.read_csv(f"{pwd}/trades.csv", parse_dates=["entry_ts", "exit_ts"]).sort_values("entry_ts")

# Precompute equity curve per params_hash/stop_loss if you want:
def make_equity(df_trades):
    eq = df_trades[["exit_ts","pnl"]].copy()
    eq = eq.rename(columns={"exit_ts":"ts"})
    eq["equity"] = eq["pnl"].cumsum()
    return eq

params_options = sorted(trades["params_hash"].astype(str).unique().tolist())
stoploss_options = sorted(trades["stop_loss"].unique().tolist())

# ---------- App ----------
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Backtest Viewer"

app.layout = html.Div(
    style={"fontFamily":"system-ui", "margin":"16px"},
    children=[
        html.H2("Backtest Viewer"),
        html.Div([
            html.Div([
                html.Label("Params:"),
                dcc.Dropdown(
                    id="params_dd", options=[{"label":p, "value":p} for p in params_options],
                    value=params_options[0] if params_options else None, clearable=False
                ),
            ], style={"flex":"1"}),
            html.Div([
                html.Label("Stop-loss:"),
                dcc.Dropdown(
                    id="stoploss_dd", options=[{"label":str(s), "value":s} for s in stoploss_options],
                    value=stoploss_options[0] if stoploss_options else None, clearable=False
                ),
            ], style={"flex":"1"}),
            html.Div([
                html.Label("Side:"),
                dcc.Dropdown(
                    id="side_dd",
                    options=[
                        {"label":"All","value":"ALL"},
                        {"label":"Long","value":"LONG"},
                        {"label":"Short","value":"SHORT"} ],
                    value="ALL", clearable=False
                ),
            ], style={"flex":"1"}),
        ], style={
            "display":"flex",
            "gap":"12px",
            "alignItems":"flex-end",
            "marginBottom":"12px",
            "flexWrap":"wrap"
            }),

        dcc.Tabs(id="tabs", value="tab-price", children=[
            dcc.Tab(label="Price & Trades", value="tab-price"),
            dcc.Tab(label="Equity", value="tab-equity"),
            dcc.Tab(label="Distributions", value="tab-dist"),
        ]),

        html.Div(id="tab-content"),

        html.Hr(),
        html.H4("Trades"),
        dash_table.DataTable(
            id='trades_table',
            columns=[
                {"name":"trade_id","id":"trade_id"},
                {"name":"side","id":"side"},
                {"name":"entry_ts","id":"entry_ts"},
                {"name":"entry_price","id":"entry_price","type":"numeric","format": {"specifier":".5f"}},
                {"name":"exit_ts","id":"exit_ts"},
                {"name":"exit_price","id":"exit_price","type":"numeric","format": {"specifier":".5f"}},
                {"name":"pnl","id":"pnl","type":"numeric","format": {"specifier":".2f"}},
                {"name":"pnl_pct","id":"pnl_pct","type":"numeric","format": {"specifier":".2%"}},
                {"name":"stop_loss","id":"stop_loss"},
                {"name":"duration_s","id":"duration_s"}
            ],
            page_size=12,
            filter_action="native",
            sort_action="native",
            row_selectable="single",
            style_table={"overflowX":"auto"},
            style_cell={"fontFamily":"monospace", "fontSize":"12px"},
        ),
        dcc.Store(id="current_zoom"),
    ]
)

# ---------- Helpers ----------
def filter_trades(params_hash, stop_loss, side):
    df = trades
    if params_hash is not None:
        df = df[df["params_hash"].astype(str)==str(params_hash)]
    if stop_loss is not None:
        df = df[df["stop_loss"]==stop_loss]
    if side == "LONG":
        df = df[df["side"].str.lower()=="long"]
    elif side == "SHORT":
        df = df[df["side"].str.lower()=="short"]
    return df.copy()

def price_figure(bars_slice, trades_slice):
    # Use FigureResampler for large datasets
    fig = FigureResampler(
        go.Figure(),
        default_n_shown_samples=1000,  # Show max 1000 points initially
        default_downsampler=MinMaxLTTB(parallel=True)  # Use efficient downsampling
    )
    
    # For very large datasets, use close price as line chart
    if len(bars_slice) > 10000:
        fig.add_trace(
            go.Scattergl(
                x=bars_slice["timestamp"], 
                y=bars_slice["close"],
                mode="lines",
                name="Close Price",
                line=dict(width=1)
            ),
            hf_x=bars_slice["timestamp"],
            hf_y=bars_slice["close"]
        )
    else:
        # For smaller datasets, use candlestick with resampling
        fig.add_trace(
            go.Candlestick(
                x=bars_slice["timestamp"], 
                open=bars_slice["open"],
                high=bars_slice["high"], 
                low=bars_slice["low"], 
                close=bars_slice["close"],
                name="Price", 
                showlegend=False
            )
        )
    
    # Add trade markers (these are usually much fewer points)
    if not trades_slice.empty:
        fig.add_trace(go.Scattergl(
            x=trades_slice["entry_ts"], y=trades_slice["entry_price"],
            mode="markers", name="Entry",
            marker=dict(symbol="triangle-up", size=12),
            text=trades_slice["trade_id"].astype(str),
            hovertemplate="Entry %{y:.5f}<br>%{x}<br>trade=%{text}<extra></extra>",
        ))
        color = np.where(trades_slice["pnl"]>=0, "green", "red")
        fig.add_trace(go.Scattergl(
            x=trades_slice["exit_ts"], y=trades_slice["exit_price"],
            mode="markers", name="Exit",
            marker=dict(symbol="x", size=12, color=color),
            text=trades_slice["pnl"].round(2).astype(str),
            hovertemplate="Exit %{y:.5f}<br>%{x}<br>pnl=%{text}<extra></extra>",
        ))
    
    fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), height=520, xaxis_rangeslider_visible=False)
    return fig

def equity_figure(df_trades):
    if df_trades.empty:
        return go.Figure()
    eq = make_equity(df_trades)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=eq["ts"], y=eq["equity"], mode="lines", name="Equity"))
    fig.update_layout(margin=dict(l=0,r=0,t=10,b=0), height=420)
    return fig

def distributions_figure(df_trades):
    if df_trades.empty:
        return html.Div("No trades for selection.")
    fig1 = px.histogram(df_trades, x="pnl", nbins=60, title="PnL distribution")
    fig1.update_layout(margin=dict(l=0,r=0,t=30,b=0), height=300)
    fig2 = px.histogram(df_trades, x="duration_s", nbins=60, title="Duration (s)")
    fig2.update_layout(margin=dict(l=0,r=0,t=30,b=0), height=300)
    fig3 = px.violin(df_trades, y="pnl", color="side", box=True, points=False, title="PnL by side")
    fig3.update_layout(margin=dict(l=0,r=0,t=30,b=0), height=300)
    return html.Div([dcc.Graph(figure=fig1), dcc.Graph(figure=fig2), dcc.Graph(figure=fig3)])

# ---------- Callbacks ----------
@app.callback(
    Output("tab-content","children"),
    Output("trades_table","data"),
    Input("tabs","value"),
    Input("params_dd","value"),
    Input("stoploss_dd","value"),
    Input("side_dd","value"),
    State("current_zoom","data"),
)
def render_tab(tab, params_hash, stop_loss, side, zoom):
    df_tr = filter_trades(params_hash, stop_loss, side)
    if tab == "tab-price":
        if zoom and "x0" in zoom and "x1" in zoom:
            mask = (bars["timestamp"]>=zoom["x0"]) & (bars["timestamp"]<=zoom["x1"])
            bars_slice = bars.loc[mask]
            df_show = df_tr[(df_tr["entry_ts"]<=zoom["x1"]) & (df_tr["exit_ts"]>=zoom["x0"])]
        else:
            # if not df_tr.empty:
            #     x0 = df_tr["entry_ts"].min() - timedelta(minutes=15)
            #     x1 = df_tr["exit_ts"].max() + timedelta(minutes=15)
            #     mask = (bars["timestamp"]>=x0) & (bars["timestamp"]<=x1)
            #     bars_slice = bars.loc[mask]
            # else:
            #     bars_slice = bars
            bars_slice = bars
            df_show = df_tr
        fig = price_figure(bars_slice, df_show)
        graph = dcc.Graph(id="price_graph", figure=fig, clear_on_unhover=True)
        return graph, df_tr.to_dict("records")
    elif tab == "tab-equity":
        fig = equity_figure(df_tr)
        return dcc.Graph(figure=fig), df_tr.to_dict("records")
    else:
        content = distributions_figure(df_tr)
        return content, df_tr.to_dict("records")

@app.callback(
    Output("current_zoom","data"),
    Input("price_graph","relayoutData"),
    prevent_initial_call=True
)
def keep_zoom(relayout):
    if not relayout:
        return dash.no_update
    x0 = relayout.get("xaxis.range[0]")
    x1 = relayout.get("xaxis.range[1]")
    if x0 and x1:
        return {"x0":x0, "x1":x1}
    return dash.no_update

@app.callback(
    Output("price_graph","figure"),
    Input("trades_table","selected_rows"),
    State("trades_table","data"),
    State("params_dd","value"),
    State("stoploss_dd","value"),
    State("side_dd","value"),
    prevent_initial_call=True
)
def focus_on_trade(selected_rows, table_data, params_hash, stop_loss, side):
    if not selected_rows:
        return dash.no_update
    row = table_data[selected_rows[0]]
    entry = pd.to_datetime(row["entry_ts"])
    exit_ = pd.to_datetime(row["exit_ts"])
    pad = (exit_ - entry) * 0.5 if exit_>entry else pd.Timedelta(minutes=10)
    x0, x1 = entry - pad, exit_ + pad
    mask = (bars["timestamp"]>=x0) & (bars["timestamp"]<=x1)
    bars_slice = bars.loc[mask]
    df_tr = filter_trades(params_hash, stop_loss, side)
    df_show = df_tr[(df_tr["entry_ts"]<=x1) & (df_tr["exit_ts"]>=x0)]
    fig = price_figure(bars_slice, df_show)
    fig.add_vrect(x0=entry, x1=exit_, fillcolor="rgba(0,0,0,0.04)", line_width=0)
    return fig

# Register plotly-resampler callback for handling zoom/pan events
register_plotly_resampler(app)

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except AttributeError:
        app.run_server(debug=True)
