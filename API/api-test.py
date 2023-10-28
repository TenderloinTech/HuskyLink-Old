import requests

def testLogin(user, password):
    r = requests.post("http://localhost:5000/api/v1/login", data={"username": user, "password": password})
    return r.json()["result"]["password"]

print(testLogin("sj", "s")) # Expected to return False
print(testLogin("james", "s")) # Expected to return False
print(testLogin("james", "admin123")) # Expected to return True