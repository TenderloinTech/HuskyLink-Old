"""The profile page for a user."""

from HuskyLink.templates import template
from HuskyLink.state import State
# import datetime

import reflex as rx




@template(route="/profile", title="Your Profile")
def profile() -> rx.Component:
    # print("Rendering profile page")
    # print(State.name)
    # print(State.password)
    # print(State.role)
    # print(State.is_banned)
    
    # def convertTime(ogTime):
    #     timestamp = datetime.datetime.fromtimestamp(ogTime)
    #     return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    
    return rx.vstack(
        rx.heading("Your Profile", font_size="3em"),
        rx.image(src=f"{State.profile_image}",    width="auto",
    height="200px",
    box_shadow="lg",),
        rx.text(f"Name: {State.fullname}"),  # add text fields for first and last name
        rx.text(f"Password: {len(str(State.password)) | 0} Characters"),  # add text field for password
        rx.text(f"Role: {State.role}"),
        rx.text(f"Is banned? {State.is_banned}"),
        rx.button("Save Changes", color="primary", size="lg"),
    )
