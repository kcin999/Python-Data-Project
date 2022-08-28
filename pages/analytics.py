import dash
from dash import html, dcc, Input, Output
from pybaseball import statcast
from pybaseball import cache
import plotly.express as px


cache.enable()

dash.register_page(__name__, '/analytics')


layout = html.Div(children=[
    html.H1(children='This is our Analytics page'),
    dcc.DatePickerRange(
        id="DataRange",
        month_format="Y/M/D"
    ),
    dcc.Graph(
        id='pitch-count-bar'
    )
])


@dash.callback(
    Output('pitch-count-bar', 'figure'),
    Input('DataRange', 'start_date'),
    Input('DataRange', 'end_date'))
def get_new_data(start_date, end_date):
    dataframe = statcast(start_date, end_date, parallel=False)

    agg = dataframe.groupby('pitch_name').count().reset_index()
    agg.to_csv('agg.csv')

    fig = px.bar(agg, x="pitch_name", y="game_date", barmode="group")

    return fig
