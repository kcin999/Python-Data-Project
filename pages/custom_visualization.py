"""Custom visualization Page for Application.

This is the custom data visulazation page for the application.

The goal of this page is to let the user choose the x, y, and the type of chart they wish to see
"""
import re
import dash
from dash import dcc, Input, Output, State, ALL, html
import dash_bootstrap_components as dbc
import plotly.express as px

from database import database_functions

dash.register_page(__name__, path='/custom_visualization',
                   name="Custom Visualization")

chart_types = [
    {"label": "Bar Chart", "value": "bar_chart"},
    {"label": "Histogram", "value": "histogram"},
    {"label": "Pie Chart", "value": "pie_chart"},
    {"label": "Line Chart", "value": "line_chart"},
    {"label": "Scatter Chart", "value": "scatter_chart"}
]

dataset_options = [
    {"label": "Statcast (Baseball)", "value": "statcast"},
]


def filtering_layout() -> list:
    """Returns the contents of the data filtering section

    :return: A list containing all fo the filtering section details
    :rtype: list
    """
    return [
        html.P(
            "This is where we add filters to be applied to the chart"
        ),
        html.P(
            "Describe how the filter system is set up"
        ),
        dbc.Select(
            id="filter_column_selection"
        )
    ]


def user_chart_selection_inputs() -> dbc.Container:
    """Returns the container which holds all User Input HTML components

    :return: The container with all user input selections
    :rtype: dbc.Container
    """
    return dbc.Container([
        dbc.Row([
            dbc.Label("Dataset"),
            dbc.RadioItems(
                id="dataset_select",
                options=dataset_options,
                inline=True,
                value="statcast"
            )
        ]),
        dbc.Row([
            dbc.Label("Chart Type"),
            dbc.Select(
                id="chart_type_select",
                options=chart_types,
                value="scatter_chart"
            )
        ]),
        dbc.Row([
            dbc.Label("X Value / Grouping Value"),
            dbc.Select(
                id="x_selection",
                value="game_date"
            )
        ]),
        dbc.Row([
            dbc.Label("Y Value / Measuring Value"),
            dbc.Select(
                id="y_selection",
                value="release_speed"
            )
        ]),
        dbc.Row([
            dbc.Button(
                "Advanced Graph Settings",
                id="advanced-settings-button"
            )
        ]),
        dbc.Row([
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Advanced Settings")),
                    dbc.ModalBody(id="advanced-settings-modal-body"),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-advanced-settings-modal")
                    )
                ],
                id="advanced-settings-modal",
                is_open=False
            )
        ]),
        dbc.Row([
            dbc.Button(
                "Filters",
                id="filter-modal-button"
            )
        ]),
        dbc.Row([
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Filters")),
                    dbc.ModalBody(
                        filtering_layout(),
                        id="filter-modal-body"
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-filter-modal")
                    )
                ],
                id="filter-modal",
                is_open=False
            )
        ]),
        dbc.Row([
            dbc.Button("Update Graph", id="update-graph-button")
        ])
    ])


