
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Paths:
path_data = "data/"
path_assets = "assets/"
path_figs = "figs/"

# Modules:
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
from scipy.stats import skew
from funcs.content_page_home import content_page_home
from funcs.content_page_table import content_page_table
from funcs.content_page_plots import content_page_plots
from funcs.nice_data_format import nice_data_format
from funcs.make_datatable import make_datatable
from funcs.make_corr_matrix_plot import make_corr_matrix_plot
from funcs.make_1d_histogram import make_1d_histogram
from funcs.make_2d_density import make_2d_density
from funcs.make_bubble import make_bubble
from funcs.make_scatter_2channels import make_scatter_2channels

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)

#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################

# Read the data:
df_videos = dt.fread(path_data + "videos_data.csv", sep = ";").to_pandas()

# Test sample:
# df_videos = df_videos[(df_videos["channel_title"] == "Mustard") |
#                       (df_videos["channel_title"] == "Steve Cutts") |
#                       (df_videos["channel_title"] == "Astrum")]

# Selects options:
vars_poss_filter_num = [
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
vars_poss_cat = [
    {"label": "Channel", "value": "channel_title"},
    {"label": "Video", "value": "video_title"}
]
cols_names = [i["value"] for i in vars_poss_cat] + [i["value"] for i in vars_poss_filter_num]
nice_names = [i["label"] for i in vars_poss_cat] + [i["label"] for i in vars_poss_filter_num]
channels = np.sort(df_videos["channel_title"].unique()).tolist()
opts_channel = [{"label": i, "value": i} for i in channels]
vars_names = dict([(i["value"], i["label"]) for i in vars_poss_filter_num])
vars_names_inv = dict([(i["label"], i["value"]) for i in vars_poss_filter_num])

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

# Apply the filters on the table:
@app.callback(
    Output(component_id = "dataset_table", component_property = "children"),
    [
        Input(component_id = "bnt-apply-filters", component_property = "n_clicks")
    ],
    [
        State(component_id = "table_chosen_channel", component_property = "value"),
        State(component_id = "table_filter_num_var_name", component_property = "value"),
        State(component_id = "table_filter_num_operation", component_property = "value"),
        State(component_id = "table_filter_num_var_value", component_property = "value")
    ]
)
def update_datatable(n_clicks,
                     table_chosen_channel,
                     table_filter_num_var_name,
                     table_filter_num_operation,
                     table_filter_num_var_value):
    return(make_datatable(df_data = df_videos,
                          chosen_channel = table_chosen_channel,
                          num_var_name = table_filter_num_var_name,
                          num_operation = table_filter_num_operation,
                          num_var_value = table_filter_num_var_value,
                          cols_names = cols_names,
                          nice_names = nice_names,
                          ops = ops))

#################################################### Plots

### Correlation Matrix

@app.callback(
    Output(component_id = "plot_corr_matrix", component_property = "figure"),
    [
        Input(component_id = "plot_corr_matrix_chosen_channel", component_property = "value")
    ]
)
def update_corr_matrix_plot(plot_corr_matrix_chosen_channel):
    return(make_corr_matrix_plot(df_data = df_videos, 
                                 chosen_channel = plot_corr_matrix_chosen_channel,
                                 vars_names_inv = vars_names_inv))

### 1D Histogram

# Update the range slider min:
@app.callback(
    Output(component_id = "plot_1d_histogram_chosen_range", component_property = "min"),
    [
        Input(component_id = "plot_1d_histogram_chosen_channel", component_property = "value"),
        Input(component_id = "plot_1d_histogram_chosen_xvar", component_property = "value")
    ]
)
def update_1d_histogram_range_min(chosen_channel,
                                  chosen_xvar):
    x_vals = df_videos.loc[df_videos["channel_title"] == chosen_channel, chosen_xvar]
    x_min = np.min(x_vals)
    return(x_min)

# Update the range slider max:
@app.callback(
    Output(component_id = "plot_1d_histogram_chosen_range", component_property = "max"),
    [
        Input(component_id = "plot_1d_histogram_chosen_channel", component_property = "value"),
        Input(component_id = "plot_1d_histogram_chosen_xvar", component_property = "value")
    ]
)
def update_1d_histogram_range_max(chosen_channel,
                                  chosen_xvar):
    x_vals = df_videos.loc[df_videos["channel_title"] == chosen_channel, chosen_xvar]
    x_max = np.max(x_vals)
    return(x_max)

# Update the range slider step:
@app.callback(
    Output(component_id = "plot_1d_histogram_chosen_range", component_property = "step"),
    [
        Input(component_id = "plot_1d_histogram_chosen_range", component_property = "min"),
        Input(component_id = "plot_1d_histogram_chosen_range", component_property = "max")
    ]
)
def update_1d_histogram_range_step(chosen_xmin,
                                   chosen_xmax):
    n_points = 1000
    step = (chosen_xmax - chosen_xmin)/n_points
    return(step)

# Update the range slider value:
@app.callback(
    Output(component_id = "plot_1d_histogram_chosen_range", component_property = "value"),
    [
        Input(component_id = "plot_1d_histogram_chosen_range", component_property = "min"),
        Input(component_id = "plot_1d_histogram_chosen_range", component_property = "max")
    ]
)
def update_1d_histogram_range_value(chosen_xmin,
                                    chosen_xmax):
    value = [chosen_xmin, chosen_xmax]
    return(value)

# Plot:
@app.callback(
    Output(component_id = "plot_1d_histogram", component_property = "figure"),
    [
        Input(component_id = "plot_1d_histogram_chosen_channel", component_property = "value"),
        Input(component_id = "plot_1d_histogram_chosen_xvar", component_property = "value"),
        Input(component_id = "plot_1d_histogram_chosen_bins", component_property = "value"),
        Input(component_id = "plot_1d_histogram_chosen_range", component_property = "value")
    ]
)
def update_1d_histogram(plot_1d_histogram_chosen_channel,
                        plot_1d_histogram_chosen_xvar,
                        plot_1d_histogram_chosen_bins,
                        plot_1d_histogram_chosen_range):
    return(make_1d_histogram(df_data = df_videos,
                             chosen_channel = plot_1d_histogram_chosen_channel,
                             chosen_xvar = plot_1d_histogram_chosen_xvar,
                             chosen_bins = plot_1d_histogram_chosen_bins,
                             chosen_range = plot_1d_histogram_chosen_range,
                             vars_names = vars_names))

### 2D Density

@app.callback(
    Output(component_id = "plot_2d_density", component_property = "figure"),
    [
        Input(component_id = "plot_2d_density_chosen_channel", component_property = "value"),
        Input(component_id = "plot_2d_density_chosen_xvar", component_property = "value"),
        Input(component_id = "plot_2d_density_chosen_yvar", component_property = "value")
    ]
)
def update_2d_density(plot_2d_density_chosen_channel,
                      plot_2d_density_chosen_xvar,
                      plot_2d_density_chosen_yvar):
    return(make_2d_density(df_data = df_videos, 
                           chosen_channel = plot_2d_density_chosen_channel,
                           chosen_xvar = plot_2d_density_chosen_xvar,
                           chosen_yvar = plot_2d_density_chosen_yvar,
                           vars_names = vars_names))

### Bubble with colors

@app.callback(
    Output(component_id = "plot_bubble", component_property = "figure"),
    [
        Input(component_id = "plot_bubble_chosen_channel", component_property = "value"),
        Input(component_id = "plot_bubble_chosen_xvar", component_property = "value"),
        Input(component_id = "plot_bubble_chosen_yvar", component_property = "value"),
        Input(component_id = "plot_bubble_chosen_sizevar", component_property = "value"),
        Input(component_id = "plot_bubble_chosen_colorvar", component_property = "value"),
    ]
)
def update_bubble(plot_bubble_chosen_channel,
                  plot_bubble_chosen_xvar,
                  plot_bubble_chosen_yvar,
                  plot_bubble_chosen_sizevar,
                  plot_bubble_chosen_colorvar):
    return(make_bubble(df_data = df_videos, 
                       chosen_channel = plot_bubble_chosen_channel,
                       chosen_xvar = plot_bubble_chosen_xvar,
                       chosen_yvar = plot_bubble_chosen_yvar,
                       chosen_sizevar = plot_bubble_chosen_sizevar,
                       chosen_colorvar = plot_bubble_chosen_colorvar,
                       vars_names = vars_names))

### Scatter to compare 2 channels

@app.callback(
    Output(component_id = "plot_scatter_2channels", component_property = "figure"),
    [
        Input(component_id = "plot_scatter_2channels_chosen_channel_1", component_property = "value"),
        Input(component_id = "plot_scatter_2channels_chosen_channel_2", component_property = "value"),
        Input(component_id = "plot_scatter_2channels_chosen_xvar", component_property = "value"),
        Input(component_id = "plot_scatter_2channels_chosen_yvar", component_property = "value")
    ]
)
def update_scatter_2channels(plot_scatter_2channels_chosen_channel_1,
                             plot_scatter_2channels_chosen_channel_2,
                             plot_scatter_2channels_chosen_xvar,
                             plot_scatter_2channels_chosen_yvar):
    return(make_scatter_2channels(df_data = df_videos, 
                                  chosen_channel_1 = plot_scatter_2channels_chosen_channel_1,
                                  chosen_channel_2 = plot_scatter_2channels_chosen_channel_2,
                                  chosen_xvar = plot_scatter_2channels_chosen_xvar,
                                  chosen_yvar = plot_scatter_2channels_chosen_yvar,
                                  vars_names = vars_names))

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
        return content_page_table(opts_channel = opts_channel,
                                  vars_poss_filter_num = vars_poss_filter_num,
                                  filter_operations_poss = filter_operations_poss)
    elif pathname == "/page_plots":
        return content_page_plots(vars_poss_filter_num = vars_poss_filter_num,
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

