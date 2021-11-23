
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

def tab_table(vars_poss_filter_cat,
              vars_poss_filter_num,
              filter_operations_poss):
    """
    Makes the UI of the Table tab.
    :param filter_operations_poss:
    :param vars_poss_filter_cat:
    :param vars_poss_filter_num:
    :return: 
    """
    
    tab = html.Div(
        [
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H4("Filters"),
                                                    html.Br()
                                                ],
                                                width = 12
                                            )
                                        ]
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H4("Channel"),
                                                    html.Br()
                                                ],
                                                width = 6
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.Select(
                                                        id = "table_filter_cat_var_value",
                                                        options = [{"label": "", "value": ""}],
                                                        value = ""
                                                    )
                                                ],
                                                width = 6
                                            )
                                        ]
                                    )
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 12
                    )
                ]
            )
        ]
    )

    # tab = html.Div(
    #     [
    #         html.Br(),
    #         dbc.Row(
    #             [
    #                 dbc.Col(
    #                     [
    #                         dbc.Card(
    #                             [
    #                                 # Filters:
    #                                 dbc.Row(
    #                                     [
    #                                         # Numeric:
    #                                         dbc.Col(
    #                                             [
    #                                                 dbc.Card(
    #                                                     [
    #                                                         dbc.Row(
    #                                                             [
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         html.H4("Numeric Filter"),
    #                                                                         html.Br()
    #                                                                     ],
    #                                                                     width = 12
    #                                                                 ),
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         dbc.Select(
    #                                                                             id = "table_filter_num_var_name",
    #                                                                             options = vars_poss_filter_num,
    #                                                                             value = vars_poss_filter_num[0]["value"]
    #                                                                         )
    #                                                                     ],
    #                                                                     width = 5
    #                                                                 ),
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         dbc.Select(
    #                                                                             id = "table_filter_num_operation",
    #                                                                             options = filter_operations_poss,
    #                                                                             value = filter_operations_poss[0]["value"]
    #                                                                         )
    #                                                                     ],
    #                                                                     width = 3
    #                                                                 ),
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         dbc.Input(
    #                                                                             id = "table_filter_num_var_value",
    #                                                                             type = "number",
    #                                                                             value = 0
    #                                                                         )
    #                                                                     ],
    #                                                                     width = 4
    #                                                                 )
    #                                                             ]
    #                                                         )
    #                                                     ],
    #                                                     className = "plot-card",
    #                                                     inverse = True
    #                                                 )
    #                                             ],
    #                                             width = 6
    #                                         ),
    # 
    #                                         # Categoric:
    #                                         dbc.Col(
    #                                             [
    #                                                 dbc.Card(
    #                                                     [
    #                                                         dbc.Row(
    #                                                             [
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         html.H4("Categoric Filter"),
    #                                                                         html.Br()
    #                                                                     ],
    #                                                                     width = 12
    #                                                                 ),
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         dbc.Select(
    #                                                                             id = "table_filter_cat_var_name",
    #                                                                             options = vars_poss_filter_cat,
    #                                                                             value = vars_poss_filter_cat[0]["value"]
    #                                                                         )
    #                                                                     ],
    #                                                                     width = 6
    #                                                                 ),
    #                                                                 dbc.Col(
    #                                                                     [
    #                                                                         dbc.Select(
    #                                                                             id = "table_filter_cat_var_value",
    #                                                                             options = [{"label": "", "value": ""}],
    #                                                                             value = ""
    #                                                                         )
    #                                                                     ],
    #                                                                     width = 6
    #                                                                 )
    #                                                             ]
    #                                                         )
    #                                                     ],
    #                                                     className = "plot-card",
    #                                                     inverse = True
    #                                                 )
    #                                             ],
    #                                             width = 6
    #                                         )
    #                                     ]
    #                                 ),
    # 
    #                                 # Table:
    #                                 dbc.Row(
    #                                     [
    #                                         dbc.Col(
    #                                             [
    #                                                 html.Div(
    #                                                     id = "div_table",
    #                                                     children = "",
    #                                                     className = "table-data"
    #                                                 )
    #                                             ],
    #                                             width = 12
    #                                         )
    #                                     ]
    #                                 )
    #                             ],
    #                             className = "table-card",
    #                             inverse = True
    #                         )
    #                     ],
    #                     width = 12
    #                 )
    #             ]
    #         )
    #     ]
    # )

    return (tab)
