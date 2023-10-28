import requests
import random

endpoint = "localhost"

def testLogin(user, password):
    r = requests.post(f"http://{endpoint}:5000/api/v1/login", data={"username": user, "password": password})
    return r.json()["result"]["password"]

print(testLogin("sj", "s")) # Expected to return False
print(testLogin("james", "s")) # Expected to return False
print(testLogin("james", "admin123")) # Expected to return True

def testCreateAccount(user, password, realName, userType, profileImageURL):
    r = requests.post(f"http://{endpoint}:5000/api/v1/createAccount", data={"username": user, "password": password, "realName": realName, "userType": userType, "profileImageURL": profileImageURL})
    return r.json()["result"]

print(testCreateAccount("trent", "demo123", "Trent Wiles", "student", "https://trentwil.es/a/FI3S64vsT4.png")) # Expected to return "Username exists"
print(testCreateAccount("trent" + str(random.randint(0,1000000)), "demo123", "Trent Wiles", "student", "https://trentwil.es/a/FI3S64vsT4.png"))

def testListUsers():
    return requests.get(f"http://{endpoint}:5000/api/v1/listAllUsers").json()

print(testListUsers())

def testCreateRequest(username, title, description, tags):
    return requests.post(f"http://{endpoint}:5000/api/v1/createNewRequest", data={"username": username, "title": title, description: "description", "tags": tags})