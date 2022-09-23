import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"]),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                # This is where we can ignore pages from our side bar
                if not page["name"].startswith("Not Found")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        ))
