
# Packages:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc

# Modules:
from funcs.make_barplot import make_barplot

def content_page_plots(
        vars_poss_filter_cat,
        vars_poss_filter_num,
        filter_operations_poss,
        df_data,
        opts_channel
):
    """
    Make the content for the Plots page.
    :param vars_poss_filter_cat:
    :param vars_poss_filter_num:
    :param filter_operations_poss:
    :param df_data:
    :param opts_channel:
    :return: pg
    """
    
    pg = [
        html.Div(
            [
                # Tabs row for the different types of plot:
                dbc.Tabs(
                    [
                        ### Plots without filters
                        
                        # Barplot:
                        dbc.Tab(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dcc.Graph(
                                                            id = "plot_barplot",
                                                            figure = make_barplot(df = df_data)
                                                        )
                                                    ],
                                                    class_name = "card-container"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ],
                            label = "Barplot",
                            class_name = "tab-plot"
                        ),
                        
                        ### Plots with filters
                        
                        # Correlation matrix:
                        dbc.Tab(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        # Filters:
                                                        dbc.Row(
                                                            [
                                                                dbc.Col(
                                                                    [
                                                                        html.Div(
                                                                            "Choose the channel",
                                                                            className = "filter-title"
                                                                        )
                                                                    ],
                                                                    width = 12
                                                                ),
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Select(
                                                                            id = "plot_corr_matrix_chosen_channel",
                                                                            options = opts_channel,
                                                                            value = opts_channel[0]["value"]
                                                                        )
                                                                    ],
                                                                    width = 6
                                                                )
                                                            ]
                                                        ),
                                                        # Plot:
                                                        dbc.Row(
                                                            [
                                                                dbc.Col(
                                                                    [
                                                                        dcc.Graph(
                                                                            id = "plot_corr_matrix",
                                                                            figure = {"layout": {"height": 650}}
                                                                        )
                                                                    ],
                                                                    width = 12
                                                                )
                                                            ]
                                                        )
                                                        # dbc.Graph(
                                                        #     id = "plot_corr_matrix",
                                                        #     figure = ""
                                                        # )
                                                    ],
                                                    class_name = "card-container"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ],
                            label = "Correlation Matrix",
                            class_name = "tab-plot"
                        )
                        
                        # 1D Histogram:
                        
                        # 2D Density:
                        
                        # Scatter with colors:
                        
                        # Bubble with colors:
                        
                        # Scatter to compare 2 channels:
                        
                    ],
                    class_name = "tabs-row-plots"
                )
            ],
            className = "plots-page"
        )
    ]

    return (pg)

