import requests
import random
import string

def firstLast():
    first = ["bob", "john", "tim", "nick", "james"]
    last = ["smith", "gupta", "johnson", "mehta", "patel"]
    return first[random.randint(0, len(first) - 1)] + " " + last[random.randint(0, len(last) - 1)]

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


for x in range(10):
    un = firstLast()
    r = requests.post("https://api.tenderloin.tech/api/v1/createAccount", data={"username": (un + str(random.randint(0,100)) ).split(" ")[1], "password": "demo123", "email": f"{generate_random_string(4)}.{generate_random_string(5)}@northeastern.edu", "userType": "student", "realName": firstLast()})
    print(r.text)