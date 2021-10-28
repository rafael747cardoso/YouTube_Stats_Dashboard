
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Packages:
import numpy as np
import pandas as pd
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

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)


#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################

# Read the data:
df_videos = pd.read_csv("data/videos_data.csv", sep = ",")





#----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ##########################################################

app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ##########################################################

###### Exploratory Data Analysis


# Scatter plot:
@app.callback(
    Output(component_id = "plot_scatter_eda", component_property = "figure"),
    [Input(component_id = "x_scatter_eda", component_property = "value"),
     Input(component_id = "y_scatter_eda", component_property = "value"),
     Input(component_id = "size_scatter_eda", component_property = "value"),
     Input(component_id = "color_scatter_eda", component_property = "value")]
)
def update_plot_scatter_eda(x_scatter_eda,
                            y_scatter_eda,
                            size_scatter_eda,
                            color_scatter_eda):
    plot_scatter_eda = px.scatter(
        data_frame = df_airplanes,
        x = x_scatter_eda,
        y = y_scatter_eda,
        size = size_scatter_eda,
        color = color_scatter_eda,
        custom_data = list(df_airplanes.columns),
        template = "plotly_dark",
        labels = axis_plots
    )
    plot_scatter_eda.update_traces(
        hovertemplate = custom_hovertemplate
    )
    return(plot_scatter_eda)


###### Table

# Update the options for the categorical filter select:
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
    df = df_airplanes.copy()
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





#----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ###########################################################


# Layout:
app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.H2("Trunfo Airplanes Dashboard",
                style = {"text-align": "center"}),
        html.Br(),
        html.Br(),
        dbc.Tabs(
            [
                dbc.Tab(
                    label = "Exploratory Data Analysis",
                    children = tab_explo_data_analysis(fastest = fastest,
                                                       heaviest = heaviest,
                                                       longest = longest,
                                                       most_potent = most_potent,
                                                       vars_poss_num = vars_poss_num,
                                                       vars_poss_cat = vars_poss_cat,
                                                       vars_poss_dens_cat = vars_poss_dens_cat,
                                                       funcs_pie_poss = funcs_pie_poss)
                ),
                dbc.Tab(
                    label = "Table",
                    children = tab_table(vars_poss_filter_num = vars_poss_filter_num,
                                         vars_poss_filter_cat = vars_poss_filter_cat,
                                         filter_operations_poss = filter_operations_poss)
                ),
                dbc.Tab(
                    label = "Machine Learning Model",
                    children = tab_ml_models(logit_predictors_poss = logit_predictors_poss)
                )
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





