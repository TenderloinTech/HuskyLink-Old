import requests

def testLogin(user, password):
    r = requests.post("localhost:5000/api/v1/login", data={})