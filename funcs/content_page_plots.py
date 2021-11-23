
### Make the content for the Plots page

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

def content_page_plots():
    
    pg = [
        html.Div(
            "Here goes the plots page",
            className = "welcome-page"
        )
    ]

    return (pg)

