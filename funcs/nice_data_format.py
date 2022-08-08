
import numpy as np
import pandas as pd

def nice_data_format(df, nice_names):
    """
    Format the data for a nice view in the data_table.
    :param df:
    :param nice_names:
    :return: df_nice
    """

    extra_space = " | "
    if df.shape[0] > 0:
        # Character variables:
        vars_char = df.select_dtypes(exclude = [np.number]).columns.tolist()
        for var in vars_char:
            df[var] = df[var] + extra_space

        # Integer variables:
        vars_int = df.select_dtypes(include = [int]).columns.tolist()
        for var in vars_int:
            df[var] = df[var].apply(lambda x: str("{:,d}".format(x)) + extra_space)

        # Float variables:
        vars_float = df.select_dtypes(include = [float]).columns.tolist()
        for var in vars_float:
            var_min = min(df[var])
            if var_min > 0:
                decimals = int(round((abs(np.log10(min(df[var])))), 0))
            else:
                decimals = 3
            df[var] = df[var].apply(lambda x: str(str("{:,." + str(decimals) + "f}").format(x)) + extra_space)

    # Nice names:
    nice_header = [i + extra_space for i in nice_names]
    df.columns = nice_header
    df_nice = df.copy()
    
    return(df_nice)


