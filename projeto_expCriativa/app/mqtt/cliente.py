# app/mqtt/client.py

import json

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

def get_mqtt_data():
    return {
        "temperature": temperature,
        "huminity": huminity
    }

def publish_message(topic, message):
    return mqtt_instance.publish(topic, message)
