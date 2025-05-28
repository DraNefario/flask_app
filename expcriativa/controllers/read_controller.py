#reads_controller.py
from flask import Blueprint, request, render_template
from models.iot.read import Read
from models.iot.sensors import *

read_ = Blueprint("read",__name__, template_folder="views")

@read_.route("/history_read")
def history_read():
    sensors = Sensor.get_sensors()
    read = {}
    return render_template("tr.html", sensors = sensors, read = read)

@read_.route("/get_read", methods=['POST'])
def get_read():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        read = Read.get_read(id, start, end)

        sensors = Sensor.get_sensors()
        return render_template("tr.html", sensors = sensors, read = read)


