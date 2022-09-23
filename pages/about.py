"""Home Page for Application.

This is the welcome page for the application.
This has information regarding the application and various navigation pieces.
"""
import dash
from dash import html


dash.register_page(__name__, path='/about', name="About")


def layout() -> html.Div:
    """Returns the layout for the about page

    :return: The HTML.DIV for the about page
    :rtype: html.Div
    """
    return html.Div(children=[
        html.H1(children='This is our About page'),

        html.Div(children='''
        This is our About page content.
    '''),

    ])
