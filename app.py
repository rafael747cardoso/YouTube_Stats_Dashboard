
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Paths:
path_data = "data/"
path_assets = "assets/"

# Packages:
import numpy as np
import pandas as pd
import datatable as dt
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import operator
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from funcs.ui_table import tab_table



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
ops = {
    ">=": operator.ge,
    ">": operator.gt,
    "==": operator.eq,
    "<": operator.lt,
    "<=": operator.le
}





#----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ##########################################################

app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ##########################################################

###### Exploratory Data Analysis

### Table

# Update the options for the channel filter:
@app.callback(
    Output(component_id = "table_filter_cat_var_value", component_property = "options"),
    [Input(component_id = "table_filter_cat_var_name", component_property = "value")]
)
def update_select_filter_cat(table_filter_cat_var_name):
    opt0 = [{"label": "", "value": ""}]
    if table_filter_cat_var_name in df_airplanes.columns:
        opts = [{"label": l, "value": l} for l in df_airplanes[table_filter_cat_var_name].unique()]
    else:
        opts = [{"label": "", "value": ""}]
    return (opt0 + opts)

# Table with filters:
@app.callback(
    Output(component_id = "div_table", component_property = "children"),
    [Input(component_id = "table_filter_num_var_name", component_property = "value"),
     Input(component_id = "table_filter_num_operation", component_property = "value"),
     Input(component_id = "table_filter_num_var_value", component_property = "value"),
     Input(component_id = "table_filter_cat_var_name", component_property = "value"),
     Input(component_id = "table_filter_cat_var_value", component_property = "value")
     ]
)
def update_table(table_filter_num_var_name,
                 table_filter_num_operation,
                 table_filter_num_var_value,
                 table_filter_cat_var_name,
                 table_filter_cat_var_value):
    # Filters:
    df = df_videos.copy()
    if table_filter_num_var_name != "Variable" and \
            table_filter_num_operation != "Operator":
        op_func = ops[table_filter_num_operation]
        df = df[op_func(df[table_filter_num_var_name], table_filter_num_var_value)]
    if table_filter_cat_var_name != "Variable" and \
            table_filter_cat_var_value != "Levels" and \
            table_filter_cat_var_value != "":
        df = df[df[table_filter_cat_var_name] == table_filter_cat_var_value]
    df.columns = nice_names

    # Table:
    table = dash_table.DataTable(
        id = "table_data",
        columns = [{"name": c, "id": c} for c in df.columns],
        data = df.to_dict("records"),
        page_size = 18,
        style_as_list_view = True,
        style_header = {
            "backgroundColor": "rgb(30, 30, 30)"
        },
        style_cell = {
            "backgroundColor": "rgb(50, 50, 50)",
            "color": "white",
            "textAlign": "center"
        },
        style_cell_conditional = [
            {"if": {"column_id": ["Manufacturer Name",
                                  "Model Name"]},
             "textAlign": "left"}
        ],
        style_table = {
            "overflowX": "auto"
        }
    )
    return (table)


### Plots

# Barplot of the number of videos by channel:

# 1D histogram:

# 2D Density:

# Scatter with colors:

# Bubble with colors:

# Scatter to compare 2 channels:

# Correlation matrix:









#----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ###########################################################


# Layout:
app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.H2("YouTube Videos EDA",
                style = {"text-align": "center"}),
        html.Br(),
        html.Br(),
        dbc.Tabs(
            [
                dbc.Tab(
                    label = "Table",
                    children = tab_table(vars_poss_filter_num = vars_poss_filter_num,
                                         vars_poss_filter_cat = vars_poss_filter_cat,
                                         filter_operations_poss = filter_operations_poss)
                )#,
                # dbc.Tab(
                #     label = "Plots",
                #     children = tab_plots()
                # )
            ]
        )
    ],
    className = "main-div"
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

