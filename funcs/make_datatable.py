
from dash import dash_table

def make_datatable(
        df_data,
        chosen_channel,
        num_var_name,
        num_operation,
        num_var_value,
        col_names,
        nice_names
):
    """
    Make the data_table.
    :param df_data:
    :param chosen_channel:
    :param num_var_name:
    :param num_operation:
    :param num_var_value:
    :param col_names:
    :param nice_names:
    :return: dt_table
    """

    # Apply the filters:
    df = df_data.copy()[cols_names]
    df = df[df["channel_title"] == chosen_channel]
    if num_var_name != "Variable" and \
            num_operation != "Operator":
        op_func = ops[num_operation]
        df = df[op_func(df[num_var_name], num_var_value)]

    # Format the data for a nice view:
    nice_data_format(df = df,
                     nice_names = nice_names)

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


