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
    registeration page for users without account 
    """
    return render_template("register.html")
