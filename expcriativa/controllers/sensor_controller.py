#sensors_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors import Sensor
from utils.decorators import *


sensor_ = Blueprint("sensor_",__name__, template_folder="templates")

@sensor_.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor_.route('/add_sensor', methods=['POST'])
def add_sensor():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, topic, unit, is_active )

    sensors = Sensor.get_sensors()
    return render_template("sensors.html")

@sensor_.route('/list_sensors')
def sensors():
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors = sensors)

