"""The dashboard page."""
from HuskyLink.templates import template

import reflex as rx


@template(route="/login", title="Login")
def login() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Login Page", font_size="3em"),
        rx.text("Please log in!"),
        rx.hstack(
        rx.text("Username:"),  # add text field for username
        rx.input(placeholder="Username", size="lg"),  # add text field for username 
        ),
        rx.hstack(
        rx.text("Password:"),  # add text field for password
        rx.input(placeholder="Password", size="lg"),
        ),# add text field for password
        rx.button("Login", color="primary", size="lg"),
    )
