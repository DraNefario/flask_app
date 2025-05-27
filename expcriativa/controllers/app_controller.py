from flask import Flask, render_template
from flask_login import LoginManager
from models.db import *
from models.user.user import User
from controllers.sensor_controller import sensor_
from controllers.actuator_controller import actuator_
from controllers.auth_controller import auth_
from controllers.user_controller import user_

def create_app():
    app = Flask(__name__, 
                template_folder="./templates/", 
                static_folder="./static/",
                root_path="./")
    
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    # Configuração do Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user_.home"  

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Rotas e blueprints
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')
    app.register_blueprint(auth_, url_prefix='/')
    app.register_blueprint(user_, url_prefix='/')
    
    @app.route('/')
    def index():
        return render_template("inicio.html")
    
    @app.route('/login')
    def login():
        return render_template("login.html")
    
    return app
