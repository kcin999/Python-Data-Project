"""Main starting point for the application
"""
from dash import Dash, html
import dash_bootstrap_components as dbc
import dash
import config

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Custom Visualizations",
                    href="/custom_visualization")),
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Admin", href="/admin"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Data Project",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True
)


def create_app() -> Dash:
    """Creates the application object to run

    :return: Returns the Dash Application
    :rtype: Dash
    """
    app = Dash(__name__,
               use_pages=True,
               external_stylesheets=[dbc.themes.DARKLY]
               )
    server = app.server

    server.config.from_object(config.Config)

    from database.database_models import db
    db.init_app(server)
    db.create_all(app=server)

    app.layout = html.Div(
        children=[
            navbar,
            dash.page_container
        ]
    )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run_server()
