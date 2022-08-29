import dash
from dash import html, dcc, Input, Output
from pybaseball import statcast
from pybaseball import cache
import plotly.express as px
import datetime


cache.enable()

dash.register_page(__name__, '/daily-analytics', title="Daily Analytics")


layout = html.Div(children=[
    html.H1(children='This is our Daily Analytics page'),
    dcc.DatePickerSingle(
        id="DataRange",
        month_format="M/D/Y",
        placeholder="M/D/Y",
        date=datetime.date.today() - datetime.timedelta(days=1),
    ),
    dcc.Graph(
        id='pitch-type-stacked'
    ),
    dcc.Graph(
        id='pitch-count-bar'
    )
])


@dash.callback(
    Output('pitch-count-bar', 'figure'),
    Output('pitch-type-stacked', 'figure'),
    Input('DataRange', 'date'))
def get_new_data(date):
    dataframe = statcast(date, parallel=False)

    pitch_name = dataframe.groupby('pitch_name').agg(
        count=('game_date', 'count')).reset_index()
    pitch_count_bar = px.bar(pitch_name, x="pitch_name", y="count", barmode="group",  labels={
        'pitch_name': 'Pitch Name',
        'count': 'Pitch Count'
    })

    pitch_group = dataframe.groupby(['player_name', 'pitch_name']).agg(
        count=('game_date', 'count')).reset_index()
    pitch_type_stack = px.bar(pitch_group, x="player_name",
                              y="count", color="pitch_name", title="Long-Form Input",  labels={
                                'player_name': 'Player Name',
                                  'pitch_name': 'Pitch Name',
                                  'count': 'Pitch Count'
                              })
    return pitch_count_bar, pitch_type_stack
