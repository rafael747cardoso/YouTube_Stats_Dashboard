
from dash import dash_table

def make_datatable(df):
    """
    Make the data_table.
    :param df:
    :return: dt_table
    """
    dt_table = dash_table.DataTable(
        id = "dataset-table",
        columns = [
            {"name": c, "id": c} for c in df.columns
        ],
        data = df.to_dict("records"),
        page_size = 15,
        style_as_list_view = True,
        style_table = {
            "overflowX": "auto"
        },
        style_header = {
            "backgroundColor": "rgb(30, 30, 30)",
            "textAlign": "right"
        },
        style_cell = {
            "backgroundColor": "rgb(50, 50, 50)",
            "color": "white",
            "textAlign": "right"
        },
        style_cell_conditional = [
            {
                "if": {
                    "column_id": [
                        "Channel",
                        "Video"
                    ]
                },
                "textAlign": "left"
            }
        ]
    )
    return(dt_table)

