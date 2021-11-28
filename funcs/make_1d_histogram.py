
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import skew


def make_1d_histogram(
        df_data,
        chosen_channel,
        chosen_xvar,
        chosen_bins,
        chosen_range,
        vars_names
):
    """
    Make the 1D histogram plot.
    :param df_data:
    :param chosen_channel:
    :param chosen_xvar:
    :param chosen_bins:
    :param chosen_range:
    :param vars_names:
    :return: fig
    """
    
    # Data:
    x_vals = df_data.loc[df_data["channel_title"] == chosen_channel, chosen_xvar]

    # Limit the bins:
    if chosen_bins is None:
        chosen_bins = 10

    # Filter the range:
    x_vals = x_vals[(x_vals >= chosen_range[0]) & (x_vals <= chosen_range[1])]

    # Statistics:
    x_mean = np.mean(x_vals)
    x_median = np.median(x_vals)
    x_std = np.std(x_vals)
    x_skew = skew(x_vals)

    # Format the stats:

    # Plot:
    title_stats = "<b style = 'color: #c70039'>Mean</b>: " + f"{x_mean:.7g}      " + \
                  "<b style = 'color: #ffc300'>Median</b>: " + f"{x_median:.7g}      " + \
                  "<b>Standard deviation</b>: " + f"{x_std:.7g}      " + \
                  "<b>Skewness</b>: " + f"{x_skew:.3g}"
    fig = go.Figure(
        data = [
            go.Histogram(
                x = x_vals,
                histfunc = "count",
                nbinsx = chosen_bins,
                marker_color = "#00baad",
                opacity = 1
            )
        ],
        layout = go.Layout(
            shapes = [
                {
                    "line": {
                        "color": "#c70039",
                        "dash": "dash",
                        "width": 2
                    },
                    "type": "line",
                    "x0": x_mean,
                    "x1": x_mean,
                    "xref": "x",
                    "y0": 0,
                    "y1": 1,
                    "yref": "paper"
                },
                {
                    "line": {
                        "color": "#ffc300",
                        "dash": "dash",
                        "width": 2
                    },
                    "type": "line",
                    "x0": x_median,
                    "x1": x_median,
                    "xref": "x",
                    "y0": 0,
                    "y1": 1,
                    "yref": "paper"
                }
            ],
            title = title_stats,
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
                "title": "<b>Counts</b>",
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

    
    