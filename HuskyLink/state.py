"""Base state for the app."""

import reflex as rx
import requests
import random
class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    
    username: str = ""
    password: str = ""
    name: str = ""
    createdAtTime: int = 0
    role: str = ""
    profile_image: str = ""
    is_banned: bool = False
    loggedIn: bool = False
    joined: int = 0
    
    @rx.var
    def title(self):
            return self.router.page.params.get("id", 0)
    #     # print("id:", id)
    #     # print("broo... check out the ID: ---> ", type(id))
    #     # if id == 0:
    #     #     return "unset"
    #     # print(f"API Call to - https://api.tenderloin.tech/api/v1/getRequestByID/{id}")
    #     # r = requests.get(f"https://api.tenderloin.tech/api/v1/getRequestByID/{id}")
    #     # if r is not None:
    #     #     print(r.json())
    #     #     return r
    #     # return "unset"
        
    # def getPostID(self):
    #     return self.title
    
    def loginAuth(self, form_data: dict):
        # print("form data", form_data)
        
        self.username = form_data['username']
        self.password = form_data['password']
        r = requests.post(f"https://api.tenderloin.tech/api/v1/login", data={"username": self.username, "password": self.password})        
        
        if r.json()["result"]["password"] is True:
            self.loggedIn = True
            results = requests.get(f"https://api.tenderloin.tech/api/v1/getUserInfo/{self.username}")  
            
            self.name = results.json()[0][1]      
            self.role = results.json()[0][3]
            self.joined = results.json()[0][2]      
            self.profile_image = results.json()[0][4]
            self.is_banned = results.json()[0][5]  
            
            # print("name:", self.name)
            # print("role:", self.role)
            # print("profile image:", self.profile_image)
            # print("is banned:", self.is_banned)
            
              
            print("login successful, redirecting to explore")        
            return rx.redirect("/explore")
        
    pass


