# app.py
# pip install dash==2.* plotly==5.* pandas numpy plotly-resampler==0.9.*
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

from dash import Dash, dcc, html, Input, Output, State, dash_table
import plotly.graph_objects as go
import plotly.express as px
import dash

# Plotly-resampler imports (required)
from plotly_resampler import FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB

from research.data_downloader import get_filename

# ---------- Load your data ----------
ticker = 'AAPL'
interval = '5s'
year = '2024'
pwd = os.path.dirname(os.path.abspath(__file__))
filename = get_filename(ticker, interval, year)
bars = pd.read_parquet(f'{pwd}/../{filename}')
#bars = bars[:80000]
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

# Global resampler only used in 'line' mode; capped candles to keep UI responsive
current_resampler = None
# stores the current drag mode (zoom or pan). needed to keep it when switching between lines/candles.
current_dragmode = None
# how many candles do we allow to be shown. resampler works only with lines. hence i have to
# limit candles because currently there is no resampler for candles.
MAX_CANDLES = 5000

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
            html.Div([
                html.Label("Mode:"),
                dcc.RadioItems(
                    id="mode",
                    options=[
                        {"label": "Line", "value": "line"},
                        {"label": "Candles", "value": "candles"},
                    ],
                    value="line",
                    inline=True,
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
def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"{ts} {msg}")

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

def price_figure(bars_df, trades_df, mode="line"):
    """Minimal figure builder: 'line' uses FigureResampler; 'candles' uses Candlestick."""
    global current_resampler
    timestamps_np = bars_df["timestamp"].values # numby array to avoid datetime warning
    if mode == "candles":
        # for 'candles' there is no resampler.
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=timestamps_np, open=bars_df["open"], high=bars_df["high"],
            low=bars_df["low"], close=bars_df["close"], name="Price", showlegend=False
        ))
    else:
        # for 'lines' mode there is an automatic resampler that allows to render millions of points.
        fig = FigureResampler(
            default_n_shown_samples=1000,
            default_downsampler=MinMaxLTTB(parallel=False)
        )
        current_resampler = fig
        # Close, High, Low lines; all resampled
        fig.add_trace(
            go.Scattergl(mode="lines", name="Close", line=dict(width=1)),
            hf_x=timestamps_np, hf_y=bars_df["close"]
        )
        fig.add_trace(
            go.Scattergl(mode="lines", name="High", line=dict(width=1, color="gray")),
            hf_x=timestamps_np, hf_y=bars_df["high"]
        )
        fig.add_trace(
            go.Scattergl(mode="lines", name="Low", line=dict(width=1, color="gray")),
            hf_x=timestamps_np, hf_y=bars_df["low"]
        )
    if not trades_df.empty:
        entry_ts_np = trades_df["entry_ts"].values # numby array to avoid datetime warning
        fig.add_trace(go.Scattergl(
            x=entry_ts_np, y=trades_df["entry_price"], mode="markers", name="Entry",
            marker=dict(symbol="triangle-up", size=10)
        ))
        color = np.where(trades_df["pnl"]>=0, "green", "red")
        exit_ts_np = trades_df["exit_ts"].values # numby array to avoid datetime warning
        fig.add_trace(go.Scattergl(
            x=exit_ts_np, y=trades_df["exit_price"], mode="markers", name="Exit",
            marker=dict(symbol="x", size=10, color=color)
        ))

    fig.update_layout(
        # note: large margins to avoid jittering(jumping) while scroll-zooming.
        margin=dict(l=50,r=50,t=23,b=0), height=520, xaxis_rangeslider_visible=False,
        uirevision="price-graph", dragmode="pan",
        showlegend=False
    )
    fig.update_xaxes(
        tickformat='%H:%M\n%y-%m-%d',
        automargin=False, # force fixed margins to avoid jittering while scroll-zooming.
        # showticklabels=False,
        # tickangle=90,
    )
    fig.update_yaxes(
        automargin=False, # force fixed margins to avoid jittering while scroll-zooming.
        # showticklabels=False,
    )
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
    Output("mode","value"),
    Input("tabs","value"),
    Input("params_dd","value"),
    Input("stoploss_dd","value"),
    Input("side_dd","value"),
    Input("mode","value"),
    State("current_zoom","data"),
)
def render_tab(tab, params_hash, stop_loss, side, mode, zoom):
    global current_dragmode
    df_tr = filter_trades(params_hash, stop_loss, side)
    if tab == "tab-price":
        dragmode = current_dragmode if current_dragmode else 'pan'
        has_zoom = zoom and "x0" in zoom and "x1" in zoom
        # if there are too many points then force 'line' mode because there is no resampler for candles.
        if has_zoom:
            x0, x1 = pd.to_datetime(zoom["x0"]), pd.to_datetime(zoom["x1"])
            # log(f'render_tab: x0 = {x0}, x1 = {x1}')
            mask = (bars["timestamp"] >= x0) & (bars["timestamp"] <= x1)
            if mask.sum() > MAX_CANDLES:
                mode = "line"
        else:
            mode = "line"
        if has_zoom:
            # Filter trades to current window intersection so that auto-zoom for y-axis will work.
            df_show = df_tr[(df_tr["entry_ts"] <= x1) & (df_tr["exit_ts"] >= x0)]
        else:
            df_show = df_tr
        # log(f'render_tab: dragmode = {dragmode}, mode={mode}, x0={x0}, x1={x1}')
        if mode == "candles":
            if has_zoom:
                fig = price_figure(bars.loc[mask], df_show, mode="candles")
                fig.update_layout(xaxis_range=[x0, x1], dragmode=dragmode)
        else:
            # Line mode: preserve range when switching back using stored zoom
            if has_zoom:
                fig = price_figure(bars, df_show, mode="line")
                # need to fix y-range now. otherwise it's worng.
                mask = (bars["timestamp"] >= x0) & (bars["timestamp"] <= x1)
                bars_slice = bars.loc[mask]
                if not bars_slice.empty:
                    y_min = float(bars_slice["low"].min())
                    y_max = float(bars_slice["high"].max())
                    pad = (y_max - y_min) * 0.05 if y_max > y_min else 0.5
                    fig.update_layout(
                        xaxis_range=[x0, x1],
                        yaxis_range=[y_min - pad, y_max + pad],
                        yaxis_autorange=False,
                        dragmode=dragmode
                    )
                else:
                    fig.update_layout(xaxis_range=[x0, x1], dragmode=dragmode)
            else:
                fig = price_figure(bars, df_show, mode="line")
        graph = dcc.Graph(id="price_graph", figure=fig, clear_on_unhover=True,
                          config={ "scrollZoom": True })
        return graph, df_show.to_dict("records"), mode
    elif tab == "tab-equity":
        fig = equity_figure(df_tr)
        return dcc.Graph(figure=fig), df_tr.to_dict("records"), dash.no_update
    else:
        content = distributions_figure(df_tr)
        return content, df_tr.to_dict("records"), dash.no_update

