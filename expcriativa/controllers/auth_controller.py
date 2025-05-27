from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from models.db import db
from models.user.user import User

auth_ = Blueprint('auth', __name__, template_folder="templates")


@auth_.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        senha = request.form["senha"]
        roles = request.form.getlist("roles")  # <- Captura os perfis selecionados

        # Verifica se já existe username ou email
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return render_template("register_user.html", erro="Usuário ou email já cadastrado")

        # Se for o primeiro usuário, adiciona automaticamente o papel admin
        if User.query.count() == 0 and "admin" not in roles:
            roles.append("admin")

        novo_usuario = User(
            username=username,
            email=email,
            roles=",".join(roles)
        )
        novo_usuario.set_senha(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("user_.home"))

    return render_template("register_user.html")


@auth_.route("/validate_user", methods=["POST"])
def validated_user():
    username = request.form["username"]
    senha = request.form["senha"]
    user = User.query.filter_by(username=username).first()

    if user and user.verificar_senha(senha):
        login_user(user)  
        return redirect(url_for("user_.home"))

    return render_template("login.html", erro="Usuário ou senha inválidos")


@auth_.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user_.login"))
