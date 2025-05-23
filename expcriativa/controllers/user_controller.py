#user_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user.user import User
from utils.decorators import login_required, admin_required


user_ = Blueprint("user_",__name__, template_folder="templates")

@user_.route('/')
def index():
    return render_template("login.html")

@user_.route('/home')
@login_required
def home():
    return render_template('home.html')

@user_.route('/register_user')
def register_user():
    return render_template("register_user.html")