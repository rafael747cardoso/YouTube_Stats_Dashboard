
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import skew

# Dynamic bubble size:
def size_func(s_vals):
    ref_size = max(s_vals)/(20**2)
    return(ref_size)

def make_bubble(
        df_data,
        chosen_channel,
        chosen_xvar,
        chosen_yvar,
        chosen_sizevar,
        chosen_colorvar,
        vars_names
):
    """
    Make the bubble plot with colors.
    :param df_data:
    :param chosen_channel:
    :param chosen_xvar:
    :param chosen_yvar:
    :param chosen_sizevar:
    :param chosen_colorvar:
    :param vars_names:
    :return: fig
    """
    
    # Data:
    df = df_data.loc[df_data["channel_title"] == chosen_channel]
    x_vals = df[chosen_xvar]
    y_vals = df[chosen_yvar]
    size_vals = df[chosen_sizevar]
    color_vals = df[chosen_colorvar]
    
    # Palette:
    n_colors = 100
    my_colors = ["#770484", "#E008F8", "#F81D08", "#F88A08", "#F7FE04"]
    cmap = LinearSegmentedColormap.from_list("my_palette", my_colors)
    my_palette = [to_hex(j) for j in [cmap(i / n_colors) for i in np.array(range(n_colors))]]
    
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
                x = x_vals,
                y = y_vals,
                mode = "markers",
                marker = {
                    "color": color_vals,
                    "colorscale": my_palette,
                    "showscale": True,
                    "colorbar": {
                        "title": "<b>" + vars_names[chosen_colorvar] + "</b>"
                    },
                    "size": size_vals,
                    "opacity": 0.9,
                    "sizemode": "area",
                    "sizeref": size_func(size_vals),
                    "sizemin": 2,
                    "line": {
                        "color": "rgba(0, 0, 0, 0)"
                    }
                },
                text = df["video_title"],
                customdata = df[list(vars_names.keys())],
                hovertemplate = custom_template
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
            showlegend = False,
            height = 600
        )
    )
    return (fig)


