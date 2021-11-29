
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import skew


def make_scatter_2channels(
        df_data,
        chosen_channel_1,
        chosen_channel_2,
        chosen_xvar,
        chosen_yvar,
        vars_names
):
    """
    Make the bubble plot with colors.
    :param df_data:
    :param chosen_channel_1:
    :param chosen_channel_2:
    :param chosen_xvar:
    :param chosen_yvar:
    :param vars_names:
    :return: fig
    """

    # Data:
    df1 = df_data.loc[df_data["channel_title"] == chosen_channel_1]
    x1_vals = df1[chosen_xvar]
    y1_vals = df1[chosen_yvar]
    df2 = df_data.loc[df_data["channel_title"] == chosen_channel_2]
    x2_vals = df2[chosen_xvar]
    y2_vals = df2[chosen_yvar]

    # Palette:
    my_colors = ["#2a7b9b", "#ff8d1a"]

    # Hover tamplate:
    custom_vars = list(vars_names.values())
    custom_template = "<b>Video title: %{text}<br>"
    for i in range(0, len(custom_vars)):
        custom_template += list(vars_names.values())[i] + ": %{customdata[" + str(i) + "]:}<br>"
    custom_template = custom_template + "</b><extra></extra>"

    # Plot:
    fig = go.Figure(
        data = [
            go.Scatter(
                x = x1_vals,
                y = y1_vals,
                mode = "markers",
                marker = {
                    "color": my_colors[0],
                    "size": 7
                },
                text = df1["video_title"],
                customdata = df1[list(vars_names.keys())],
                hovertemplate = custom_template,
                name = chosen_channel_1
            ),
            go.Scatter(
                x = x2_vals,
                y = y2_vals,
                mode = "markers",
                marker = {
                    "color": my_colors[1],
                    "size": 7
                },
                text = df2["video_title"],
                customdata = df2[list(vars_names.keys())],
                hovertemplate = custom_template,
                name = chosen_channel_2
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
            paper_bgcolor = "rgba(0, 0, 0, 0)",
            plot_bgcolor = "rgba(0, 0, 0, 0)",
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
            showlegend = True,
            height = 600
        )
    )
    return (fig)


