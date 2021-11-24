
### Make the content for the Table page

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

def content_page_table(
        # vars_poss_filter_cat,
        # vars_poss_filter_num,
        # filter_operations_poss
):
    # """
    # Makes the UI of the Table tab.
    # :param vars_poss_filter_cat:
    # :param vars_poss_filter_num:
    # :param filter_operations_poss:
    # :return: 
    # """

    # pg = [
    #     html.Div(
    #         [
    #             html.Br(),
    #             dbc.Row(
    #                 [
    #                     dbc.Col(
    #                         [
    #                             dbc.Card(
    #                                 [
    #                                     # Filters:
    #                                     dbc.Row(
    #                                         [
    #                                             # Categoric:
    #                                             dbc.Col(
    #                                                 [
    #                                                     dbc.Card(
    #                                                         [
    #                                                             dbc.Row(
    #                                                                 [
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             html.Div(
    #                                                                                 "Categoric filter",
    #                                                                                 className = "filter-title"
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 12
    #                                                                     ),
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             dbc.Select(
    #                                                                                 id = "table_filter_cat_var_name",
    #                                                                                 options = vars_poss_filter_cat,
    #                                                                                 value = vars_poss_filter_cat[0]["value"]
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 6
    #                                                                     ),
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             dbc.Select(
    #                                                                                 id = "table_filter_cat_var_value",
    #                                                                                 options = [
    #                                                                                     {
    #                                                                                         "label": "",
    #                                                                                         "value": ""
    #                                                                                     }
    #                                                                                 ],
    #                                                                                 value = ""
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 6
    #                                                                     )
    #                                                                 ]
    #                                                             )
    #                                                         ],
    #                                                         className = "card-container"
    #                                                     )
    #                                                 ],
    #                                                 width = 6
    #                                             ),
    #                                             # Numeric:
    #                                             dbc.Col(
    #                                                 [
    #                                                     dbc.Card(
    #                                                         [
    #                                                             dbc.Row(
    #                                                                 [
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             html.Div(
    #                                                                                 "Numeric filter",
    #                                                                                 className = "filter-title"
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 12
    #                                                                     ),
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             dbc.Select(
    #                                                                                 id = "table_filter_num_var_name",
    #                                                                                 options = vars_poss_filter_num,
    #                                                                                 value = vars_poss_filter_num[0]["value"]
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 6
    #                                                                     ),
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             dbc.Select(
    #                                                                                 id = "table_filter_num_operation",
    #                                                                                 options = filter_operations_poss,
    #                                                                                 value = filter_operations_poss[0]["value"]
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 3
    #                                                                     ),
    #                                                                     dbc.Col(
    #                                                                         [
    #                                                                             dbc.Input(
    #                                                                                 id = "table_filter_num_var_value",
    #                                                                                 type = "number",
    #                                                                                 value = 0
    #                                                                             )
    #                                                                         ],
    #                                                                         width = 3
    #                                                                     )
    #                                                                 ]
    #                                                             )
    #                                                         ],
    #                                                         className = "card-container"
    #                                                     )
    #                                                 ],
    #                                                 width = 6
    #                                             )
    #                                         ]
    #                                     ),
    #                                     # Button to run the filters:
    #                                     dbc.Button(
    #                                         "Apply the filters",
    #                                         id = "bnt-apply-filters",
    #                                         className = "me-2",
    #                                         n_clicks = 0
    #                                     ),
    #                                     # Table:
    #                                     dbc.Row(
    #                                         [
    #                                             dbc.Col(
    #                                                 [
    #                                                     html.Div(
    #                                                         id = "dataset-table",
    #                                                         children = "",
    #                                                         className = "table-data"
    #                                                     )
    #                                                 ]
    #                                             )
    #                                         ]
    #                                     )
    #                                 ],
    #                                 className = "card-container",
    #                                 inverse = True
    #                             )
    #                         ],
    #                         width = 12
    #                     )
    #                 ]
    #             )
    #         ],
    #         className = "table-page"
    #     )
    # ]
    
    pg2 = html.Div(
        [
            dbc.Input(
                id = "test_input",
                type = "number",
                value = 10
            ),
            
            dbc.Button(
                "Apply the filters",
                id = "bnt-apply-filters",
                className = "me-2",
                n_clicks = 0
            ),
            
            html.Div(
                id = "test_output",
                children = ""
            )
        ]
    )
    
    return (pg2)

