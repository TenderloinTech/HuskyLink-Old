"""The profile page for a user."""

from HuskyLink.templates import template
from HuskyLink.state import State

import reflex as rx


@template(route="/profile", title="Your Profile")
def profile() -> rx.Component:
    # print("Rendering profile page")
    # print(State.name)
    # print(State.password)
    # print(State.role)
    # print(State.is_banned)
    
    return rx.vstack(
        rx.heading("Your Profile", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(f"Name: {State.name}"),  # add text fields for first and last name
        rx.text(f"Password: {len(str(State.password)) | 0}"),  # add text field for password
        rx.text(f"Role: {State.role}"),
        rx.text(f"Is banned? {State.is_banned}"),
        rx.button("Save Changes", color="primary", size="lg"),
    )
