"""404 Page for Application.

This is the 404 Page for the application
"""
from dash import html
import dash


dash.register_page(__name__)


def layout() -> html.Div:
    """Returns the layout for the not found page

    :return: The HTML.DIV for the not found page
    :rtype: html.Div
    """
    return html.H1("This is our custom 404 content")
