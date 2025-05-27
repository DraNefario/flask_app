#user_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user.user import User
from utils.decorators import *


user_ = Blueprint("user_",__name__, template_folder="templates")



@user_.route('/home')
@login_required_custom
def home():
    return render_template('home.html')

@user_.route('/register_user')
def register_user():
    return render_template("register_user.html")

@user_.route('/list_user')
def list_user():
    return render_template('user.html')


@user_.route('/admin_dashboard')
@role_required('admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@user_.route('/estatistica')
@role_required('estatico', 'admin')
def ver_dados_estatisticos():
    return render_template('estatistico.html')
