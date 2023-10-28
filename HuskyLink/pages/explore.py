"""The explore page."""
from HuskyLink.templates import template

import reflex as rx


@template(route="/explore", title="Explore")
def explore() -> rx.Component:
    """The explore page.

    Returns:
        The UI for the explore page.
    """
    return rx.vstack(
        rx.heading("Explore", font_size="3em"),
        rx.text("This is where you will find people to link up with!"),
        
    )