@app.callback(
    Output("current_zoom","data"),
    Input("price_graph","relayoutData"),
    prevent_initial_call=True
)
def keep_zoom(relayout):
    ''' stores zoom and drag mode in global variables.
        needed to restore the sate when switching beween lines/candles.'''
    global current_dragmode
    if not relayout:
        return dash.no_update
    # log(f'keep_zoom: {[f"{k}={relayout[k]}" for k in relayout.keys()]}')
    if "dragmode" in relayout:
        current_dragmode = relayout["dragmode"]
    x0 = relayout.get("xaxis.range[0]")
    x1 = relayout.get("xaxis.range[1]")
    # log(f'keep_zoom: x0 = {x0}, x1 = {x1}')
    if x0 and x1:
        return {"x0":x0, "x1":x1}
    return dash.no_update

@app.callback(
    Output("price_graph", "figure", allow_duplicate=True),
    Input("price_graph", "relayoutData"),
    Input("tab-content", "children"),
    Input("mode", "value"),
    State("params_dd", "value"),
    State("stoploss_dd", "value"),
    State("side_dd", "value"),
    State("current_zoom", "data"),
    prevent_initial_call=True,
)
def update_fig(relayoutdata, _tab_children, mode, params_hash, stop_loss, side, zoom):
    global current_resampler, current_dragmode
    # If triggered by mode change to 'line' and we have a stored zoom, push a resampler patch
    if not relayoutdata:
        if mode == "line" and zoom and "x0" in zoom and "x1" in zoom and current_resampler is not None:
            # log(f'zoom["x0"] = {zoom["x0"]}, zoom["x1"] = {zoom["x1"]}')
            return current_resampler.construct_update_data_patch({
                "xaxis.range[0]": zoom["x0"],
                "xaxis.range[1]": zoom["x1"],
            })
        return dash.no_update

    # Only handle zoom/pan events
    if 'xaxis.range[0]' in relayoutdata and 'xaxis.range[1]' in relayoutdata:
        x_start = pd.to_datetime(relayoutdata['xaxis.range[0]'])
        x_end = pd.to_datetime(relayoutdata['xaxis.range[1]'])
        mask = (bars["timestamp"] >= x_start) & (bars["timestamp"] <= x_end)
        points_in_range = mask.sum()

        if mode == 'candles':
            # Candles: rebuild only if within limit
            if points_in_range == 0 or points_in_range > MAX_CANDLES:
                return dash.no_update
            df_tr = filter_trades(params_hash, stop_loss, side)
            # Filter trades to current window
            df_tr = df_tr[(df_tr["entry_ts"]<=x_end) & (df_tr["exit_ts"]>=x_start)]
            bars_slice = bars.loc[mask]
            new_fig = price_figure(bars_slice, df_tr, mode="candles")
            # Preserve ranges and drag mode
            y0 = relayoutdata.get('yaxis.range[0]')
            y1 = relayoutdata.get('yaxis.range[1]')
            dragmode = current_dragmode if current_dragmode else 'pan'
            # log(f'update_fig: dragmode = {dragmode}')
            new_fig.update_layout(
                xaxis_range=[x_start, x_end],
                yaxis_range=[y0, y1] if y0 and y1 else None,
                uirevision="price-graph",
                dragmode=dragmode,
            )
            return new_fig
        else:
            # Delegate to resampler
            if current_resampler is None:
                return dash.no_update
            return current_resampler.construct_update_data_patch(relayoutdata)

    # Not a range-change relayout; nothing to do
    return dash.no_update

if __name__ == "__main__":
    app.run(debug=True, threaded=False, dev_tools_hot_reload=False, use_reloader=False)
