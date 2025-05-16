# app/routes/user_routes.py

from flask import Blueprint, request, render_template, redirect, session
from app.controllers.user_controller import (
    handle_login, handle_add_user, handle_list_users, handle_remove_user
)
from app.auth.decorators import admin_required

user_bp = Blueprint("user", __name__, template_folder="../views/templates")

@user_bp.route('/')
def index():
    return render_template("login.html")

@user_bp.route('/home')
def home():
    return render_template('home.html')

@user_bp.route('/validated_user', methods=['POST'])
def validated_user():
    if handle_login(request.form):
        session['user'] = request.form['user']
        session['admin'] = (request.form['user'] == 'admin')
        return render_template('home.html')
    return '<h1>Invalid credentials!</h1>'

@user_bp.route('/register_user')
def register_user():
    return render_template("register_user.html")

@user_bp.route('/add_user', methods=['GET', 'POST'])
@admin_required
def add_user():
    if request.method == 'POST':
        users = handle_add_user(request.form)
        return f'Usuário {request.form["user"]} adicionado com sucesso!'
    return render_template("user.html", devices=handle_list_users())

@user_bp.route('/list_users')
def list_users():
    return render_template("user.html", devices=handle_list_users())

@user_bp.route('/remove_user')
@admin_required
def remove_user():
    return render_template("remove_user.html", devices=handle_list_users())

@user_bp.route('/del_user', methods=['POST'])
@admin_required
def del_user():
    users = handle_remove_user(request.form['user'])
    return render_template("user.html", devices=users)
