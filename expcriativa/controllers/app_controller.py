from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager

from models.db import *
from models.user.user import User
from models.iot.read import Read
from models.iot.write import Write
from utils.decorators import *

from controllers.sensor_controller import sensor_
from controllers.actuator_controller import actuator_
from controllers.auth_controller import auth_
from controllers.user_controller import user_
from controllers.read_controller import read_
from controllers.write_controller import write_

from flask_mqtt import Mqtt
import json

temperature = None
huminity = None


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
    app.register_blueprint(actuator_, url_prefix='/')
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(auth_, url_prefix='/')
    app.register_blueprint(user_, url_prefix='/')
    app.register_blueprint(read_, url_prefix='/')
    app.register_blueprint(write_, url_prefix='/')
    
    @app.route('/')
    def index():
        return render_template("inicio.html")
    
    @app.route('/login')
    def login():
        return render_template("login.html")
    
    app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = 'SistemaIrrigacaoAutomatica'  
    app.config['MQTT_PASSWORD'] = ''  
    app.config['MQTT_KEEPALIVE'] = 60 
    app.config['MQTT_TLS_ENABLED'] = False  

    mqtt_client= Mqtt()
    mqtt_client.init_app(app)

    topic_subscribe = "/irrigar/sensor"  
    topic_publish = "/irrigar/controle" 


    @app.route('/tr')
    @role_required('admin', 'estatistico')
    def tempo_real():
        global temperature, huminity
        values = {"temperature":temperature, "huminity":huminity}
        return render_template("tr.html", values=values)
    
    @app.route('/publish')
    @role_required('admin', 'operador')
    def publish():
        return render_template('publish.html')

    @app.route('/publish_message', methods=['GET','POST'])
    @role_required('admin', 'operador')
    def publish_message():
        request_data = request.get_json()
        publish_result = mqtt_client.publish("/irrigar/controle", request_data['message'])
        try:
            with app.app_context():
                Write.save_write("/irrigar/controle", request_data['message'])  # sem float()
        except:
            pass
        return jsonify(publish_result)




    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Broker Connected successfully')
            mqtt_client.subscribe(topic_subscribe) 
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
            if(js["sensor"]=="/irrigar/temperature"):
                temperature = js["valor"]
            elif(js["sensor"]=="/irrigar/huminity"):
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
