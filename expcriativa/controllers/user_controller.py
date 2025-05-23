#user_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user.user import User

user_ = Blueprint("user_",__name__, template_folder="templates")

@user_.route('/register_user')
def register_user():
    return render_template("register_user.html")