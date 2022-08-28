from dash import Dash, html, dcc
import dash


def create_app():
    app = Dash(__name__, use_pages=True)

    app.layout = html.Div([
        dash.page_container
    ])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
