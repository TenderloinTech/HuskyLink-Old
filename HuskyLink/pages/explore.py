"""The explore page."""
from HuskyLink.templates import template
import requests

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
        rx.table_container(
            rx.table(
                headers=["Name", "Age", "Location", "Button"],
                rows=[
                    ("John", 30, "New York", rx.button("View Details", color="#FF0000", variant='ghost')),
                    ("Jane", 31, "San Francisco", rx.button("View Details", color="#FF0000",variant='ghost')),
                    ("Joe", 32, "Los Angeles", rx.button("View Details", color="#FF0000", variant='ghost')),
                ],
                variant="striped",
            )
        )
        
    )
