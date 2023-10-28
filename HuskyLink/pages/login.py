"""The dashboard page."""
from HuskyLink.templates import template
from HuskyLink.state import State
import reflex as rx

@template(route="/login", title="Login")
def login() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    if State.loggedIn is True:
        return rx.redirect("/dashboard")
    return rx.vstack(
        rx.heading("Login Page", font_size="3em"),
        rx.text("Please log in!"),
        rx.hstack(
            rx.text("Username:"),  # add text field for username
            rx.input(id="username", placeholder="Username", size="lg"),
        ),
        rx.hstack(
            rx.text("Password:"),  # add text field for password
            rx.input(id="password", placeholder="Password", size="lg"),
        ),
        rx.button("Login", color="primary", size="lg", on_click=State.loginAuth),
    )
