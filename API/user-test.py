import requests
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


for x in range(10):
    username = generate_random_string(10)
    r = requests.post("https://api.tenderloin.tech/api/v1/createAccount", data={"username": username, "password": "demo123", "email": f"{generate_random_string(4)}.{generate_random_string(5)}@northeastern.edu", "userType": "student", "realName": f"{generate_random_string(7)} {generate_random_string(6)}"})
    print(r.text)