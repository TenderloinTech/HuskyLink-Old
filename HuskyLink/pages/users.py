"""The explore page."""
from HuskyLink.templates import template
import requests

import reflex as rx


@template(route="/users", title="Explore Users")
def users() -> rx.Component:
    """The users page.

    Returns:
        The UI for the users page.
    """

    rows_code = []
    r = requests.get("https://api.tenderloin.tech/api/v1/listAllUsers").json()
    # print(r)
    # All we need the uniqueID for is for pages, ie /view/<id>
    # We do not need the epoch time
    for x in r:
        # print(x[len(x) - 1])
        rows_code.append([x[0], x[1], x[3].upper(), x[len(x) - 1]])
    # for x in r:
    #     rows_code.append([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])
    # for x in r:
    #     rows_code.append([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])
    
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
        rx.text("View all users on the HuskyLink network"),
        rx.card(
        rx.table_container(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("")
                    )
                ),
                rx.tbody(
                    *[rx.tr(
                        *[rx.td(rx.vstack(rx.text(str(item)))) for item in row] + [rx.td(rx.link(rx.button("View Profile"), href=f"/user/{row[3]}"))]
                    ) for row in rows_code]
                )     
            )
        )
        )
    )
