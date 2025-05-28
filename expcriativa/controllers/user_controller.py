#user_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user.user import User
from utils.decorators import *
from models.db import *


user_ = Blueprint("user_",__name__, template_folder="templates")



@user_.route('/home')
@login_required_custom
def home():
    return render_template('home.html')

@user_.route('/login')
def login():
    return render_template('login.html')

@user_.route('/register_user')
def register_user():
    return render_template("register_user.html")

@user_.route('/list_users')
@role_required('admin')
def list_user():
    users = User.query.all()  # lista de objetos User
    return render_template("user.html", users=users)


@user_.route('/edit_user/<int:user_id>', methods=["GET", "POST"])
@role_required('admin')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        user.roles = ",".join(request.form.getlist("roles"))

        nova_senha = request.form.get("senha")
        if nova_senha:
            user.set_senha(nova_senha)

        db.session.commit()
        return redirect(url_for('/list_users'))

    return render_template("user/edit_user.html", user=user)

@user_.route('/delete_user/<int:user_id>', methods=["POST"])
@role_required('admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('/list_users'))


