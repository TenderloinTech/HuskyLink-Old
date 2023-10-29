import requests, random, json

r = requests.post("https://api.tenderloin.tech/api/v1/createNewRequest", data={"username": "trent", "title": "hey whats up my guy", "description": "yoo whats up i need some help with this big project im trying to work on and its using java so lik eyeah give me help bro", "tags": json.dumps(["test", "khoury", "roblox", "linux"]) } )
print(r.text)