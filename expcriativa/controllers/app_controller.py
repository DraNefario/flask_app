from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager

from models.db import *
from models.user.user import User
from models.iot.read import Read

from controllers.sensor_controller import sensor_
from controllers.actuator_controller import actuator_
from controllers.auth_controller import auth_
from controllers.user_controller import user_

from flask_mqtt import Mqtt
import json

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
    
    app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = 'thomas'  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    mqtt_client= Mqtt()
    mqtt_client.init_app(app)

    topic_subscribe = "/thomas/"

    @app.route('/tr')
    def tempo_real():
        global temperature, huminity
        values = {"temperature":temperature, "huminity":huminity}
        return render_template("tr.html", values=values)


    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Connected successfully')
            mqtt_client.subscribe(topic_subscribe) # subscribe topic
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_disconnect()
    def handle_disconnect(client, userdata, rc):
        print("Disconnected from broker")


    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        if(message.topic==topic_subscribe):
            global temperature, huminity
            #print(message.payload.decode())
            js = json.loads(message.payload.decode())
            if(js["sensor"]=="/aula_flask/temperature"):
                temperature = js["valor"]
            elif(js["sensor"]=="/aula_flask/huminity"):
                huminity = js["valor"]
            try:
                with app.app_context():
                    Read.save_read(js["sensor"], js["valor"])
            except:
                pass
    
    @app.route('/api/latest')
    def latest():
        global temperature, huminity
        return jsonify({
            "temperature": temperature,
            "huminity": huminity
        })
    
    
    
    return app
