from HuskyLink.templates import template
import requests
from HuskyLink.state import State
from typing import List, Tuple
import datetime

import reflex as rx
@template(route="/view/[id]/", title="View")
def view() -> rx.Component:
    """The view page.

    Returns:
        The UI for the view page.
    """
    id_savior_of_all = "5083743578"
    tags: str = "None"
    description: str = "None"
    user_name: str = "None"
    title: str = "None"
    good_time: int = 0
    
    r = requests.get(f"https://api.tenderloin.tech/api/v1/getRequestByID/{id_savior_of_all}")
    # print("response = ", r)
    if r.ok:
        data = r.json()
        # print("RESPONSE IN VIEW.PY API CALL IS: ", data)
        if data:
            user_name = data[0][0]
            title = data[0][1]
            description = data[0][2]
            tags = ", ".join(data[0][3])
            epoch_time = data[0][4]
            good_time = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d')
    
    return rx.vstack(
        rx.heading(title, font_size="3em"),
        rx.text(tags),
        rx.text(description),
        rx.button("Request to Link", color="primary", size="lg"),
        rx.hstack(
            rx.image(src="https://picsum.photos/200", width="auto", height="100px"),
            rx.vstack(
            rx.text(user_name),
            rx.text(f"Posted at: {good_time}")
            )
        )
    )
