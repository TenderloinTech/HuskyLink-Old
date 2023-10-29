from HuskyLink.templates import template
import requests

import reflex as rx


@template(route="/view", title="View")
def explore() -> rx.Component:
    """The view page.

    Returns:
        The UI for the view page.
    """

    return rx.vstack(
        rx.heading(", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.image(src=f"{State.profile_image}",    width="auto",
    height="200px",
    box_shadow="lg",),
        rx.text(f"Name: {State.name}"),  # add text fields for first and last name
        rx.text(f"Password: {len(str(State.password)) | 0} Characters"),  # add text field for password
        rx.text(f"Role: {State.role}"),
        rx.text(f"Is banned? {State.is_banned}"),
        rx.button("Save Changes", color="primary", size="lg"),
    )
