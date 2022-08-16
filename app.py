import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///diary.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Index page | Shows the user's diary
@app.route("/")
@login_required
def index():

    user_id = session["user_id"]

    diaries = db.execute("SELECT time, title, description, img_url FROM diaries WHERE user_id = ?", user_id)

    return render_template("index.html", diaries=diaries)


#Log in page
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Please provide a username", 403)

        elif not request.form.get("password"):
            return apology("Please provide a password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


#Log out page
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


#Register page
@app.route("/register", methods=["GET", "POST"])
def register():

    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if not username:
            return apology('Please type in a username')
        elif not password:
            return apology('Please type in a password')
        elif not confirmation:
            return apology('Please type in your password again')

        if password != confirmation:
            return apology('Passwords do not match')

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect('/')
        except:
            return apology('Username is already in use')

    else:
        return render_template("register.html")


# Diary page | Creates a new page in the user's diary
@app.route("/diary", methods=["GET", "POST"])
def diary():

    if request.method == "POST":

        user_id = session["user_id"]

        time = request.form.get("time")
        title = request.form.get("title")
        description = request.form.get("description")
        img_url = request.form.get("img_url")

        if not request.form.get("time"):
            return apology("Please choose a date", 403)

        elif not request.form.get("title"):
            return apology("Please type in a title", 403)

        elif not request.form.get("description"):
            return apology("Please write something into your Diaream", 403)

        db.execute("INSERT INTO diaries (user_id, time, title, description, img_url) VALUES (?, ?, ?, ?, ?)",
        user_id, time, title, description, img_url)

        return redirect("/")

    else:
        return render_template("diary.html")