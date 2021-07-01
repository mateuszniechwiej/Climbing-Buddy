import os
from flask import Flask, flash, render_template,\
 redirect, request, session, url_for
from flask_paginate import Pagination, get_page_args
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
ELEMENTS_PER_PAGE = 3

# to learn how to make pagination using flask https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
def get_elements(elements):
    """
    Getting added elements for pagination 
    on events and climbing request pages
    to organize the content.
    """
    page,per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')

    offset = page * ELEMENTS_PER_PAGE - ELEMENTS_PER_PAGE

    return elements[offset: offset + ELEMENTS_PER_PAGE]


def pagination_elements(elements):
    """
    Adding pagination to the long content pages.
    """
    page, per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')
    total = len(elements)

    return Pagination(page=page, per_page=ELEMENTS_PER_PAGE, total=total)    


@app.route("/")
@app.route("/home")
def home():
    """
    Renders home page when main website loaded
    """
    return render_template("index.html")


@app.route("/events")
def events():
    """
    Renders events page and display all events added by admin
    """
    events = list(mongo.db.events.find())
    paginated_events = get_elements(events)
    pagination = pagination_elements(events)
    return render_template("events.html", 
                          events=paginated_events,
                          pagination=pagination)

# FIXME: not every word searched in event description
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    events = list(mongo.db.events.find({"$text": {"$search": query}}))
    paginated_events = get_elements(events)
    pagination = pagination_elements(events)

    return render_template("events.html", events=paginated_events, pagination=pagination)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration page checking if account exits
     and if not allowing user to register.
     checking if password match confirm password.
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
                # using the name="" attribiute to grab the correct
                #  username,email and password
                "username":
                request.form.get("username").lower(),
                "user_email":
                request.form.get("email").lower(),
                "password":
                generate_password_hash(request.form.get("password")),
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
    Login user after checking if user in Database
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
    username = mongo.db.users.find_one({"username": session["user"]})

    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    To logout profile, remove the user session cookies and
    return to login page.
    """
    flash("You've been logged out.See you again", "message")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    """
    Allows admin to add climbing events by getting add_event
    form and stores into DB.Finaly renders add_event.html.
    """
    if request.method == "POST":
        event = {
            "event_date": request.form.get("event_date"),
            "event_location": request.form.get("event_location"),
            "event_description": request.form.get("event_description"),
            "event_type": request.form.get("event_type")
        }
        mongo.db.events.insert_one(event)
        flash("Event Created!!!", "message")
        return redirect(url_for("add_event"))
    return render_template("add_event.html")


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    """
    Allows admin to update climbing events.
    Flash message displays if successful.
    """
    if request.method == "POST":
        submit = {
            "event_date": request.form.get("event_date"),
            "event_location": request.form.get("event_location"),
            "event_description": request.form.get("event_description"),
            "event_type": request.form.get("event_type")
        }
        mongo.db.events.update({"_id": ObjectId(event_id)}, submit)
        flash("Event Successfully updated!!!", "message")

    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_event.html", event=event)


@app.route("/delete_event/<event_id>")
def delete_event(event_id):
    """
    Alows admin to delete event.
    Flash message displays if successful.
    """
    mongo.db.events.remove({"_id": ObjectId(event_id)})
    flash("Event successfully removed", "message")
    return redirect(url_for("events"))


@app.route("/climbs")
def climbs():
    """
    Renders climbs events page and display climbs request raised by
    all registered users.
    """
    climbs = list(mongo.db.climbs.find())
    paginated_climbs = get_elements(climbs)
    pagination = pagination_elements(climbs)
    username = mongo.db.users.find_one({"username": session["user"]})

    return render_template("climbs.html", climbs=paginated_climbs,pagination=pagination, username=username)


@app.route("/filter", methods=["GET", "POST"])
def filter():
    """
    Filters available climbs from select drop dwon menues and autocolpete places location field 
    """
    climb_date = request.form.get("climbing_date")
    climb_type = request.form.get("climbing_style")
    climb_location = request.form.get("climbing_location")
    full_equip = request.form.get("equipment")


    climbs = list(mongo.db.climbs.find({"$or": [{"climb_date": climb_date},
                                                 {"climb_type": climb_type},
                                                 {"climb_location": climb_location},
                                                 {"full_equip": full_equip}]}))

    username = mongo.db.users.find_one({"username": session["user"]})
    
    paginated_climbs = get_elements(climbs)
    pagination = pagination_elements(climbs)


    return render_template("climbs.html", climbs=paginated_climbs, pagination=pagination, username=username)


@app.route("/search_climber", methods=["GET", "POST"])
def search_climber():
    """
    Allows users to add climbing events by getting search climber
    form and stores into DB.Finaly renders search_climber.html.html.
    """
    user_email = (
        mongo.db.users.find_one({"username": session["user"]})["user_email"])
    if request.method == "POST":
        full_equip = "yes" if request.form.get("full_equip") else "no"
        climb = {
            "climb_date": request.form.get("climb_date"),
            "climb_type": request.form.get("climb_type"),
            "climb_location": request.form.get("climb_location"),
            "climb_description": request.form.get("climb_description"),
            "full_equip": full_equip,
            "created_by": session["user"],
            "email": user_email
        }
        mongo.db.climbs.insert_one(climb)
        flash("Climbing search added", "message")
        return redirect(url_for("climbs"))

    return render_template("search_climber.html")


@app.route("/edit_climb/<climb_id>", methods=["GET", "POST"])
def edit_climb(climb_id):
    """
    Allows users to edit the climbing request and updated it in MongoDB.
    """
    if request.method == "POST":
        full_equip = "yes" if request.form.get("full_equip") else "no"
        edit = {
            "climb_date": request.form.get("climb_date"),
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


@app.route("/delete_climb/<climb_id>")
def delete_climb(climb_id):
    """
    Allows users to delete climbing requests created by them.
    Flash message displays if successful.
    """
    mongo.db.climbs.remove({"_id": ObjectId(climb_id)})
    flash("Climb search removed", "message")
    return redirect(url_for("climbs"))


# Error handlers
# Testing errrors by importing abort from flask and return it in homepage
@app.errorhandler(404)
def page_not_found(error):
    error = 404
    error_msg = "I'm sorry but the page you looking for doesn't exist."
    return render_template("error.html", error=error, error_msg=error_msg), 404


@app.errorhandler(500)
def internal_error(error):
    error = 500
    error_msg = "We're sorry! There is an internal server error.\
        please try again later."
    return render_template("error.html",
                           error=error, error_msg=error_msg), 500


@app.errorhandler(Exception)
def other_exceptions(error):
    error_msg = "We're sorry but the error above has occured"
    return render_template("error.html", error=error, error_msg=error_msg)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
