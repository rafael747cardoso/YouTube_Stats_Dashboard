
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
                        #################################### Plots without filters
                        
                        ### Barplot
                        
                        dbc.Tab(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.Spinner(
                                                            [
                                                                dcc.Graph(
                                                                    id = "plot_barplot",
                                                                    figure = make_barplot(df = df_data)
                                                                )
                                                            ],
                                                            color = "#a00710",
                                                            type = "border",
                                                            size = "md"
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
                        
                        #################################### Plots with filters
                        
                        ### Correlation matrix
                        
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
                                                                        dbc.Row(
                                                                            [
                                                                                dbc.Col(
                                                                                    [
                                                                                        html.Div(
                                                                                            "Channel",
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
                                                                                    width = 12
                                                                                )
                                                                            ]
                                                                        )
                                                                    ],
                                                                    width = 3
                                                                )
                                                            ]
                                                        ),
                                                        # Plot:
                                                        dbc.Row(
                                                            [
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Spinner(
                                                                            [
                                                                                dcc.Graph(
                                                                                    id = "plot_corr_matrix",
                                                                                    figure = {}
                                                                                )
                                                                            ],
                                                                            color = "#a00710",
                                                                            type = "border",
                                                                            size = "md"
                                                                        )
                                                                    ],
                                                                    width = 12
                                                                )
                                                            ],
                                                            class_name = "plot-row"
                                                        )
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
                        ),
                        
                        ### 1D Histogram

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
                                                                # Channel:
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Row(
                                                                            [
                                                                                dbc.Col(
                                                                                    [
                                                                                        html.Div(
                                                                                            "Channel",
                                                                                            className = "filter-title"
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                ),
                                                                                dbc.Col(
                                                                                    [
                                                                                        dbc.Select(
                                                                                            id = "plot_1d_histogram_chosen_channel",
                                                                                            options = opts_channel,
                                                                                            value = opts_channel[0]["value"]
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                )
                                                                            ]
                                                                        )
                                                                    ],
                                                                    width = 3
                                                                ),
                                                                # X variable:
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Row(
                                                                            [
                                                                                dbc.Col(
                                                                                    [
                                                                                        html.Div(
                                                                                            "X Variable",
                                                                                            className = "filter-title"
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                ),
                                                                                dbc.Col(
                                                                                    [
                                                                                        dbc.Select(
                                                                                            id = "plot_1d_histogram_chosen_xvar",
                                                                                            options = vars_poss_filter_num,
                                                                                            value = vars_poss_filter_num[1]["value"]
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                )
                                                                            ]
                                                                        )
                                                                    ],
                                                                    width = 3
                                                                ),
                                                                # Number of bins:
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Row(
                                                                            [
                                                                                dbc.Col(
                                                                                    [
                                                                                        html.Div(
                                                                                            "Bins",
                                                                                            className = "filter-title"
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                ),
                                                                                dbc.Col(
                                                                                    [
                                                                                        dbc.Input(
                                                                                            id = "plot_1d_histogram_chosen_bins",
                                                                                            type = "number",
                                                                                            value = 50,
                                                                                            min = 10,
                                                                                            max = 1000,
                                                                                            step = 10
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                )
                                                                            ]
                                                                        )
                                                                    ],
                                                                    width = 3
                                                                ),
                                                                # Range:
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Row(
                                                                            [
                                                                                dbc.Col(
                                                                                    [
                                                                                        html.Div(
                                                                                            "Range",
                                                                                            className = "filter-title"
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                ),
                                                                                dbc.Col(
                                                                                    [
                                                                                        # update_range_slider
                                                                                        # html.Div(
                                                                                        #     id = "",
                                                                                        #     children = ""
                                                                                        # )
                                                                                        dcc.RangeSlider(
                                                                                            id = "plot_1d_histogram_chosen_range",
                                                                                            min = 0,
                                                                                            max = 100000,
                                                                                            step = 500,
                                                                                            value = [10000, 50000],
                                                                                            tooltip = {
                                                                                                "placement": "bottom",
                                                                                                "always_visible": True
                                                                                            }
                                                                                        )
                                                                                    ],
                                                                                    width = 12
                                                                                )
                                                                            ]
                                                                        )
                                                                    ],
                                                                    width = 3
                                                                )
                                                            ]
                                                        ),
                                                        # Plot:
                                                        dbc.Row(
                                                            [
                                                                dbc.Col(
                                                                    [
                                                                        dbc.Spinner(
                                                                            [
                                                                                dcc.Graph(
                                                                                    id = "plot_1d_histogram",
                                                                                    figure = {}
                                                                                )
                                                                            ],
                                                                            color = "#a00710",
                                                                            type = "border",
                                                                            size = "md"
                                                                        )
                                                                    ],
                                                                    width = 12
                                                                )
                                                            ],
                                                            class_name = "plot-row"
                                                        )
                                                    ],
                                                    class_name = "card-container"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ],
                            label = "1D Histogram",
                            class_name = "tab-plot"
                        )
                                                
                        ### 2D Density
                        
                        
                        
                        ### Scatter with colors
                        
                        
                        
                        ### Bubble with colors
                        
                        
                        
                        ### Scatter to compare 2 channels
                        
                        
                        
                    ],
                    class_name = "tabs-row-plots"
                )
            ],
            className = "plots-page"
        )
    ]

    return (pg)

