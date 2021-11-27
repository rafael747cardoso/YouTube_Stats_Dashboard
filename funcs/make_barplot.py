
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go

def make_barplot(df):
    """
    Make the barplot.
    :param df:
    :return: fig
    """

    # Data:
    video_counts = df["channel_title"].value_counts()
    df_plot = pd.DataFrame(
        {
            "channel": video_counts.index.tolist(),
            "freq": video_counts.tolist()
        }
    )
    df_plot["freq_rel"] = [round(i / sum(df_plot["freq"]) * 100, 3) for i in df_plot["freq"]]
    df_plot["freq_rel_char"] = [str(i) + "%" for i in df_plot["freq_rel"]]

    # Palette:
    n_levels = df_plot.shape[0]
    cmap = LinearSegmentedColormap.from_list("my_palette", ["#111539", "#97A1D9"])
    my_palette = [to_hex(j) for j in [cmap(i / n_levels) for i in np.array(range(n_levels))]]

    # Plot:
    fig = px.bar(
        data_frame = df_plot,
        x = "channel",
        y = "freq",
        log_y = True,
        color = "channel",
        color_discrete_sequence = my_palette,
        text = "freq_rel_char"
    )
    fig.update_traces(
        textposition = "outside",
        hovertemplate = "<b>Channel: %{x}<br>Frequency: %{y:}</b><extra></extra>"
    )
    fig.update_layout(
        xaxis = {
            "title": "<b>Channel</b>",
            "titlefont": {
                "size": 20,
                "color": "white"
            },
            "tickfont": {
                "size": 18,
                "color": "white"
            },
            "gridcolor": "rgba(255, 255, 255, 0.3)"
        },
        yaxis = {
            "title": "<b>Number of Videos</b>",
            "titlefont": {
                "size": 20,
                "color": "white",
                "family": "Helvetica"
            },
            "tickfont": {
                "size": 18,
                "color": "white",
                "family": "Helvetica"
            },
            "gridcolor": "rgba(255, 255, 255, 0.3)"
        },
        font = {
            "size": 18,
            "color": "white",
                "family": "Helvetica"
        },
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        hoverlabel = {
            "font_size": 18,
            "font_family": "Helvetica"
        },
        margin = {
            "l": 20,
            "r": 20,
            "t": 50,
            "b": 20
        },
        showlegend = False,
        height = 600
    )
    
    return (fig)

