import requests, random, json

for x in range(len("hellooooo")):
    r = requests.post("https://api.tenderloin.tech/api/v1/createNewRequest", data={"username": "gutpa87", "title": "Help me with my code!", "description": "I need some help with my code! I cant seem to figure out reactConsole, maybe someone here can help?", "tags": json.dumps(["khoury", "reactConsole"]) } )
    print(r.text)