#controllers.actuator_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.actuators import Actuator

actuator_ = Blueprint("Actuator_", __name__, template_folder="templates")

@actuator_.route('/register_atuator')
def register_sensor():
    return render_template("register_atuator.html")


@actuator_.route('/add_actuator', methods = ['POST'])
def add_actuator():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator.save_actuator(name, brand, model, topic, unit, is_active )

    actuators = Actuator.get_actuators()
    return render_template("atuadores.html", actuators = actuators)