"""The dashboard page."""
from HuskyLink.templates import template
from HuskyLink.state import State
import reflex as rx

class AddRequestState(State):
    title: str = ""
    description: str = ""
    tags: str = ""
    def submit_form(self, form_data: dict):
        self.title = form_data['title']
        self.description = form_data['description']
        self.tags = form_data['tags']
        print(form_data)
        return rx.redirect("/dashboard")


@rx.page(route="/add_request", title="Add Request")
def add_request() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """

    
            
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Add new request", font_size="3em"),
                rx.hstack(
                    rx.text("Title:"),
                    rx.input(id="title", placeholder="Title", size="lg"),
                ),
                rx.hstack(
                    rx.text("Description:"),
                    rx.input(id="description", placeholder="Description", size="lg"),
                ),
                rx.hstack(
                    rx.text("Tags:"),  
                    rx.input(id="tags", placeholder="Tags", size="lg"),
                ),
                rx.link(rx.button("Submit", type="submit"), href="/dashboard"),
                rx.link(rx.button("Cancel"), href="/dashboard"),
            ), on_submit=AddRequestState.submit_form )
    )
