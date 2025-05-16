# app/models/user_model.py

users = {
    'admin': 'admin123',
    'user1': '1234'
}

def validate_user(username, password):
    return username in users and users[username] == password

def add_user(username, password):
    users[username] = password

def get_users():
    return users

def remove_user(username):
    if username in users:
        users.pop(username)
