#login.py
from flask import Blueprint, request, render_template, session, redirect, url_for
from auth import admin_required, login_required


user = Blueprint("user",__name__, template_folder="templates")

# Dados de usuários cadastrados
users = {
    'admin': 'admin123',
    'user1': '1234'
}

@user.route('/')
def index():
    return render_template("login.html")

# Rota para validar usuário
@user.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            session['user'] = user
            session['admin'] = (user == 'admin')
            return render_template('home.html')
        else:
            return '<h1>Invalid credentials!</h1>'
    else:
        return render_template('login.html')

# Rota para cadastrar usuário
@user.route('/register_user')
def register_user():
    return render_template("register_user.html")

# Rota para adicionar usuário
@user.route('/add_user', methods=['GET', 'POST'])
@admin_required
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        users[user] = password
        return f'Usuário {user} adicionado com sucesso!'
    return render_template("user.html", devices=users)

# Rota para listar usuários
@user.route('/list_users')
def list_users():
    return render_template("user.html", devices=users)

# Rota para remover usuário
@user.route('/remove_user')
@admin_required
def remove_user():
    return render_template("remove_user.html", devices=users)

@user.route('/del_user', methods=['POST'])
@admin_required
def del_user():
    global users
    user = request.form['user']
    if user in users:
        users.pop(user)
    return render_template("user.html", devices=users)