import requests
import random

def testLogin(user, password):
    r = requests.post("http://localhost:5000/api/v1/login", data={"username": user, "password": password})
    return r.json()["result"]["password"]

print(testLogin("sj", "s")) # Expected to return False
print(testLogin("james", "s")) # Expected to return False
print(testLogin("james", "admin123")) # Expected to return True

def testCreateAccount(user, password):
    r = requests.post("http://localhost:5000/api/v1/createAccount", data={"username": user, "password": password})
    return r.json()["result"]

print(testCreateAccount("nick", "bob123")) # Expected to return "Username exists"
print(testCreateAccount(f"demouser{str(random.randint(0,100000000))}", "mypassword123")) # Should always work