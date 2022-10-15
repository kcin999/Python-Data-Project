"""Configuration for the Flask Application
"""


class Config():
    """Configuration Object for the Flask Applciation
    """
    SQLALCHEMY_DATABASE_URI  = "sqlite:///baseball.db"
    SQLALCHEMY_BINDS = {
        "baseball": "sqlite:///baseball.db",
        "robinhood": "sqlite:///robinhood.db"
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False