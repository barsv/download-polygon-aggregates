click_log = []
# !pip install scikit-learn pandas numpy plotly
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict
import pandas as pd


def get_pattern_info(sorted_results):
    pattern_info = []
    for i in range(len(sorted_results)):
        start_index = sorted_results[i][0]
        similar_count = sorted_results[i][1]
        pattern_info.append({
            'start_index': start_index,
            'similar_count': similar_count,
            'original_rank': i
        })
    return pattern_info


def extract_pattern_features(df, sorted_results, m=60):
    """
    Extract feature vectors for each pattern in sorted_results.
    Uses the actual pattern values as features.
    """
    patterns = []
    print(f"Extracting features for top {len(sorted_results)} patterns...")
    for i in range(len(sorted_results)):
        start_index = sorted_results[i][0]
        # Extract the pattern window
        pattern = df['open'].iloc[start_index:start_index + m].values
        # Normalize pattern (mean=0, std=1) for better comparison
        pattern_normalized = (pattern - pattern.mean()) / pattern.std()
        patterns.append(pattern_normalized)
    return np.array(patterns)


def handle_click(trace, points, state):
    global click_log
    for i in points.point_inds:
        record = {
            "index": i,
            "x": trace.x[i],
            "y": trace.y[i],
            "trace": trace,
            "custom": trace.customdata[i] if trace.customdata is not None else None
        }
        click_log.append(record)
        # from IPython.display import display
        # display(record)


def get_tsne(patterns):
    print("Computing t-SNE embedding...")
    # Apply t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(patterns)-1))
    tsne_coords = tsne.fit_transform(patterns)
    return tsne_coords


def visualize_clusters_tsne(tsne_coords, pattern_info, color):
    """
    Visualize clusters using t-SNE dimensionality reduction.
    """
    # Create DataFrame for plotting
    plot_data = pd.DataFrame({
        'x': tsne_coords[:, 0],
        'y': tsne_coords[:, 1],
        'start_index': [info['start_index'] for info in pattern_info],
        'similar_count': [info['similar_count'] for info in pattern_info],
        'rank': [info['original_rank'] for info in pattern_info],
        'max_pnl': [info['max_pnl'] for info in pattern_info],
        'max_pnl_index': [info['max_pnl_index'] for info in pattern_info],
        'sl': [info['sl'] for info in pattern_info],
        'side': [info['side'] for info in pattern_info],
    })
    # Create interactive plot
    fig_px = px.scatter(
        plot_data, 
        x='x', y='y', 
        color=color,
        hover_data=['start_index', 'similar_count', 'rank', 'max_pnl_index', 'max_pnl', 'sl', 'side'],
        # width=800,
        height=400
    )
    fig_px.update_traces(marker=dict(size=8, opacity=0.7))
    fig_px.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    figWidget = go.FigureWidget(fig_px)
    sc = figWidget.data[0]
    sc.on_click(handle_click)
    return plot_data, figWidget


def plot_window(starting_point):
    a = create_window(df, starting_point, m)
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=a))
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=400)
    fig.show()


def plot_selected():
    if len(click_log) > 0:
        last_click_log = click_log[-1]
        clicked_trace = last_click_log['trace']
        clicked_index = last_click_log['index']
        selected_staring_point = int(clicked_trace['customdata'][clicked_index][0])
        selected_similar_count = int(clicked_trace['customdata'][clicked_index][1])
        selected_rank = int(clicked_trace['customdata'][clicked_index][2])
        plot_window(selected_staring_point)
        print(f'starting point: {selected_staring_point}, similar count: {selected_similar_count}, rank: {selected_rank}')
    else:
        print('select a point on tSNE')