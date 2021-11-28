
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import skew


def make_2d_density(
        df_data,
        chosen_channel,
        chosen_xvar,
        chosen_yvar,
        vars_names
):
    """
    Make the 2D density plot.
    :param df_data:
    :param chosen_channel:
    :param chosen_xvar:
    :param chosen_yvar:
    :param vars_names:
    :return: fig
    """

    # Data:
    df = df_data.loc[df_data["channel_title"] == chosen_channel]
    x_vals = df[chosen_xvar]
    y_vals = df[chosen_yvar]
    
    # Palette:
    my_colors = ["#000000", "#E008F8", "#F81D08", "#F88A08", "#F7FE04"]

    # Plot:
    fig = go.Figure(
        data = [
            go.Histogram2dContour(
                x = x_vals,
                y = y_vals,
                colorscale = my_colors,
                ncontours = 10,
                histnorm = "probability density",
                colorbar = dict(
                    title = "<b>Density</b>"
                )
            )
        ],
        layout = go.Layout(
            xaxis = {
                "title": "<b>" + vars_names[chosen_xvar] + "</b>",
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
                "title": "<b>" + vars_names[chosen_yvar] + "</b>",
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
                "t": 70,
                "b": 20
            },
            showlegend = False,
            height = 600
        )
    )
    return (fig)


