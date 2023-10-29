from HuskyLink.templates import template
import requests

import reflex as rx


@template(route="/user/[name]/", title="User")
def user() -> rx.Component:
    """The view page.

    Returns:
        The UI for the view page.
    """
    name = "gupta87"

    r = requests.get(f"https://api.tenderloin.tech/api/v1/getUserInfo/{name}")

    return rx.vstack(
        rx.heading(f"{r.json()[0][1]} ({r.json()[0][0]})", font_size="3em"),
        rx.link(rx.text(f"Email: {r.json()[0][7]}"), href=f"mailto:{r.json()[0][7]}"),
        rx.text(f"Role: {r.json()[0][3]}"),
        rx.image(src=f"{r.json()[0][4]}", width="auto", height="200px"),
        rx.hstack(
            rx.card(
                rx.text("dakjsdaksjh"),
                header=rx.heading("About", font_size="2em"),
                footer=rx.text("dakjsdaksjh"),
            ),
            rx.card(
                rx.text("dakjsdaksjh"),
                header=rx.heading("About", font_size="2em"),
                footer=rx.text("dakjsdaksjh"),
            ),
            rx.card(
                rx.text("dakjsdaksjh"),
                header=rx.heading("About", font_size="2em"),
                footer=rx.text("dakjsdaksjh"),
            ),
        )
    )
