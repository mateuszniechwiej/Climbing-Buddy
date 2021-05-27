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
    events = list(mongo.db.events.find())

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


@app.route("/add_event",methods=["GET","POST"])
def add_event():
    if request.method == "POST":
        event = {
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_location": request.form.get("event_location"),
            "event_description": request.form.get("event_description"),
            "event_type":request.form.get("event_type")  
        }
        mongo.db.events.insert_one(event)
        flash("Event Created!!!", "message")
        return redirect(url_for("add_event"))
    return render_template("add_event.html")


@app.route("/edit_event/<event_id>", methods=["GET","POST"])
def edit_event(event_id):
    """
    Allows admin to update and delete climbing events.
    """
    if request.method == "POST":
        submit = {
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_location": request.form.get("event_location"),
            "event_description": request.form.get("event_description"),
            "event_type":request.form.get("event_type")  
        }
        mongo.db.events.update({"_id": ObjectId(event_id)}, submit)
        flash("Event Successfully updated!!!", "message")

    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_event.html", event=event)


@app.route("/delete_event/<event_id>")
def delete_event(event_id):
    mongo.db.events.remove({"_id": ObjectId(event_id)})
    flash("Event successfully removed", "message")
    return redirect(url_for("events"))


@app.route("/climbs")
def climbs():
    """
    Renders climbs events page
    """
    climbs = list(mongo.db.climbs.find())

    return render_template("climbs.html",climbs=climbs)


@app.route("/search_climber",methods=["GET","POST"])
def search_climber():
    """
    Allows users to raise a climbing partner search event
    """
    if request.method == "POST":
        full_equip = "yes" if request.form.get("full_equip") else "no"
        climb = {
            "climb_date": request.form.get("climb_date"),
            "climb_time": request.form.get("climb_time"),
            "climb_type": request.form.get("climb_type"),
            "climb_location": request.form.get("climb_location"),
            "climb_description": request.form.get("climb_description"),
            "full_equip": full_equip,
            "created_by": session["user"]
        }
        mongo.db.climbs.insert_one(climb)
        flash("Climbing search added", "message")
        return redirect(url_for("climbs"))

    return render_template("search_climber.html")


@app.route("/edit_climb/<climb_id>", methods=["GET", "POST"])
def edit_climb(climb_id):
    if request.method == "POST":
        full_equip = "yes" if request.form.get("full_equip") else "no"
        edit = {
            "climb_date": request.form.get("climb_date"),
            "climb_time": request.form.get("climb_time"),
            "climb_type": request.form.get("climb_type"),
            "climb_location": request.form.get("climb_location"),
            "climb_description": request.form.get("climb_description"),
            "full_equip": full_equip,
            "created_by": session["user"]
        }
        mongo.db.climbs.update({"_id": ObjectId(climb_id)}, edit)
        flash("Climbing request updated", "message")

    climb = mongo.db.climbs.find_one({"_id": ObjectId(climb_id)})
    return render_template("edit_climb.html", climb=climb)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
