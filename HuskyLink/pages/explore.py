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

    rows_code = []
    r = requests.get("https://api.tenderloin.tech/api/v1/listRequests").json()
    for x in r.json():
        tup = (x[0], 30, x[1], rx.button("View Details", color="#FF0000", variant='ghost'))
        rows_code.append(tup)
    return rx.vstack(
        rx.heading("Explore", font_size="3em"),
        rx.text("This is where you will find people to link up with!"),
        rx.table_container(
            rx.table(
                headers=["Name", "Age", "Location", "Button"],
                rows=rows_code,
                variant="striped",
            )
        )
        
    )
