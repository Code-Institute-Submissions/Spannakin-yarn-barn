import os
from flask import (Flask, render_template, redirect, request, url_for, session,
                   flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function to check if username exists in database
    if username exists user is redirected to the signin screen
    or a message is shown that registration is successful. 
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("pages/signin.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function to check if username exists in the database
    and ensures that password input by user matches the database.
    if both these are true the user is redirected to the profile page.
    if eith of these are not true then an error message is passed to
    the user to try again or register as a new user.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/signin.html", login = True)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
    {"username": session["user"]})["username"] 

    if session["user"]:
        return render_template("pages/profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/yarns", methods=["GET", "POST"])
def yarns():
    return render_template("pages/yarns.html", yarns=yarns)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"))

