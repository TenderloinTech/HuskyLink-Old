from flask import Flask, request, Response
import psycopg2
import json

# Create a Flask app
app = Flask(__name__)



# Define a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/api/v1/login", methods=["POST"])
def login():
    user = request.form.get('username')
    password = request.form.get('password')

    conn = psycopg2.connect(json.loads(open("API/config.json").read())["cockroach"])

    with conn.cursor() as cur:
        cur.execute(f"select * from testlogin where username='{user}'")
        res = cur.fetchall()
        conn.commit()
        print(res)
    return Response(json.dumps({"result": res}), content_type="application/json")



# Run the app
if __name__ == '__main__':
    app.run()