# app/controllers/user_controller.py

from models.iot.user_model import validate_user, add_user, get_users, remove_user

def handle_login(form):
    username = form['user']
    password = form['password']
    return validate_user(username, password)

def handle_add_user(form):
    add_user(form['user'], form['password'])
    return get_users()

def handle_list_users():
    return get_users()

def handle_remove_user(username):
    remove_user(username)
    return get_users()
