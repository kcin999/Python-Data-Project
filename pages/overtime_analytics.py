import dash
from dash import html, dcc, Input, Output
from pybaseball import statcast
from pybaseball import cache
import plotly.express as px
import datetime

from global_variables import pitch_types


cache.enable()

dash.register_page(__name__, '/overtime-analytics', title="Overtime Analytics")

layout = html.Div(children=[
	html.H1(children='This is our Overtime Analytics page'),
	dcc.DatePickerRange(
		id="DataRange",
		month_format="M/D/Y",
		start_date=datetime.date.today() - datetime.timedelta(days=30),
		end_date=datetime.date.today(),
		updatemode='bothdates'
	),
	dcc.Dropdown(options=pitch_types, id='pitch-selector'),
	dcc.Graph(
		id='pitch-count-over-time'
	),
	dcc.Graph(
		id='max-speed-over-time'
	)
])


@dash.callback(
	Output('pitch-count-over-time', 'figure'),
	Output('max-speed-over-time', 'figure'),
	Input('DataRange', 'start_date'),
	Input('DataRange', 'end_date'),
	Input('pitch-selector', 'value')
)
def get_new_data(start_date, end_date, pitch_name):
	dataframe = statcast(start_date, end_date, parallel=False)

	if pitch_name:
		dataframe = dataframe[dataframe['pitch_name'] == pitch_name]
		dataframe.to_csv('filtered.csv')

	agg_pitch_count = dataframe.groupby(['game_date', 'player_name']).agg(
		count=('release_speed', 'count')).reset_index()
	agg_max_release = dataframe.groupby(['game_date', 'player_name']).agg(
		max=('release_speed', 'max')).reset_index()

	pitch_count_over_time = px.line(
		agg_pitch_count, x="game_date", y="count", color="player_name", markers=True)
	max_speed_over_time = px.line(
		agg_max_release, x="game_date", y="max", color="player_name", markers=True)

	return pitch_count_over_time, max_speed_over_time
