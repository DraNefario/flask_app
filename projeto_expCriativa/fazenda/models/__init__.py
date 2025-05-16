# app/__init__.py

from flask import Flask
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

from routes.sensor_routes import sensors_bp
from routes.atuador_routes import atuadores_bp
from routes.user_routes import user_bp
from routes.mqtt_routes import mqtt_routes_bp
from mqtt.cliente import init_mqtt




def create_app():
    app = Flask(__name__, static_folder='app/views/static', template_folder='app/views/templates')
    app.secret_key = 'newton'

    # Configurações MQTT
    app.config.update({
        'MQTT_BROKER_URL': 'broker.emqx.io',
        'MQTT_BROKER_PORT': 1883,
        'MQTT_USERNAME': 'thomas',
        'MQTT_PASSWORD': '',
        'MQTT_KEEPALIVE': 60,
        'MQTT_TLS_ENABLED': False,
        'MQTT_PATH': '/mqtt'
    })

    # Inicializações
    socketio = SocketIO(app, async_mode='eventlet')
    mqtt = Mqtt(app)

    # Blueprints
    app.register_blueprint(sensors_bp)
    app.register_blueprint(atuadores_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(mqtt_routes_bp)

    init_mqtt(app, mqtt)

    return app, socketio
