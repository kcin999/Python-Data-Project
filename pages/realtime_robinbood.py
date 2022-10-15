import dash

dash.register_page(__name__, path='/realtime-robinhood',
                   name="Realtime Robinhood")


def layout():
    return "Robinhood"