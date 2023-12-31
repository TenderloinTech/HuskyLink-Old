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
    r = requests.get("https://api.tenderloin.tech/api/v1/listRequests")
    if r.ok:
        r = r.json()
        for x in r:
            if x[5]:
                rows_code.append([x[0], x[1], ", ".join(x[3]), x[len(x)-1]])
    # print(r)
    # All we need the uniqueID for is for pages, ie /view/<id>
    # We do not need the epoch time
    
            
    return rx.vstack(
        rx.heading("Explore", font_size="3em"),
        rx.text("This is where you will find people to link up with!"),
        rx.table_container(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Username"),
                        rx.th("Title"),
                        rx.th("Tags"),
                    )
                ),
                rx.tbody(
                    *[rx.tr(
                        *[rx.td(rx.vstack(rx.text(str(item)))) for item in row[:-1]] + [rx.td(rx.link(rx.button("View Details"), href=f"/view/{row[3]}"))]
                    ) for row in rows_code]
                )     
            )
        )
    )
