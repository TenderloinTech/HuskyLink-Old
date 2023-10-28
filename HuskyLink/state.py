"""Base state for the app."""

import reflex as rx

class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    
    username: str = ""
    password: str = ""
    loggedIn: bool = False

    # @rx.var
    # def username(self) -> str:
    #     """The username of the user."""
    #     return self.username
    
    # @rx.var
    # def password(self) -> str:
    #     """The password of the user."""
    #     return self.password
    
    @rx.var
    def loggedIn(self) -> bool:
        """Whether the user is logged in."""
        return self.loggedIn
    
    def loginAuth(self):
        
        if self is not None and self.username is not None and self.password is not None and State.loggedIn is True:
            State.username = self.username
            State.password = self.password    
            if len(self.username)>0 and len(self.password)>0:
                State.loggedIn = True
                return rx.redirect("/dashboard")
        return rx.redirect("/login")
    pass


