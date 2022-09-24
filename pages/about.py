"""Home Page for Application.

This is the welcome page for the application.
This has information regarding the application and various navigation pieces.
"""
import dash
from dash import html
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/about', name="About")


def information_card(title: str, link: str, image: str) -> dbc.Card:
    """Returns a card used for information on the About Page

    :param title: Title to display within the card
    :type title: str

    :param link: Destination Link for the button in the card
    :type link: str

    :param image: Image URL for the top of the card
    :type image: str

    :return: DBC Card for to display
    :rtype: dbc.Card
    """
    return dbc.Card([
        dbc.CardImg(src=image, top=True),
        dbc.CardBody([
            dbc.Row([
                html.H4(title, style={"text-align": "center"}),
                dbc.Button(
                    "Click Me!",
                    href=link,
                    target="#",
                    className="col-7"
                )
            ], justify="center"),
        ])
    ])


def about_the_project() -> dbc.Accordion:
    """The "About The Project" Accordion

    :return: Returns the HTML object to render
    :rtype: dbc.Accordion
    """
    return dbc.Accordion(
        dbc.AccordionItem(
            [
                dbc.Container([
                    dbc.Row([
                        html.P(
                            "Welcome to the Nick's Data Project! "
                        ),
                        html.P(
                            (
                                "This is a project created and maintianed by Nick Bierman, "
                                "experimenting with data visualization, website creation, "
                                "design and user interactions, "
                                "data handling and calculating and so much more!"
                            )
                        )
                    ]),
                    dbc.Row([
                        dbc.Col([
                            information_card(
                                title="Project Link",
                                link="https://github.com/kcin999/Python-Data-Project",
                                image="static/images/GitHub.png"
                            )
                        ], width=4)
                    ], justify="center")
                ])
            ],
            title="About the Project"
        ), start_collapsed=True
    )


def about_the_author() -> dbc.Accordion:
    """The "About The Author" Accordion

    :return: Returns the HTML object to render
    :rtype: dbc.Accordion
    """
    return dbc.Accordion(
        dbc.AccordionItem(
            [
                dbc.Container([
                    dbc.Row([
                        html.P(
                            (
                                "Nick Bierman is a current college Senior at Xavier Univeristy "
                                "studying Computer Science with dual minors in "
                                "Mathematics and Business Analytics. "
                            )
                        ),
                        html.P(
                            (
                                "He has a strong interest and passion for data, "
                                "including pulling insights, and making data accessible. "
                            )
                        ),
                        html.P(
                            (
                                "In addition to data analysis, Nick enjoys pulling data from "
                                "multiple sources and connecting them and combining them. "
                            )
                        ),
                        html.P(
                            (
                                "Outside of his data project, school, and work, "
                                "Nick enjoys listening to music"
                                "such as: country, rock, pop, and anything in between. "
                                "He also loves sports and especially baseball, "
                                "thus showing the emphasis on baseball statistics"
                            )
                        )
                    ]),
                    dbc.Row([
                        dbc.Col([
                            information_card(
                                title="LinkedIn",
                                link="https://www.linkedin.com/in/nicholas-bierman/",
                                image="static/images/LinkedIn.png"
                            )
                        ], width=4),
                        dbc.Col([
                            information_card(
                                title="Gmail",
                                link="mailto:nbierman2002@gmail.com",
                                image="static/images/Gmail.png"
                            )
                        ], width=4),
                        dbc.Col([
                            information_card(
                                title="GitHub",
                                link="https://github.com/kcin999",
                                image="static/images/GitHub.png"
                            )
                        ], width=4)
                    ], justify="center")
                ])
            ],
            title="About the Author"
        ), start_collapsed=True
    )


def layout() -> dbc.Container:
    """Returns the layout for the about page

    :return: The HTML.DIV for the about page
    :rtype: html.Div
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                [
                    html.Div(
                        [
                            html.H2("Nick's Data Project!"),
                        ], style={"text-align": "center"}
                    )
                ],
                width=7
            )
        ], justify="center"
        ),
        dbc.Row([
            dbc.Col([
                about_the_project()
            ], width=6),
            dbc.Col([
                about_the_author()
            ], width=6)
        ],
            justify="center"
        )
    ])
