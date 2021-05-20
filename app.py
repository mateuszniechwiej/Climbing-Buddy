import os
from flask import Flask, flash, render_template,\
 redirect, request, session, url_for
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
@app.route("/events")
def events():
    """
    Renders events page
    """
    events = mongo.db.events.find()

    return render_template("events.html", events=events)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    registeration page cheking if account exits
     and if not allowing user to register.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user:
            flash("Username with this name already exists", "error")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password == confirm_password:
            new_member = {
                # using the name= "" attribiute to grab the correct username,email and password
                "username": request.form.get("username").lower(),
                "user_email": request.form.get("email").lower(),
                "password": generate_password_hash(request.form.get("password")),
            }
            # insert new member into Database
            mongo.db.users.insert_one(new_member)
            # user 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Successfully registered!!!", "message")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Passwords Don't Match", "error")
            return redirect(url_for("register"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login user after checking if user in DB
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get(
                    "username")), "message")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Inccorect Password and/or User", "error")
                return redirect(url_for("login"))

        else:
            flash("Inccorect Password and/or User", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Taking session user's username and email from DataBase
    """
    username = mongo.db.users.find_one({"username": session["user"] })

    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))
#TODO: Add raised climbing searches and for admin also climbing events


@app.route("/logout")
def logout():
    """
    To logout profile, remove the user session cookies and
    return to login page.
    """
    flash("You've been logged out.See you again", "message")
    session.pop("user")
    return redirect(url_for("login"))

