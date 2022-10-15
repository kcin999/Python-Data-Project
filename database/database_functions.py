"""Has all database functions within it
"""
import os
import io
from datetime import datetime
import pybaseball
import requests
import pandas as pd
from sqlalchemy.inspection import inspect
from robin_stocks import robinhood as r
import pyotp

from database.database_models import OwnedStock, Pitches, Players, db
from global_variables import PLAYER_INFO_URL


class Statcast():
    def add_player_info(self):
        """Adds Player Info to the Database
        """
        df = self.download_player_info()

        df.to_sql(con=db.engine, name='players',
                  if_exists='append', index=False)

    def download_player_info(self) -> pd.DataFrame:
        """Get's all player info

        :return: Dataframe that contains the player information
        :rtype: pd.DataFrame
        """
        request_content = requests.get(PLAYER_INFO_URL).content
        columns_to_keep = [
            'key_retro',
            'key_bbref',
            'key_fangraphs',
            'key_mlbam',
            'mlb_played_first',
            'mlb_played_last',
            'name_last',
            'name_first',
            'name_given',
            'name_suffix',
            'name_nick',
            'birth_date',
            'death_date'
        ]
        df = pd.read_csv(
            io.StringIO(request_content.decode('utf-8')),
            dtype=str
        )

        # Only MLB Players
        df.dropna(how='all', subset=[
            'key_retro',
            'key_bbref',
            'key_fangraphs',
            'mlb_played_first',
            'mlb_played_last'
        ], inplace=True)

        # Converts Birth and Death Columns to a singular datetime column
        df['birth_date'] = pd.to_datetime(
            df['birth_year'] + '/' + df['birth_month'] + '/' + df['birth_day'])
        df['death_date'] = pd.to_datetime(
            df['death_year'] + '/' + df['death_month'] + '/' + df['death_day'])

        return df[columns_to_keep]

    def download_statcast_data(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """Retrieves the Statcast Data between the two dates

        :param start_date: Start date of range to get data for
        :type start_date: datetime

        :param end_date: End date of range to get data for
        :type end_date: datetime

        :return: Dataframe containing all information relating to statcast data
        :rtype: pd.DataFrame
        """
        df = pybaseball.statcast(
            start_dt=start_date.strftime("%Y-%m-%d"),
            end_dt=end_date.strftime("%Y-%m-%d"),
            parallel=False
        )

        return df[[
            'pitch_type',
            'game_date',
            'release_speed',
            'release_pos_x',
            'release_pos_y',
            'release_pos_z',
            'batter',
            'pitcher',
            'events',
            'description',
            'zone',
            'des',
            'game_type',
            'stand',
            'p_throws',
            'home_team',
            'away_team',
            'type',
            'hit_location',
            'bb_type',
            'balls',
            'strikes',
            'pfx_x',
            'pfx_z',
            'plate_x',
            'plate_z',
            'on_3b',
            'on_2b',
            'on_1b',
            'outs_when_up',
            'inning',
            'inning_topbot',
            'hc_x',
            'hc_y',
            'vx0',
            'vy0',
            'vz0',
            'ax',
            'ay',
            'az',
            'sz_top',
            'sz_bot',
            'hit_distance_sc',
            'launch_speed',
            'launch_angle',
            'effective_speed',
            'release_spin_rate',
            'spin_axis',
            'release_extension',
            'game_pk',
            'fielder_2',
            'fielder_3',
            'fielder_4',
            'fielder_5',
            'fielder_6',
            'fielder_7',
            'fielder_8',
            'fielder_9',
            'estimated_ba_using_speedangle',
            'estimated_woba_using_speedangle',
            'woba_value',
            'woba_denom',
            'babip_value',
            'iso_value',
            'launch_speed_angle',
            'at_bat_number',
            'pitch_number',
            'pitch_name',
            'home_score',
            'away_score',
            'bat_score',
            'fld_score',
            'post_away_score',
            'post_home_score',
            'post_bat_score',
            'post_fld_score',
            'if_fielding_alignment',
            'of_fielding_alignment',
            'delta_home_win_exp',
            'delta_run_exp'
        ]]

    def add_statcast_data_to_database(self, start_date: datetime, end_date: datetime):
        """Adds statcast data to our database

        :param start_date: Start date of range to get data for
        :type start_date: datetime

        :param end_date: End date of range to get data for
        :type end_date: datetime
        """
        df = self.download_statcast_data(start_date, end_date)

        df.to_sql(
            con=db.engines['baseball'], name='pitches',
            if_exists='append', index=False
        )

    def delete_statcast_data_from_database(self, start_date: datetime = None, end_date: datetime = None):
        """Clears statcast data between the two date ranges.
            If they are not provided, it goes to the beginning / end of the data

        :param start_date: Start date of range to get data for, defaults to None
        :type start_date: datetime, optional
        :param end_date: End date of range to get data for, defaults to None
        :type end_date: datetime, optional
        """
        query = Pitches.query
        if start_date:
            query = query.filter(Pitches.game_date >= start_date)

        if end_date:
            query = query.filter(Pitches.game_date <= end_date)

        query.delete()

    def get_columns(self, model: str) -> list[str]:
        """Retuns a list of the columns in a table

        :param model: WHich table / model to get the attributes for
        :type model: str

        :return: List of the column names
        :rtype: list[str]
        """
        if model == 'Pitches':
            return [column.name for column in inspect(Pitches).c]
        elif model == 'Players':
            return [column.name for column in inspect(Players).c]

    def get_statcast_data_from_database(self) -> pd.DataFrame:
        """Returns the Statcast data from within the table

        :return: Dataframe of statcast data
        :rtype: pd.Dataframe
        """
        return pd.read_sql(Pitches.query.statement, con=db.engines['baseball'])


class Robinhood():

    def download_robinhood_data(self) -> pd.DataFrame:
        """Downloads the Robinhood share data

        :return: Dataframe of Stock data for a given point in time
        :rtype: pd.DataFrame
        """
        if os.environ.get('ROBINHOOD_ONETIME_PASSWORD') is not None:
            r.login(os.environ.get('ROBINHOOD_USERNAME'), os.environ.get('ROBINHOOD_PASSWORD'),
                    mfa_code=pyotp.TOTP(os.environ.get('ROBINHOOD_ONETIME_PASSWORD')).now())
        else:
            r.login(os.environ.get('ROBINHOOD_USERNAME'),
                    os.environ.get('ROBINHOOD_PASSWORD'))

        my_stocks = r.account.build_holdings()
        r.authentication.logout()

        df = pd.DataFrame(my_stocks)

        df = df.T
        df['ticker'] = df.index
        df = df.reset_index(drop=True)

        return df

    def add_owned_stock_to_database(self):
        """Adds Stock Data to the database
        """
        stock_data = self.download_robinhood_data()

        stock_data.drop(labels=['type', 'name', 'id'], axis=1, inplace=True)

        stock_data.to_sql(
            con=db.engines['robinhood'],
            name='ownedstock',
            if_exists='append',
            index=False
        )
