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
    """
    function to load the home page
    """
    return render_template("pages/home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function to check if username exists in database
    if username exists user is redirected to the signin screen
    or a message is shown that registration is successful
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        registration_data = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration_data)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("pages/signup.html", register=True)


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
            flash("User does not exist please sign up")
            return redirect(url_for("register"))

    return render_template("pages/login.html", login=True)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Function to render the profile page for a user
    Shows thier reviews and provides ability to edit them
    If unsuccessful the user is redirected to the login page
    """
    if session["user"]:
        # grab session user from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # get the reviews written by session user
        yarn_reviews = list(mongo.db.yarn.find(
            {"created_by": session["user"]}))
        reviews = list(mongo.db.yarn.find())

        return render_template(
            "pages/profile.html", username=username,
            yarn_reviews=yarn_reviews, reviews=reviews)
    flash("Please log in")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Function to log user out of account
    this ends the session cokkies
    once logged out the user is redirected to the home page
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/yarns", methods=["GET", "POST"])
def yarns():
    """
    function to render the yarn lists
    information on each yarn is retreived from the database
    each yarn is added to its own card
    """
    yarn = list(mongo.db.yarn.find())
    return render_template("pages/yarns.html", yarn=yarn)


@app.route("/add/yarn", methods=["GET", "POST"])
def add_yarn():
    """
    Function that allows the user to add a new yarn to the database
    a form allows the user to add the information about a yarn in the correct
    format for the database.
    A message is shown to the user to see
    that their submission has been successful
    """
    if request.method == "POST":
        yarn = {
            "yarn_name": request.form.get("yarn_name"),
            "yarn_producer": request.form.get("yarn_producer"),
            "yarn_weight": request.form.get("yarn_weight"),
            "yarn_colour": request.form.get("yarn_colour"),
            "yarn_review": request.form.get("yarn_review"),
            "created_by": session["user"]
        }
        mongo.db.yarn.insert_one(yarn)
        flash("Yarn Successfully Added to the Library")

    return render_template("pages/addyarn.html", add_yarn=True)


@app.route("/edit/yarn/<yarn_id>", methods=["GET", "POST"])
def edit_yarn(yarn_id):
    """
    Function that allows the user to edit a yarn in the database
    a form allows the user to add the information about a yarn in the correct
    format for the database.
    A message is shown to the user to see
    that their submission has been successful
    """
    if request.method == "POST":
        yarn_createdby = mongo.db.yarn.find_one({"_id": ObjectId(yarn_id)})
        if session["user"] == yarn_createdby["created_by"]:
            yarn = {
                "yarn_name": request.form.get("yarn_name"),
                "yarn_producer": request.form.get("yarn_producer"),
                "yarn_weight": request.form.get("yarn_weight"),
                "yarn_colour": request.form.get("yarn_colour"),
                "yarn_review": request.form.get("yarn_review"),
                "created_by": session["user"]
            }
            mongo.db.yarn.update({"_id": ObjectId(yarn_id)}, yarn)
            flash("Yarn Successfully Updated")
        else:
            flash("Not authorised to update this yarn")

    yarn = mongo.db.yarn.find_one({"_id": ObjectId(yarn_id)})
    return render_template("pages/edit-yarn.html/", yarn=yarn)


@app.route("/delete/yarn/<yarn_id>", methods=["GET", "POST"])
def delete_yarn(yarn_id):
    """
    Function to delete a yarn from the database
    A message is shown to the user to show that
    the deletion has been successful
    """
    yarn_createdby = mongo.db.yarn.find_one({"_id": ObjectId(yarn_id)})
    if session["user"] == yarn_createdby["created_by"]:
        mongo.db.yarn.remove({"_id": ObjectId(yarn_id)})
        flash("Yarn Successfully Deleted")
    else:
        flash("Not authorised to delete this yarn")
    return redirect(url_for("yarns"))


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders error.html with 404 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 404


@app.errorhandler(500)
def server_error(error):
    """
    Renders error.html with 500 message.
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
