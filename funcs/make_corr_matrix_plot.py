
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go

def make_corr_matrix_plot(
        df_data,
        chosen_channel,
        vars_names_inv
):
    """
    Make the 1D hidtogram.
    :param df_data:
    :param chosen_channel:
    :param vars_names_inv:
    :return: fig
    """
    
    # Data:
    df = df_data.copy()[df_data["channel_title"] == chosen_channel]
    df = df[list(vars_names_inv.values())]
    corr_vals = df.corr()

    # Palette:
    n_colors = 100
    my_colors = ["#000000", "#E008F8", "#F81D08", "#F88A08", "#F7FE04"]
    cmap = LinearSegmentedColormap.from_list("my_palette", my_colors)
    my_palette = [to_hex(j) for j in [cmap(i / n_colors) for i in np.array(range(n_colors))]]

    # Plot:
    xy_names = list(vars_names_inv.keys())
    fig = go.Figure(
        data = [
            go.Heatmap(
                x = xy_names,
                y = xy_names,
                z = corr_vals,
                colorscale = my_palette,
                colorbar = dict(
                    title = "<b>Pearson correlation </b>"
                ),
                zmin = -1,
                zmax = 1,
                hovertemplate = "<b>" +
                                "%{x}<br>" +
                                "%{y}</br>" +
                                "Correlation: %{z:, }</b><extra></extra>"
            )
        ],
        layout = go.Layout(
            xaxis = {
                "title": "",
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
                "title": "",
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
            paper_bgcolor = "rgba(0, 0, 0, 0)",
            plot_bgcolor = "rgba(0, 0, 0, 0)",
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
    )
    return (fig)


