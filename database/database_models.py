"""Houses all Database Models / Tables for the database
"""
from datetime import datetime
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pitches(db.Model):
    """This is a database model class which houses all pitches and their results
    """
    __tablename__ = "pitches"
    __bind_key__ = 'baseball'

    id = db.Column(db.Integer, primary_key=True)
    pitch_type = db.Column(db.String(2))
    game_date = db.Column(db.Date)
    release_pos_x = db.Column(db.Float)
    release_speed = db.Column(db.Float)
    release_pos_z = db.Column(db.Float)
    release_pos_y = db.Column(db.Float)
    pitcher = db.Column(db.String(8))
    batter = db.Column(db.String(8))
    description = db.Column(db.String(35))
    events = db.Column(db.String(35))
    des = db.Column(db.Text)
    zone = db.Column(db.String(1))
    stand = db.Column(db.String(1))
    game_type = db.Column(db.String(1))
    home_team = db.Column(db.String(3))
    p_throws = db.Column(db.String(1))
    type = db.Column(db.String(1))
    away_team = db.Column(db.String(3))
    bb_type = db.Column(db.String(15))
    hit_location = db.Column(db.String(1))
    strikes = db.Column(db.Integer)
    balls = db.Column(db.Integer)
    pfx_z = db.Column(db.Float)
    pfx_x = db.Column(db.Float)
    plate_z = db.Column(db.Float)
    plate_x = db.Column(db.Float)
    on_2b = db.Column(db.String(8))
    on_3b = db.Column(db.String(8))
    outs_when_up = db.Column(db.Integer)
    on_1b = db.Column(db.String(8))
    inning_topbot = db.Column(db.String(3))
    inning = db.Column(db.String(1))
    hc_y = db.Column(db.Float)
    hc_x = db.Column(db.Float)
    vy0 = db.Column(db.Float)
    vx0 = db.Column(db.Float)
    ax = db.Column(db.Float)
    vz0 = db.Column(db.Float)
    az = db.Column(db.Float)
    ay = db.Column(db.Float)
    sz_bot = db.Column(db.Float)
    sz_top = db.Column(db.Float)
    launch_speed = db.Column(db.Float)
    hit_distance_sc = db.Column(db.Integer)
    effective_speed = db.Column(db.Float)
    launch_angle = db.Column(db.Integer)
    spin_axis = db.Column(db.Integer)
    release_spin_rate = db.Column(db.Integer)
    game_pk = db.Column(db.String(8))
    release_extension = db.Column(db.Float)
    fielder_3 = db.Column(db.String(8))
    fielder_2 = db.Column(db.String(8))
    fielder_5 = db.Column(db.String(8))
    fielder_4 = db.Column(db.String(8))
    fielder_7 = db.Column(db.String(8))
    fielder_6 = db.Column(db.String(8))
    fielder_9 = db.Column(db.String(8))
    fielder_8 = db.Column(db.String(8))
    estimated_woba_using_speedangle = db.Column(db.Float)
    estimated_ba_using_speedangle = db.Column(db.Float)
    woba_denom = db.Column(db.Integer)
    woba_value = db.Column(db.Float)
    iso_value = db.Column(db.Integer)
    babip_value = db.Column(db.Integer)
    at_bat_number = db.Column(db.Integer)
    launch_speed_angle = db.Column(db.Integer)
    pitch_name = db.Column(db.String(25))
    pitch_number = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    home_score = db.Column(db.Integer)
    fld_score = db.Column(db.Integer)
    bat_score = db.Column(db.Integer)
    post_home_score = db.Column(db.Integer)
    post_away_score = db.Column(db.Integer)
    post_fld_score = db.Column(db.Integer)
    post_bat_score = db.Column(db.Integer)
    of_fielding_alignment = db.Column(db.String(20))
    if_fielding_alignment = db.Column(db.String(20))
    delta_run_exp = db.Column(db.Float)
    delta_home_win_exp = db.Column(db.Float)


class Players(db.Model):
    """This is the database model class which houses all player information and their various keys
    """
    __tablename__ = 'players'
    __bind_key__ = 'baseball'

    id = db.Column(db.Integer, primary_key=True)
    key_retro = db.Column(db.String(10))
    key_bbref = db.Column(db.String(10))
    key_fangraphs = db.Column(db.String(10))
    key_mlbam = db.Column(db.String(10))
    mlb_played_first = db.Column(db.String(4))
    mlb_played_last = db.Column(db.String(4))
    name_last = db.Column(db.String(20))
    name_first = db.Column(db.String(20))
    name_given = db.Column(db.String(60))
    name_suffix = db.Column(db.String(20))
    name_nick = db.Column(db.String(55))
    birth_date = db.Column(db.Date)
    death_date = db.Column(db.Date)


class Stocks(db.Model):
    """This is the database model class which houses overall stock information
    """
    __tablename__ = 'stocks'
    __bind_key__ = 'robinhood'

    stock_ticker = db.Column(db.String(5), primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)

    owned_stock = db.relationship('OwnedStock', backref='stocks', lazy=True)

    created_datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=sqlalchemy.sql.func.now()
    )
    updated_datetime = db.Column(
        db.DateTime, nullable=False,
        onupdate=datetime.utcnow(),
        server_onupdate=sqlalchemy.sql.func.now()
    )


class OwnedStock(db.Model):
    """This is the database model class which houses equity informaiton for stocks
    """
    __tablename__ = 'ownedstock'
    __bind_key__ = 'robinhood'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(
        db.String(5),
        db.ForeignKey('stocks.stock_ticker'),
        nullable=False
    )
    created_datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=sqlalchemy.sql.func.now()
    )
    price = db.Column(db.Numeric(8, 4))
    quantity = db.Column(db.Numeric(16, 8))
    average_buy_price = db.Column(db.Numeric(8, 4))
    equity = db.Column(db.Numeric(8, 4))
    percent_change = db.Column(db.Numeric(5, 2))
    intraday_percent_change = db.Column(db.Numeric(5, 2))
    equity_change = db.Column(db.Numeric(8, 4))
    pe_ratio = db.Column(db.Numeric(12, 8))
    percentage = db.Column(db.Numeric(5, 2))
