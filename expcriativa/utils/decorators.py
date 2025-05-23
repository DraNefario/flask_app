# utils/decorators.py

from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("user_.index"))  # rota de login
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("user_.home"))  # redireciona se não for admin
        return f(*args, **kwargs)
    return decorated_function
