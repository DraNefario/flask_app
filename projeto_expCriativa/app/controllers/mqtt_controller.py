# app/controllers/mqtt_controller.py

from app.mqtt.cliente import get_mqtt_data, publish_message

def handle_get_mqtt_data():
    return get_mqtt_data()

def handle_publish_message(data):
    return publish_message(data['topic'], data['message'])
