from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from . import db
from .models import User

views = Blueprint("views", __name__, template_folder="templates")


@views.route("/home")
@views.route("/")
def home():
    return render_template("index.html")


@views.route("/profile/user/<username>")
@login_required
def profile(username):
    return render_template("profile.html")


@views.route("/delete")
@login_required
def delete():
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    flash("You deleted your account!", "success")
    return redirect(url_for("views.home"))
