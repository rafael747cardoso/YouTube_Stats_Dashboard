
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Paths:
path_data = "data/"
path_assets = "assets/"
path_figs = "figs/"

# Packages:
import numpy as np
import pandas as pd
import datatable as dt
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import operator
import dash
from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import base64


# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)



#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################

# Read the data:
df_videos = dt.fread(path_data + "videos_data.csv", sep = ";").to_pandas()

# Selects options:
vars_cat_opts = [
    {"label": "Channel", "value": "channel_title"}
]
vars_num_opts = [
    {"label": "Views", "value": "views"},
    {"label": "Likes", "value": "likes"},
    {"label": "Dislikes", "value": "dislikes"},
    {"label": "Comments", "value": "comments"},
    {"label": "Age (days)", "value": "age_days"},
    {"label": "Likes/dislikes", "value": "likes_dislikes_ratio"},
    {"label": "Likes/views", "value": "likes_views_ratio"},
    {"label": "Dislikes/views", "value": "dislikes_views_ratio"},
    {"label": "Comments/views", "value": "comments_views_ratio"},
    {"label": "Comments/likes", "value": "comments_likes_ratio"},
    {"label": "Comments/dislikes", "value": "comments_dislikes_ratio"},
    {"label": "Mean views per day", "value": "mean_views_day"},
    {"label": "Mean likes per day", "value": "mean_likes_day"},
    {"label": "Mean dislikes per day", "value": "mean_dislikes_day"},
    {"label": "Mean comments per day", "value": "mean_comments_day"},
    {"label": "Mean likes/dislikes per day", "value": "mean_likes_dislikes_ratio_day"},
    {"label": "Mean likes/views per day", "value": "mean_likes_views_ratio_day"},
    {"label": "Mean dislikes/views per day", "value": "mean_dislikes_views_ratio_day"},
    {"label": "Mean comments/views per day", "value": "mean_comments_views_ratio_day"},
    {"label": "Mean comments/likes per day", "value": "mean_comments_likes_ratio_day"},
    {"label": "Mean comments/dislikes per day", "value": "mean_comments_dislikes_ratio_day"}
]
operations_opts = [
    {"label": "Operator", "value": "Operator"},
    {"label": ">=", "value": ">="},
    {"label": ">", "value": ">"},
    {"label": "==", "value": "=="},
    {"label": "<", "value": "<"},
    {"label": "<=", "value": "<="}
]
operations_funcs = {
    ">=": operator.ge,
    ">": operator.gt,
    "==": operator.eq,
    "<": operator.lt,
    "<=": operator.le
}





#----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ##########################################################

app = dash.Dash(
    name = __name__,
    external_stylesheets = ["assets/bootstrap.css"]
)
server = app.server

#----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ##########################################################

###### Exploratory Data Analysis

### Table



### Plots

# Barplot of the number of videos by channel:

# 1D Histogram:

# 2D Density:

# Scatter with colors:

# Bubble with colors:

# Scatter to compare 2 channels:

# Correlation matrix:









#----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ###########################################################

# Logo image:
logo_filename = "dash_logo.png"
encoded_image = base64.b64encode(open(logo_filename, "rb").read())

# Layout:
app.layout = html.Div(
    children = [
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(
                                        src = "data:image/png;base64,{}".format(encoded_image.decode()),
                                        height = "60px"
                                    )
                                )
                            ],
                            align = "left",
                            className = "g-0",
                        )
                    ),
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink("Table", href = "#")
                            ),
                            dbc.NavItem(
                                dbc.NavLink("Plots", href = "#")
                            )
                        ],
                        className = "ms-auto",
                        navbar = True
                    )
                ],
            ),
            color = "#0D0629",
            dark = True,
            className = "mb-5",
        )
    ],
    className = "div-main"
)



#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

run_vers = "dev"
# run_vers = "production"

if run_vers == "dev":
    app.run_server(debug = True)
if run_vers == "production":
    if __name__ == "__main__":
        app.run_server(debug = True)

