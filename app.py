from dash import Dash, html
import dash
import config


def create_app():
    """Creates the application object to run

    :return: Returns the Dash Application
    :rtype: Dash
    """
    app = Dash(__name__, use_pages=True)
    server = app.server

    server.config.from_object(config.Config)

    from database.database_models import db
    db.init_app(server)
    db.create_all(app=server)

    app.layout = html.Div([
        dash.page_container
    ])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
