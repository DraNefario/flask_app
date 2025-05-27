from functools import wraps
from flask import redirect, url_for
from flask_login import current_user

def login_required_custom(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("user_.index"))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*required_roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("user_.index"))

            if not any(current_user.has_role(role) for role in required_roles):
                return redirect(url_for("user_.home"))

            return f(*args, **kwargs)
        return decorated_function
    return wrapper
