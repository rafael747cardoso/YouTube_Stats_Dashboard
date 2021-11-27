
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
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
import operator
from dash import Dash, dcc, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import base64

# Modules:
from funcs.content_page_home import content_page_home
from funcs.content_page_table import content_page_table
from funcs.content_page_plots import content_page_plots
from funcs.nice_data_format import nice_data_format
from funcs.make_datatable import make_datatable


# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)


#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################

# Read the data:
df_videos = dt.fread(path_data + "videos_data.csv", sep = ";").to_pandas()

df_videos = df_videos[(df_videos["channel_title"] == "Mustard") |
                      (df_videos["channel_title"] == "Steve Cutts") |
                      (df_videos["channel_title"] == "Astrum")]


# Selects options:
vars_poss_filter_cat = [
    {"label": "Variable", "value": "Variable"},
    {"label": "Channel", "value": "channel_title"},
    {"label": "Video", "value": "video_title"}
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
channels = np.sort(df_videos["channel_title"].unique()).tolist()
opts_channel = [{"label": i, "value": i} for i in channels]
vars_names = dict([(i["label"], i["value"]) for i in vars_poss_filter_num[1:]])





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
@app.callback(
    Output(component_id = "table_filter_cat_var_value", component_property = "options"),
    [
        Input(component_id = "table_filter_cat_var_name", component_property = "value")
    ]
)
def update_select_filter_cat(table_filter_cat_var_name):
    opt0 = [{"label": "All", "value": "All"}]
    if table_filter_cat_var_name in df_videos.columns:
        opts = [{"label": l, "value": l} for l in df_videos[table_filter_cat_var_name].unique()]
    else:
        opts = [{"label": "", "value": ""}]
    return(opt0 + opts)

# Apply the filters on the table:
@app.callback(
    Output(component_id = "dataset_table", component_property = "children"),
    [
        Input(component_id = "bnt-apply-filters", component_property = "n_clicks")
    ],
    [
        State(component_id = "table_filter_cat_var_name", component_property = "value"),
        State(component_id = "table_filter_cat_var_value", component_property = "value"),
        State(component_id = "table_filter_num_var_name", component_property = "value"),
        State(component_id = "table_filter_num_operation", component_property = "value"),
        State(component_id = "table_filter_num_var_value", component_property = "value")
    ]
)
def update_table(n_clicks,
                 table_filter_cat_var_name,
                 table_filter_cat_var_value,
                 table_filter_num_var_name,
                 table_filter_num_operation,
                 table_filter_num_var_value):
    # Apply the filters:
    df = df_videos.copy()[cols_names]
    if table_filter_cat_var_name != "Variable" and \
       table_filter_cat_var_value != "All":
        df = df[df[table_filter_cat_var_name] == table_filter_cat_var_value]
    if table_filter_num_var_name != "Variable" and \
       table_filter_num_operation != "Operator":
        op_func = ops[table_filter_num_operation]
        df = df[op_func(df[table_filter_num_var_name], table_filter_num_var_value)]
    
    # Format the data for a nice view:
    nice_data_format(df = df,
                     nice_names = nice_names)

    # Table:
    table = make_datatable(df = df)
    return(table)

#################################################### Plots with filters

# Correlation Matrix:
@app.callback(
    Output(component_id = "plot_corr_matrix", component_property = "figure"),
    [
        Input(component_id = "plot_corr_matrix_chosen_channel", component_property = "value")
    ]
)
def update_corr_matrix(plot_corr_matrix_chosen_channel):
    
    # Data:
    df = df_videos.copy()[df_videos["channel_title"] == plot_corr_matrix_chosen_channel]
    df = df[list(vars_names.values())]
    corr_vals = df.corr()
    
    # Palette:
    n_colors = 100
    my_colors = ["#000000", "#E008F8", "#F81D08", "#F88A08", "#F7FE04"]
    cmap = LinearSegmentedColormap.from_list("my_palette", my_colors)
    my_palette = [to_hex(j) for j in [cmap(i / n_colors) for i in np.array(range(n_colors))]]

    # Plot:
    xy_names = list(vars_names.keys())
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
            paper_bgcolor = "rgba(0,0,0,0)",
            plot_bgcolor = "rgba(0,0,0,0)",
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
    return(fig)

# 1D Histogram:




# 2D Density:

# Scatter with colors:

# Bubble with colors:

# Scatter to compare 2 channels:










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
    dbc.Container(
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
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Home",
                                        href = "/",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Table:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(table_tab_image.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Table",
                                        href = "/page_table",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Plots:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(plots_tab_image.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Plots",
                                        href = "/page_plots",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    )
                ],
                navbar = True
            )
        ],
        class_name = "my-navbar"
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
    ]
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
        return content_page_table(vars_poss_filter_cat = vars_poss_filter_cat,
                                  vars_poss_filter_num = vars_poss_filter_num,
                                  filter_operations_poss = filter_operations_poss)
    elif pathname == "/page_plots":
        return content_page_plots(vars_poss_filter_cat = vars_poss_filter_cat,
                                  vars_poss_filter_num = vars_poss_filter_num,
                                  filter_operations_poss = filter_operations_poss,
                                  df_data = df_videos,
                                  opts_channel = opts_channel)







#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

run_vers = "dev"
# run_vers = "production"

if run_vers == "dev":
    app.run_server(debug = True)
if run_vers == "production":
    if __name__ == "__main__":
        app.run_server(debug = True)

