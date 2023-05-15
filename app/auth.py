from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user

from . import db, login_manager
from .forms import LoginForm, RegisterForm
from .models import User

auth = Blueprint("auth", __name__, template_folder="templates")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        username = current_user.username
        return redirect(url_for("views.profile", username=username))
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                flash("You have logged into your account!", "success")
                return redirect(url_for("views.home"))
            else:
                flash("Wrong password!", "warning")
        else:
            flash("This account does not exist!", "warning")
    return render_template("login.html", form=form)


@auth.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        username = current_user.username
        return redirect(url_for("views.profile", username=username))
    form = RegisterForm()
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("This account already exists!", "warning")
        else:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Account created successfully", "success")
            return redirect(url_for("views.home"))
    return render_template("sign-in.html", form=form)


@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You logged out of your account!", "success")
    return redirect(url_for("views.home"))
