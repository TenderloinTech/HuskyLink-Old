"""The explore page."""
from HuskyLink.templates import template
import requests

import reflex as rx

def createExplorePageTable():
    html = "<table><th><tr>Title</tr><tr>Description</tr><tr>Created By</tr></th>"
    r = requests.get("https://api.tenderloin.tech/api/v1/listRequests")
    for x in r.json():
        html += f"<th><td>{x[0]}</td><td>{x[1]}</td><td>{x[7]}</td>"
    html += "</table>"
    return html


@template(route="/explore", title="Explore")
def explore() -> rx.Component:
    """The explore page.

    Returns:
        The UI for the explore page.
    """
    return rx.vstack(
        rx.heading("Explore", font_size="3em"),
        rx.text("This is where you will find people to link up with!"),
        rx.html(createExplorePageTable())
        
    )
