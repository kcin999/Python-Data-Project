"""Home Page for Application.

This is the welcome page for the application.
This has information regarding the application and various navigation pieces.
"""
import dash
from dash import html


dash.register_page(__name__, path='/', redirect_from=['/home'])


def layout() -> html.Div:
    """Returns the layout for the home page

    :return: The HTML.DIV for the home page
    :rtype: html.Div
    """
    return html.Div(children=[
        html.H1(children='This is our Home page'),

        html.Div(children='''
        This is our Home page content.
    '''),

    ])
