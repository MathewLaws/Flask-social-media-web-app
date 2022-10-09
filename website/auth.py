from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=user_name).first()

        if user:
            if password == user.password:
                flash("Logged in Succesfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))

            else:
                flash("Incorrect password", category="error")
        else:
            flash("User does not exist", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=user_name).first()
        if user:
            flash("username taken!", category="error")
        elif len(user_name) < 6:
            flash("username too short", category="error")
        elif len(password) < 6:
            flash("password too short", category="error")
        else:
            new_user = User(username=user_name, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Logged in Succesfully!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign-up.html", user=current_user)