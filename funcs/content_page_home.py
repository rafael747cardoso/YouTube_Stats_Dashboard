
### Make the content for the home page

from dash import html
import dash_bootstrap_components as dbc
import base64

# Mosaic picture:
logo_filename = "home_pic.png"
encoded_image = base64.b64encode(open(logo_filename, "rb").read())

def content_page_home():
    
    pg = [
        html.Div(
            [
                # Videos covers picture:
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src = "data:image/png;base64,{}".format(encoded_image.decode()),
                                    height = "500px",
                                    className = "welcome-pic"
                                )
                            ]
                        )
                    ]
                ),
                # Welcome text:
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    "Here you will find the public data for 150.899 videos from 207 YouTube channels. " + \
                                    "Using this Dashboard you will be able to make various types of visualizations" + \
                                    " with diferent kinds of filters, producing your own unique insights " + \
                                    "over the channels listed in the dataset.",
                                    className = "welcome-text"
                                ),
                                html.Div(
                                    "For more information about the dataset go to:",
                                    className = "welcome-note"
                                ),
                                html.A(
                                    "https://www.kaggle.com/rafael747cardoso/datasets",
                                    href = "https://www.kaggle.com/rafael747cardoso/datasets",
                                    target = "_blank",
                                    className = "welcome-link"
                                ),
                                html.Br(),
                                html.Br(),
                                html.Div(" ")
                            ]
                        )
                    ]
                )
            ],
            className = "welcome-page"
        )
    ]
    
    return(pg)
    
