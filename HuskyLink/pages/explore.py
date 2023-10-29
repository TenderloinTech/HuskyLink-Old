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
    print(r)
    for x in r:
        rows_code.append([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])
    for x in r:
        rows_code.append([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])
    for x in r:
        rows_code.append([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])
    
    def renderer(thing: list):
        return rx.vstack(
            rx.text(str(thing[0])),
            # rx.text(thing[1]),
            # rx.text(thing[2]),
            # rx.text(thing[4]),
            # rx.text(thing[5]),
            rx.button("View details")
        )
    # def rendering(x):
    #     print(x)
    #     return rx.td(rx.vstack(
    #         rx.heading(x[0], font_size="3em"),
    #         rx.text("tester"),
    #         rx.text(x[1]),  # add text fields for first and last name
    #         #rx.text(f"Password: {len(str(State.password)) | 0} Characters"),  # add text field for password
    #         #rx.text(f"Role: {State.role}"),
    #         #rx.text(f"Is banned? {State.is_banned}"),
    #         rx.button("View Request", color="primary", size="lg"),
    #     ))
    #     #tup = (x[0], 30, x[1], rx.button("View Details", color="#FF0000", variant='link'))
    #     rows_code.append(stateForTable)
    return rx.vstack(
        rx.heading("Explore", font_size="3em"),
        rx.text("This is where you will find people to link up with!"),
        rx.table_container(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("")
                    )
                ),
                rx.tbody(
                        *[rx.tr(
                            *[rx.td(rx.vstack(
                                rx.text(str(item)),
                                ))for item in row
                            ]
                        ) for row in rows_code]
                        
                    )     
            )
        )
    )
