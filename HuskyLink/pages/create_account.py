"""The dashboard page."""
from HuskyLink.templates import template
from HuskyLink.state import State
import reflex as rx
import requests
from typing import List
import time

@rx.page(route="/create_account", title="Create Account")
def create_account() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    
    class createAccountState(State):
        text:str = "no selection"
        def createAccount(self, form_data: dict):
            r = requests.post("https://api.tenderloin.tech/api/v1/createAccount", 
                data={
                    "username": form_data["username"],
                    "password": form_data["password"],
                    "realName": form_data["full_name"],
                    "userType": self.text,
                    "createdAt":round(time.time()),
                    "profileImage": form_data["pfp_link"],
                    "isBanned": False,
                    "email": form_data["email"],
                })

        
    options: List[str] = ["Student", "Instructor"]

    
    
    return rx.vstack(
        rx.form(
        rx.vstack(
        rx.heading("Login Page", font_size="3em"),
        rx.text("Please log in!"),
        rx.hstack(
            rx.text("Username:"),  # add text field for username
            rx.input(id="username", placeholder="Username", size="lg"),
        ),
        rx.hstack(
            rx.text("Password:"),  # add text field for password
            rx.input(id="password", placeholder="Password", size="lg"),
        ),
        rx.hstack(
            rx.text("Full Name:"),  # add text field for password
            rx.input(id="full_name", placeholder="Full Name", size="lg"),
        ),
        rx.hstack(
            rx.text("Email:"),  # add text field for password
            rx.input(id="email", placeholder="Email", size="lg"),
        ),
        rx.radio_group(
            options,
            on_change=createAccountState.set_text,
        ),
        rx.hstack(
            rx.text("URL for profile Image:"),  # add text field for password
            rx.input(id="pfp_link", placeholder="URL to Image", size="lg"),
        ),
        rx.button("Login", color="primary", size="lg", type_="submit")
    ), on_submit=createAccountState.createAccount)
    )
