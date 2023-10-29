"""Base state for the app."""

import reflex as rx
import requests
import random
class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    
    username: str = ""
    name: str = ""
    createdAtTime: int = 0
    role: str = ""
    profile_image: str = ""
    is_banned: bool = False
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
    
    # @rx.var
    # def loggedIn(self) -> bool:
    #     """Whether the user is logged in."""
    #     return self.loggedIn
    
    def loginAuth(self, form_data: dict):
        # print("form data", form_data)
        
        State.username = form_data['username']
        State.password = form_data['password']
        # print(State.username, State.password)
        r = requests.post(f"http://143.198.129.9:5000/api/v1/login", data={"username": State.username, "password": State.password})        
        # print("response:",r.json())
        
        if r.json()["result"]["password"]:
            State.loggedIn = True
            results = requests.get(f"http://143.198.129.9:5000/api/v1/getUserInfo/{State.username}")  
            print(results)
            State.name = results.json()[0][1]      
            State.role = results.json()[0][2]      
            State.profile_image = results.json()[0][4]
            State.is_banned = results.json()[0][5]            
            return rx.redirect("/profile")

    pass


