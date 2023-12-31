"""Sidebar component for the app."""

from HuskyLink import styles
from HuskyLink.state import State

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.vstack(
        # The logo.
        rx.image(
            src="/logo.png",
            height="10em",
        ),
        # Link to Reflex GitHub repo.
        rx.link(
            rx.center(
                rx.image(
                    src="/github.svg",
                    height="3em",
                    padding="0.5em",
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="https://github.com/TenderloinTech/HuskyLink",
        ),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Docs"),
            href="https://reflex.dev/docs/getting-started/introduction/",
        ),
        rx.link(
            rx.text("Blog"),
            href="https://reflex.dev/blog/",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (State.router.page.path == f"/{text.lower()}") | (
        (State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.image(
                src=icon,
                height="2.5em",
                padding="0.5em",
            ),
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages
    # print("\n\n\nPAGES = ", pages, "\n\n\n")

    routes = [
        {"title": "Dashboard", "route": "/dashboard", "image": "dashboard.svg"},
        {"title": "Explore", "route": "/explore", "image": "explore.svg"},
        # {"title": "Create Account", "route": "/create_account", },
        # {"title": "Login", "route": "/"},
        {"title": "Your Profile", "route": "/profile", "image": "userprofile.svg"},
        {"title": "Explore Users", "route": "/users", "image": "users.svg"},
    ]
    
    
    
    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        icon="",
                        url=page["route"],
                    )
                    for page in routes
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
