#sensors_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors import Sensor
from utils.decorators import *


sensor_ = Blueprint("sensor_",__name__, template_folder="templates")

@sensor_.route('/register_sensor')
@role_required('admin', 'operador', 'estatistico')
def register_sensor():
    return render_template("register_sensor.html")

@sensor_.route('/add_sensor', methods=['POST'])
@role_required('admin', 'operador', 'estatistico')
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
@role_required('admin', 'operador', 'estatistico')
def sensors():
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors = sensors)

@sensor_.route('/edit_sensor')
@role_required('admin', 'operador', 'estatistico')
def edit_sensor():
    id = request.args.get('id', None)
    sensor = Sensor.get_single_sensor(id)
    return render_template("update_sensor.html", sensor = sensor)

@sensor_.route('/update_sensor', methods=['POST'])
@role_required('admin', 'operador', 'estatistico')
def update_sensor():
    id = request.form.get("id")
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False
    sensors = Sensor.update_sensor(id, name, brand, model, topic, unit, is_active )
    return render_template("sensors.html", sensors = sensors)

@sensor_.route('/del_sensor', methods=['GET'])
@role_required('admin', 'operador', 'estatistico')
def del_sensor():
    id = request.args.get('id', None)
    sensors = Sensor.delete_sensor(id)
    return render_template("sensors.html", sensors = sensors)



