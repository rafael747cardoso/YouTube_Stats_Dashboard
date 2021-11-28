
from dash import html
import dash_bootstrap_components as dbc

def content_page_table(
        opts_channel,
        vars_poss_filter_num,
        filter_operations_poss
):
    """
    Make the content for the Table page.
    :param opts_channel:
    :param vars_poss_filter_num:
    :param filter_operations_poss:
    :return: pg
    """

    pg = [
        html.Div(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        # Filters:
                                        dbc.Row(
                                            [
                                                # Categoric:
                                                dbc.Col(
                                                    [
                                                        dbc.Card(
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
                                                                                    id = "table_chosen_channel",
                                                                                    options = opts_channel,
                                                                                    value = opts_channel[0]["value"]
                                                                                )
                                                                            ],
                                                                            width = 12
                                                                        )
                                                                    ]
                                                                )
                                                            ],
                                                            class_name = "card-container"
                                                        )
                                                    ],
                                                    width = 6
                                                ),
                                                # Numeric:
                                                dbc.Col(
                                                    [
                                                        dbc.Card(
                                                            [
                                                                dbc.Row(
                                                                    [
                                                                        dbc.Col(
                                                                            [
                                                                                html.Div(
                                                                                    "Numeric filter",
                                                                                    className = "filter-title"
                                                                                )
                                                                            ],
                                                                            width = 12
                                                                        ),
                                                                        dbc.Col(
                                                                            [
                                                                                dbc.Select(
                                                                                    id = "table_filter_num_var_name",
                                                                                    options = vars_poss_filter_num,
                                                                                    value = vars_poss_filter_num[0]["value"]
                                                                                )
                                                                            ],
                                                                            width = 6
                                                                        ),
                                                                        dbc.Col(
                                                                            [
                                                                                dbc.Select(
                                                                                    id = "table_filter_num_operation",
                                                                                    options = filter_operations_poss,
                                                                                    value = filter_operations_poss[0]["value"]
                                                                                )
                                                                            ],
                                                                            width = 3
                                                                        ),
                                                                        dbc.Col(
                                                                            [
                                                                                dbc.Input(
                                                                                    id = "table_filter_num_var_value",
                                                                                    type = "number",
                                                                                    value = 0
                                                                                )
                                                                            ],
                                                                            width = 3
                                                                        )
                                                                    ]
                                                                )
                                                            ],
                                                            class_name = "card-container"
                                                        )
                                                    ],
                                                    width = 6
                                                )
                                            ]
                                        ),
                                        # Button to run the filters:
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Button(
                                                            "Apply the filters",
                                                            id = "bnt-apply-filters",
                                                            class_name = "my-button",
                                                            n_clicks = 0
                                                        )
                                                    ],
                                                    width = 12,
                                                    class_name = "button-right-end"
                                                )
                                            ]
                                        ),
                                        # Table:
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Spinner(
                                                            [
                                                                html.Div(
                                                                    id = "dataset_table",
                                                                    children = "",
                                                                    className = "table-data"
                                                                )
                                                            ],
                                                            color = "#a00710",
                                                            type = "border",
                                                            size = "md"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ],
                                    class_name = "card-container"
                                )
                            ],
                            width = 12
                        )
                    ]
                )
            ],
            className = "table-page"
        )
    ]
    
    return(pg)