def layout() -> dbc.Container:
    """Returns the layout for the page

    :return: The HTML.DIV for the page
    :rtype: dbc.Container
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                [
                    user_chart_selection_inputs()
                ],
                width=6
            ),
            dbc.Col(
                width=6,
                id="graph_column"
            )
        ]
        )
    ])


@dash.callback(
    Output(component_id="graph_column", component_property="children"),
    Input(component_id="update-graph-button", component_property="n_clicks"),
    [
        State(component_id="dataset_select", component_property="value"),
        State(component_id="chart_type_select", component_property="value"),
        State(component_id="x_selection", component_property="value"),
        State(component_id="y_selection", component_property="value"),
        State(component_id={'type': 'advanced-settings',
              'input_value': ALL}, component_property="value")
    ]
)
def update_graph(_n1: int, _dataset: str, chart_type: str,
                 x_column: str, y_column: str, _advanced_settings: list) -> dcc.Graph:
    """Updates the graph on the page based on user inputs and selections

    :param _n1: Number of times that update graph has been clicked
    :type _n1: int

    :param _dataset: Which dataset that the user has selected.
    :type _dataset: str

    :param chart_type: Which chart type the user has selected
    :type chart_type: str

    :param x_column: Which value for x-axis the user has selected
    :type x_column: str

    :param y_column: Which value for y-axis the user has selected
    :type y_column: str

    :param _advanced_settings: All of the advanced setting values that the user has selected
    :type _advanced_settings: list

    :return: Returns the rendred graph, wrapped in a dcc.Graph
    :rtype: dcc.Graph
    """
    statcast = database_functions.Statcast()
    df = statcast.get_statcast_data_from_database()
    if chart_type == "bar_chart":
        fig = px.bar(df, x=x_column, y=y_column)
    elif chart_type == "histogram":
        fig = px.histogram(df, x=x_column)
    elif chart_type == "pie_chart":
        fig = px.pie(df, values=y_column, names=x_column)
    elif chart_type == "line_chart":
        fig = px.line(df, x=x_column, y=y_column)
    elif chart_type == "scatter_chart":
        fig = px.scatter(df, x=x_column, y=y_column)

    # Doing this to be able to associate a value with a specifc feature on the Plotly Chart
    states: dict = dash.callback_context.states

    for state, value in states.items():
        match_object = re.match(
            pattern=r'{"input_value":"([^0-9]*)","type":"([^0-9]*)"}.value',
            string=state
        )

        if match_object:
            layout_to_update = match_object.group(1)
            fig.update_layout(**{layout_to_update: value})

    return dcc.Graph(figure=fig)


@dash.callback(
    [
        Output('x_selection', 'options'),
        Output('y_selection', 'options'),
        Output('filter_column_selection', 'options')
    ],
    Input("dataset_select", "value")

)
def update_column_values(dataset: str) -> tuple[list, list, list]:
    """Returns the needed column values for x and y based on the selected dataset

    :param dataset: Which dataset that the user has selected.
    :type dataset: str

    :return: List of columns for both X and Y. It is the same list, just duplicated
    :rtype: tuple[list, list]
    """
    if dataset == 'statcast':
        statcast = database_functions.Statcast()
        columns = statcast.get_columns('Pitches')
    else:
        statcast = database_functions.Statcast()
        columns = statcast.get_columns('Pitches')

    selection_drop_down = []
    for item in columns:
        selection_drop_down.append({
            "label": item.replace('_', ' ').title(),
            "value": item
        })

    return (selection_drop_down,) * 3


@dash.callback(
    Output("advanced-settings-modal", "is_open"),
    [
        Input("advanced-settings-button", "n_clicks"),
        Input("close-advanced-settings-modal", "n_clicks")
    ],
    [State("advanced-settings-modal", "is_open")],
    prevent_initial_call=True
)
def toggle_advanced_settings_modal(_n: int, _n1: int, is_open: bool) -> bool:
    """Opens and closes the modal if button is pressed

    :param _n: Number of times the 'Advanced Graph Settings' button has been clicked
    :type _n: int

    :param _n1: Number of times the 'Close' Modal button has been clicked
    :type _n1: int

    :param is_open: State of the modal
    :type is_open: bool

    :return: Opposite of the is_open parameter
    :rtype: bool
    """
    return not is_open


@dash.callback(
    Output("filter-modal", "is_open"),
    [
        Input("filter-modal-button", "n_clicks"),
        Input("close-filter-modal", "n_clicks")
    ],
    [State("filter-modal", "is_open")],
    prevent_initial_call=True
)
def toggle_filter_modal(_n: int, _n1: int, is_open: bool) -> bool:
    """Opens and closes the modal if button is pressed

    :param _n: Number of times the 'Advanced Graph Settings' button has been clicked
    :type _n: int

    :param _n1: Number of times the 'Close' Modal button has been clicked
    :type _n1: int

    :param is_open: State of the modal
    :type is_open: bool

    :return: Opposite of the is_open parameter
    :rtype: bool
    """
    return not is_open


@dash.callback(
    Output(component_id='advanced-settings-modal-body',
           component_property='children'),
    Input(component_id='chart_type_select', component_property='value'),
    [
        State(component_id='x_selection', component_property='value'),
        State(component_id='y_selection', component_property='value')
    ]
)
def add_inputs_to_modal(chart_type: str, x_selection: str, y_selection: str) -> list:
    """This function updates the Modal elements based on what Chart Type is selected.
    This is used to have different advanced settings based on chart type

    :param chart_type: Which chart type the user has selected
    :type chart_type: str

    :param x_selection: What the user has selected for the X Value.

        * Used to update the value in the Modal

    :type x_selection: str

    :param y_selection: What the user has selected for the Y Value.

        * Used to update the value in the Modal

    :type y_selection: str

    :return: List of elements that are returned
    :rtype: list
    """
    universal_inputs = [
        dbc.Label("Title"),
        dbc.Input(
            id={
                "type": "advanced-settings",
                "input_value": "title"
            },
            placeholder='Title goes here...'
        )
    ]

    xy_chart_inputs = [
        dbc.Label("X Axis Label"),
        dbc.Input(
            id={
                "type": "advanced-settings",
                "input_value": "xaxis_title"
            },
            placeholder='X Axis Label Goes Here...',
            value=x_selection
        ),
        dbc.Label("Y Axis Label"),
        dbc.Input(
            id={
                "type": "advanced-settings",
                "input_value": "yaxis_title"
            },
            placeholder='Y Axis Label Goes Here...',
            value=y_selection
        )
    ]

    chart_specific_container = []
    if chart_type == "bar_chart":
        chart_specific_container = xy_chart_inputs + []
    elif chart_type == "histogram":
        chart_specific_container = [
        ]
    elif chart_type == "pie_chart":
        chart_specific_container = [
        ]
    elif chart_type == "line_chart":
        chart_specific_container = xy_chart_inputs + []
    elif chart_type == "scatter_chart":
        chart_specific_container = xy_chart_inputs + []

    return universal_inputs + chart_specific_container
