
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
from dash import Dash, dcc, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import base64
from funcs.content_page_home import content_page_home
from funcs.content_page_table import content_page_table
from funcs.content_page_plots import content_page_plots

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)


#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################

# Read the data:
df_videos = dt.fread(path_data + "videos_data.csv", sep = ";").to_pandas()

df_videos = df_videos[(df_videos["channel_title"] == "Mustard") | (df_videos["channel_title"] == "Steve Cutts")]


# Selects options:
vars_poss_filter_cat = [
    {"label": "Variable", "value": "Variable"},
    {"label": "Channel", "value": "channel_title"}
]
vars_poss_filter_num = [
    {"label": "Variable", "value": "Variable"},
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
filter_operations_poss = [
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
cols_names = [i["value"] for i in vars_poss_filter_cat[1:]] + [i["value"] for i in vars_poss_filter_num[1:]]
nice_names = [i["label"] for i in vars_poss_filter_cat[1:]] + [i["label"] for i in vars_poss_filter_num[1:]]




#----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ##########################################################

app = Dash(
    name = __name__,
    external_stylesheets = ["assets/bootstrap.css"],
    suppress_callback_exceptions = True
)
server = app.server

#----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ##########################################################

#################################################### Table

# Update the options for the categorical filter select:
# @app.callback(
#     Output(component_id = "table_filter_cat_var_value", component_property = "options"),
#     [
#         Input(component_id = "table_filter_cat_var_name", component_property = "value")
#     ]
# )
# def update_select_filter_cat(table_filter_cat_var_name):
#     opt0 = [{"label": "", "value": ""}]
#     if table_filter_cat_var_name in df_videos.columns:
#         opts = [{"label": l, "value": l} for l in df_videos[table_filter_cat_var_name].unique()]
#     else:
#         opts = [{"label": "", "value": ""}]
#     return(opt0 + opts)

# Apply the filters on the table:
# @app.callback(
#     Output(component_id = "dataset-table", component_property = "children"),
#     [
#         Input(component_id = "table_filter_cat_var_name", component_property = "value"),
#         Input(component_id = "table_filter_cat_var_value", component_property = "value"),
#         Input(component_id = "table_filter_num_var_name", component_property = "value"),
#         Input(component_id = "table_filter_num_operation", component_property = "value"),
#         Input(component_id = "table_filter_num_var_value", component_property = "value")
#      ]
# )
# def update_table(table_filter_cat_var_name,
#                  table_filter_cat_var_value,
#                  table_filter_num_var_name,
#                  table_filter_num_operation,
#                  table_filter_num_var_value):
#     # Filters:
#     df = df_videos.copy()[cols_names]
#     if table_filter_num_var_name != "Variable" and \
#        table_filter_num_operation != "Operator":
#         op_func = ops[table_filter_num_operation]
#         df = df[op_func(df[table_filter_num_var_name], table_filter_num_var_value)]
#     if table_filter_cat_var_name != "Variable" and \
#             table_filter_cat_var_value != "Levels" and \
#             table_filter_cat_var_value != "":
#         df = df[df[table_filter_cat_var_name] == table_filter_cat_var_value]
#     df.columns = nice_names
# 
#     # Table:
#     table = dash_table.DataTable(
#         id = "dataset-table",
#         columns = [{"name": c, "id": c} for c in df.columns],
#         data = df.to_dict("records"),
#         page_size = 18,
#         style_as_list_view = True,
#         style_header = {
#             "backgroundColor": "rgb(30, 30, 30)"
#         },
#         style_cell = {
#             "backgroundColor": "rgb(50, 50, 50)",
#             "color": "white",
#             "textAlign": "center"
#         },
#         style_cell_conditional = [
#             {"if": {"column_id": ["Manufacturer Name",
#                                   "Model Name"]},
#              "textAlign": "left"}
#         ],
#         style_table = {
#             "overflowX": "auto"
#         }
#     )
#     return (table)

# @app.callback(
#     Output(component_id = "test_output", component_property = "children"),
#     [
#         Input(component_id = "test_input", component_property = "value")
#     ]
# )
# def update_output(x):
#     y = x**2
#     return(y)

@app.callback(
    Output(component_id = "test_output", component_property = "children"),
    [
        Input(component_id = "bnt-apply-filters", component_property = "n_clicks"),
    ],
    State(component_id = "test_input", component_property = "value")
)
def update_output(n_clicks, x):
    y = x**2
    return(y)

    

# @app.callback(
#     Output(component_id = "dataset-table", component_property = "children"),
#     [
#         Input(component_id = "bnt-apply-filters", component_property = "n_clicks"),
#     ],
#     State(component_id = "table_filter_num_var_value", component_property = "value")
# )
# def update_table(n_clicks, table_filter_num_var_value):
#     # Apply the filters:
#     df = df_videos.copy()[cols_names]
#     df = df[df["views"] > table_filter_num_var_value]
#     
#     # Table:
#     table = dash_table.DataTable(
#         id = "dataset-table",
#         columns = [{"name": c, "id": c} for c in df.columns],
#         data = df.to_dict("records"),
#         page_size = 18,
#         style_as_list_view = True,
#         style_header = {
#             "backgroundColor": "rgb(30, 30, 30)"
#         },
#         style_cell = {
#             "backgroundColor": "rgb(50, 50, 50)",
#             "color": "white",
#             "textAlign": "center"
#         },
#         style_cell_conditional = [
#             {"if": {"column_id": ["Manufacturer Name",
#                                   "Model Name"]},
#              "textAlign": "left"}
#         ],
#         style_table = {
#             "overflowX": "auto"
#         }
#     )
#     return (table)



#################################################### Plots

# Barplot of the number of videos by channel:

# 1D Histogram:

# 2D Density:

# Scatter with colors:

# Bubble with colors:

# Scatter to compare 2 channels:

# Correlation matrix:









#----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ###########################################################

# Images for logo and tabs:
logo_filename = "dash_logo.png"
logo_image = base64.b64encode(open(logo_filename, "rb").read())
home_tab_filename = "home_tab.png"
home_tab_image = base64.b64encode(open(home_tab_filename, "rb").read())
table_tab_filename = "table_tab.png"
table_tab_image = base64.b64encode(open(table_tab_filename, "rb").read())
plots_tab_filename = "plots_tab.png"
plots_tab_image = base64.b64encode(open(plots_tab_filename, "rb").read())

# Content:
content = html.Div(
    children = [],
    id = "page-content"
)

# Top navbar:
top_navbar = dbc.Navbar(
    children = dbc.Container(
        [
            # Dashboard logo:
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src = "data:image/png;base64,{}".format(logo_image.decode()),
                                height = "60px"
                            )
                        )
                    ]
                )
            ),
            # Main navbar:
            dbc.Nav(
                [
                    # Home:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(home_tab_image.decode()),
                                    top = True,
                                    className = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Home",
                                        href = "/",
                                        active = "exact"
                                    ),
                                    className = "card-tab-body"
                                )
                            ],
                            className = "card-tab-icon"
                        )
                    ),
                    # Table:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(table_tab_image.decode()),
                                    top = True,
                                    className = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Table",
                                        href = "/page_table",
                                        active = "exact"
                                    ),
                                    className = "card-tab-body"
                                )
                            ],
                            className = "card-tab-icon"
                        )
                    ),
                    # Plots:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(plots_tab_image.decode()),
                                    top = True,
                                    className = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Plots",
                                        href = "/page_plots",
                                        active = "exact"
                                    ),
                                    className = "card-tab-body"
                                )
                            ],
                            className = "card-tab-icon"
                        )
                    )
                ],
                navbar = True
            )
        ],
        className = "my-navbar"
    ),
    color = "#0D0629"
)

# Layout:
app.layout = html.Div(
    [
        dcc.Location(
            id = "url"
        ),
        top_navbar,
        content
    ],
    className = "div-main"
)

# Make the pages:
@app.callback(
    Output(component_id = "page-content", component_property = "children"),
    [Input(component_id = "url", component_property = "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return content_page_home()
    elif pathname == "/page_table":
        return content_page_table(
        #     vars_poss_filter_cat = vars_poss_filter_cat,
        #     vars_poss_filter_num = vars_poss_filter_num,
        #     filter_operations_poss = filter_operations_poss
        )
    elif pathname == "/page_plots":
        return content_page_plots()







#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

run_vers = "dev"
# run_vers = "production"

if run_vers == "dev":
    app.run_server(debug = True)
if run_vers == "production":
    if __name__ == "__main__":
        app.run_server(debug = True)

