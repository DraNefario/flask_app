#app_controller.py
from flask import Flask, render_template, request
from models.db import *
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

    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')
    app.register_blueprint(auth_, url_prefix='/')
    app.register_blueprint(user_, url_prefix='/')
    
    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app
