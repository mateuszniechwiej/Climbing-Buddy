import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
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
    registeration page cheking if account exits and if not allowing user to register.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user:
            flash("Username with this name already exists")
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
            flash("Successfully registered!!!")
        else:
            flash("Passwords Don't Match")
            return redirect(url_for("register"))
    return render_template("register.html")
