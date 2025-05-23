#auth_controller.py
from flask import Blueprint, render_template, request, redirect, session, url_for
from models.db import db
from models.user.user import User

auth_ = Blueprint('auth', __name__, template_folder="templates")


@auth_.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        senha = request.form["senha"]

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return render_template("register_user.html", erro="Usuário ou email já cadastrado")

        is_admin = User.query.count() == 0  

        novo_usuario = User(username=username, email=email, is_admin=is_admin)
        novo_usuario.set_senha(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("user_.index"))

    return render_template("register_user.html")

@auth_.route("/validate_user", methods=["POST"])
def validated_user():
    username = request.form["username"]
    senha = request.form["senha"]
    user = User.query.filter_by(username=username).first()
    if user and user.verificar_senha(senha):
        session["user_id"] = user.id
        session["admin"] = user.is_admin
        return redirect(url_for("user_.home"))
    return render_template("login.html", erro="Usuário ou senha inválidos")
