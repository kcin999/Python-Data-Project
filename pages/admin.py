"""Admin Page for Application.

This page houses controls for any admin controlled priveledges,
as well as admin information regarding the application
"""
import datetime
import dash
from dash import html, dcc, Input, Output, State
from database import data_functions

dash.register_page(__name__, '/admin', title="Admin Page")


def layout() -> html.Div:
    """Returns the layout for the admin page

    :return: The HTML.DIV for the admin page
    :rtype: html.Div
    """
    return html.Div(children=[
        html.H1(children='This is our Admin Page'),
        dcc.DatePickerRange(
            id="data_range",
            month_format="M/D/Y",
            start_date=datetime.date.today() - datetime.timedelta(days=1),
            max_date_allowed=datetime.date.today(),
            end_date=datetime.date.today(),
            updatemode='bothdates'
        ),
        html.Button(id='add_data_submit', n_clicks=0, children='Update'),
        html.Div(id='add_data_output',
                 children='Enter a date range and press `Update`'),

        html.Button(id='add_players_submit',
                    n_clicks=0, children='Add Players'),
        html.Div(id='add_players_output',
                 children='Press Add Players to add all players to the database'),

        html.Button(id='delete_data', n_clicks=0, children='Delete'),
        html.Div(id='delete_data_output',
                 children='Delete data in the database')
    ])


@dash.callback(
    Output('add_data_output', 'children'),
    Input('add_data_submit', 'n_clicks'),
    State('data_range', 'start_date'),
    State('data_range', 'end_date'),
    prevent_initial_call=True
)
def add_statcast_data(_n_clicks: int, start_date: str, end_date: str) -> str:
    """Adds Statcast data based on the date range based in

    :param _n_clicks: Number of times that the button has been clicked.
        Not used. Just used to trigger the input
    :type _n_clicks: int

    :param start_date: Start of data range. Formatted as '%Y-%m-%d'
    :type start_date: str

    :param end_date: End of the data range. Formatted as '%Y-%m-%d'
    :type end_date: str

    :return: Message to display in the application
    :rtype: str
    """
    start_date_object = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date_object = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    data_functions.add_statcast_data(start_date_object, end_date_object)

    return f"Added data for the range {start_date} through {end_date}"


@dash.callback(
    Output('delete_data_output', 'children'),
    Input('delete_data', 'n_clicks'),
    prevent_inital_call=True
)
def delete_data(_n_clicks: int) -> str:
    """Deletes all data from the database

    :param _n_clicks: Number of times that the button has been clicked.
        Not used. Just used to trigger the input
    :type _n_clicks: int

    :return: Message to show in the application
    :rtype: str
    """
    data_functions.clear_statcast_data()
    return "Data Cleared"


@dash.callback(
    Output('add_players_output', 'children'),
    Input('add_players_submit', 'n_clicks'),
    prevent_inital_call=True
)
def add_player_data(_n_clicks: int) -> str:
    """Adds player data to the database

    :param _n_clicks: Number of times that the button has been clicked.
        Not used. Just used to trigger the input
    :type _n_clicks: int

    :return: Message to show in the application
    :rtype: str
    """
    data_functions.add_player_info()
    return "All Player Info Added"
