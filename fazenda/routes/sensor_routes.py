# app/routes/sensor_routes.py

from flask import Blueprint, request, render_template
from auth.decorators import admin_required
from controllers.sensor_controller import handle_add_sensor, handle_list_sensors, handle_remove_sensor

sensors_bp = Blueprint("sensors", __name__, template_folder="templates")

@sensors_bp.route('/register_sensor')
@admin_required
def register_sensor():
    return render_template('register_sensor.html')

@sensors_bp.route('/add_sensor', methods=['POST'])
@admin_required
def add_sensor_route():
    sensores = handle_add_sensor(request.form)
    return render_template('sensors.html', sensores=sensores)

@sensors_bp.route('/list_sensors')
@admin_required
def list_sensors():
    sensores = handle_list_sensors()
    return render_template("sensors.html", sensores=sensores)

@sensors_bp.route('/remove_sensor')
@admin_required
def remove_sensor():
    sensores = handle_list_sensors()
    return render_template("remove_sensor.html", devices=sensores)

@sensors_bp.route('/del_sensor', methods=['POST'])
@admin_required
def del_sensor():
    sensores = handle_remove_sensor(request.form['nome'])
    return render_template("sensors.html", devices=sensores)
