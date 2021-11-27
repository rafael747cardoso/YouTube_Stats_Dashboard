
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
        textfont_color = my_palette[n_levels // 2],
        textfont_size = 15,
        hovertemplate = "<b>Channel: %{x}<br>Frequency: %{y:}</b><extra></extra>"
    )
    fig.update_layout(
        xaxis_title = "<b>Channel</b>",
        yaxis_title = "<b>Number of Videos</b>",
        xaxis = dict(
            tickangle = 40
        ),
        font = dict(
            size = 18
        ),
        showlegend = False,
        plot_bgcolor = "#0d0629",
        hoverlabel = dict(
            font_size = 18,
            font_family = "Rockwell"
        ),
        margin = dict(
            l = 20,
            r = 20,
            t = 50,
            b = 20
        ),
        height = 600
    )
    
    return (fig)

