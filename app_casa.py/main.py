from flask import Flask
from actuators import actuators
from login import user
from sensors import sensors
from mqtt_routes import mqtt_routes, init_mqtt

from flask_mqtt import Mqtt

app = Flask(__name__)

app.secret_key = 'newton'


# MQTT Config
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'  
app.config['MQTT_BROKER_PORT'] = 8084  
app.config['MQTT_USERNAME'] = 'thomas' 
app.config['MQTT_PASSWORD'] = ''  
app.config['MQTT_KEEPALIVE'] = 60  
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_PATH'] = '/mqtt'  

mqtt = Mqtt(app)

# Register blueprints
app.register_blueprint(actuators)
app.register_blueprint(user)
app.register_blueprint(sensors)
app.register_blueprint(mqtt_routes)

# Inicia MQTT listeners
init_mqtt(app, mqtt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
