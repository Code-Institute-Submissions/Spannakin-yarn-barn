import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get(MONGODB_NAME)
app.config["MONGO_URI"] = os.environ.get(MONGO_URI)
app.secret_key = os.environ.get(SECRET_KEY)

mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug="1")
        