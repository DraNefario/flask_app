from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return '<h1>Acesso negado! Somente administradores.</h1>'
        return f(*args, **kwargs)
    return decorated
