"""Custom visualization Page for Application.

This is the custom data visulazation page for the application.

The goal of this page is to let the user choose the x, y, and the type of chart they wish to see
"""
import re
import dash
from dash import html, dcc, Input, Output, State, ALL, ctx
import dash_bootstrap_components as dbc
import plotly.express as px

from database.data_functions import get_columns, get_statcast_data

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


def user_chart_selection_inputs():
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
                "Advanced Settings",
                id="advanced-settings-button"
            )
        ]),
        dbc.Row([
            dbc.Collapse(
                id="advanced-settings-collapse",
                is_open=False
            )
        ]),
        html.Div(id="advanced-settings"),
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
def update_graph(_n1: int, dataset: str, chart_type: str, x_column: str, y_column: str, advanced_settings) -> dcc.Graph:
    df = get_statcast_data()
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
    ],
    Input("dataset_select", "value")

)
def update_column_values(dataset):
    if dataset == 'statcast':
        columns = get_columns('Pitches')
    else:
        columns = get_columns('Pitches')

    selection_drop_down = []
    for item in columns:
        selection_drop_down.append({
            "label": item.replace('_', ' ').title(),
            "value": item
        })

    return selection_drop_down, selection_drop_down


@dash.callback(
    Output("advanced-settings-collapse", "is_open"),
    [Input("advanced-settings-button", "n_clicks")],
    [State("advanced-settings-collapse", "is_open")],
    prevent_initial_callback=True
)
def toggle_collapse(_n, is_open):
    return not is_open


@dash.callback(
    Output(component_id='advanced-settings-collapse',
           component_property='children'),
    Input(component_id='chart_type_select', component_property='value')
)
def add_inputs_to_collapse(chart_type: str):
    if chart_type == "bar_chart":
        container = [
            dbc.Input(id={"type": "advanced-settings",
                      "input_value": "title"}, value='bar_chart')
        ]
    elif chart_type == "histogram":
        container = [
            dbc.Input(id={"type": "advanced-settings",
                      "input_value": "title"}, value='histogram')
        ]
    elif chart_type == "pie_chart":
        container = [
            dbc.Input(id={"type": "advanced-settings",
                      "input_value": "title"}, value='pie_chart')
        ]
    elif chart_type == "line_chart":
        container = [
            dbc.Input(id={"type": "advanced-settings",
                      "input_value": "title"}, value='line_chart')
        ]
    elif chart_type == "scatter_chart":
        container = [
            dbc.Input(id={"type": "advanced-settings",
                      "input_value": "title"}, value='scatter_chart')
        ]

    return container
