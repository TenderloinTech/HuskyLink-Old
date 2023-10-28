"""The profile page for a user."""

from HuskyLink.templates import template

import reflex as rx


@template(route="/profile", title="Your Profile")
def profile() -> rx.Component:
    return rx.vstack(
        rx.heading("Your Profile", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text("Name:"),  # add text fields for first and last name
        rx.text("Email:"),  # add text field for email
        rx.text("Password:"),  # add text field for password
        rx.text("Phone Number:"),  # add text field for phone number
        rx.text("Grade:"),  # add text field for grade
        rx.text("Major:"),  # add text field for major
        rx.text("Interests:"),  # add text field for interests
        rx.text("Bio:"),  # add text field for bio
        rx.button("Save Changes", color="primary"),
        rx.button("Cancel", color="secondary"),
    )
