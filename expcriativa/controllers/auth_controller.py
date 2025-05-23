from flask import Blueprint, render_template, request, redirect, session
from models.db import db
from models.user.user import User

auth_ = Blueprint('auth', __name__, template_folder="templates")

@auth_.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        if User.query.filter_by(nome=nome).first():
            return "Usuário já existe"

        is_admin = User.query.count() == 0  

        novo_usuario = User(nome=nome, is_admin=is_admin)
        novo_usuario.set_senha(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect("/login")

    return render_template("user.html")