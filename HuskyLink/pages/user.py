from HuskyLink.templates import template
import requests

import reflex as rx


@template(route="/user/<name>/", title="View")
def view(name) -> rx.Component:
    """The view page.

    Returns:
        The UI for the view page.
    """

    r = requests.get(f"https://api.tenderloin.tech/api/v1/getUserInfo/{name}")

    return rx.vstack(
        rx.heading(f"{r.json()[0][0]}", font_size="3em")
        
    )
