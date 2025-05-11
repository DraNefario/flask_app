# mqtt_routes.py
from flask import Blueprint, render_template, request, jsonify
from flask_mqtt import Mqtt
from auth import admin_required, login_required
import json

mqtt_routes = Blueprint('mqtt_routes', __name__)
temperature = 10
huminity = 10

mqtt_instance = None

def init_mqtt(app, mqtt):
    global mqtt_instance
    mqtt_instance = mqtt  
    
    topic_subscribe = "/aula_flask/"

    @mqtt.on_connect()
    def handle_connect(client, userdata, flags, rc):
        print("Tentando conectar ao MQTT...")
        if rc == 0:
            print("Connected to MQTT broker")
            mqtt.subscribe(topic_subscribe)
        else:
            print("Connection failed with code", rc)

    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        global temperature, huminity
        print(f"[MQTT] Mensagem recebida em {message.topic}: {message.payload.decode()}")
              
        js = json.loads(message.payload.decode())
        if js["sensor"] == "/aula_flask/temperature":
            temperature = js["valor"]
        elif js["sensor"] == "/aula_flask/huminity":
            huminity = js["valor"]
        elif js["sensor"] == "/aula_flask/comando":
            print(f"[COMANDO] Recebido do ESP: {js['valor']}")

@mqtt_routes.route('/tempo_real')
@login_required
def tempo_real():
    global temperature, huminity
    return render_template("tr.html", values={"temperature": temperature, "huminity": huminity})

@mqtt_routes.route('/publish')
@login_required
def publish():
    return render_template('publish.html')

@mqtt_routes.route('/publish_message', methods=['POST'])
@login_required
def publish_message():
    request_data = request.get_json()
    result = mqtt_instance.publish(request_data['topic'], request_data['message'])
    return jsonify(result)
