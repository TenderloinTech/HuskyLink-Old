from flask import Flask, request, Response
import psycopg2
import json
import time
import random

# Create a Flask app
app = Flask(__name__)



# Define a route
@app.route('/')
def hello_world():
    return Response(json.dumps({"online": True}), content_type="application/json")

@app.route("/api/v1/login", methods=["POST"])
def login():
    user = request.form.get('username').lower()
    password = request.form.get('password')

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select * from users where username='{user}'")
        res = cur.fetchall()
        conn.commit()
        print(res)
        if len(res) != 1:
            return Response(json.dumps({"result": {"password": False}}), content_type="application/json")
        if res[0][2] == password:
            return Response(json.dumps({"result": {"password": True}}), content_type="application/json")
    return Response(json.dumps({"result": {"password": False, "returnedPassword": password}}), content_type="application/json")

@app.route("/api/v1/createAccount", methods=["POST"])
def create():

    # Parameters Required
    user = request.form.get('username')
    realName = request.form.get('realName')
    password = request.form.get('password')
    createdAt = round(time.time())
    userType = request.form.get("userType")
    profileImageURL = request.form.get("profileImageURL")
    isBanned = False
    userRole = request.form.get("userRole")


    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select * from users where username='{user}'")
        res = cur.fetchall()
        conn.commit()
        if len(res) != 0:
            if res[0][0] == user:
                return Response(json.dumps({"result": {"success": False, "message": "Username exists"}})), 400

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"insert into users (username, realName, pass, createdAt, userType, profileImageURL, isBanned) values ('{user}', '{realName}', '{password}', {createdAt}, '{userType}', '{profileImageURL}', {isBanned})")
        conn.commit()
    return Response(json.dumps({"result": {"success": True, "message": "ok", "createdAt": createdAt}}), content_type="application/json")

@app.route("/api/v1/getUserInfo/<user>", methods=["GET"])
def uInfo(user):
    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select username, realName, createdAt, userType, profileImageURL, isBanned, userRole from users where username='{user}'")
        res = cur.fetchall()
        conn.commit()
        return Response(json.dumps(res), content_type="application/json")


@app.route("/api/v1/listAllUsers", methods=["GET"])
def lists():
    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select username, realName, createdAt, userType, profileImageURL, isBanned, userRole from users")
        res = cur.fetchall()
        conn.commit()
        return Response(json.dumps(res), content_type="application/json")

@app.route("/api/v1/sortByRole/<role>")
def sortRole(role):
    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select username, realName, createdAt, userType, profileImageURL, isBanned, userRole from users where role='{role}'")
        res = cur.fetchall()
        conn.commit()
        return Response(json.dumps(res), content_type="application/json")

@app.route("/api/v1/searchUsers")
def searchUsers():
    q = request.args.get("q").lower()

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    hits = []

    with conn.cursor() as cur:
        cur.execute(f"select * from requests")
        res = cur.fetchall()
        conn.commit()

        for x in res:
            if q in x[0] or q in x[1]:
                if x not in hits:
                    hits.append(x)

        return Response(json.dumps(hits), content_type="application/json")

@app.route("/api/v1/createNewRequest", methods=["POST"])
def createReq():
    # Request params

    username = request.form.get('uniqueUserID')
    title = request.form.get("title")
    description = request.form.get("description")
    tags = request.form.get("tags")
    createdAt = round(time.time())
    isActive = True
    randomID = random.randint(0,10000000000)

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"insert into requests (userUniqueID, title, description, tags, createdAt, isActive, randomID) values ('{username}', '{title}', '{description}', '{tags}', {createdAt}, {isActive}, {randomID})")
        conn.commit()

    return Response(json.dumps({"result": {"uniqueID": randomID}}))
    
@app.route("/api/v1/listRequests")
def listRequests():
    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select * from requests")
        res = cur.fetchall()
        conn.commit()
        return Response(json.dumps(res), content_type="application/json")

@app.route("/api/v1/sortRequestsByTag") # ?tags=tag1,tag2
def sortRequests():
    tags = request.args.get("tags").split(",")
    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    hits = []

    with conn.cursor() as cur:
        cur.execute(f"select * from requests")
        res = cur.fetchall()
        conn.commit()

        for x in res:
            for y in x[3]:
                if y in tags and x not in hits:
                    hits.append(x)

        return Response(json.dumps(hits), content_type="application/json")

@app.route("/api/v1/searchRequests")
def searchRequests():
    search = request.args.get("q")

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    hits = []

    with conn.cursor() as cur:
        cur.execute(f"select * from requests")
        res = cur.fetchall()
        conn.commit()

        for x in res:
            if search in x[0] or search in x[1]:
                if x not in hits:
                    hits.append(x)

        return Response(json.dumps(hits), content_type="application/json")
# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')