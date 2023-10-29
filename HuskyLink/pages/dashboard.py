"""The dashboard page."""
from HuskyLink.templates import template

import reflex as rx
import requests

@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    r = requests.get("https://api.tenderloin.tech/api/v1/getStats")
    print(r)
    total_requests = 0
    total_users = 0
    if r.ok:
        r = r.json()
        total_requests = r["totalRequests"]
        total_users = r["totalUsers"]
        
    
    
    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.heading(f"Total Requests: {total_requests}", font_size="2em"),
        rx.heading(f"Total Users: {total_users}", font_size="2em"),
        rx.button("Add Request"),
    )
