# app/controllers/sensor_controller.py

from models.iot.sensor_model import add_sensor, get_sensores, remove_sensor

def handle_add_sensor(form):
    sensor = {
        'nome': form['nome'],
        'tipo': form['tipo'],
        'valor': form['valor']
    }
    add_sensor(sensor)
    return get_sensores()

def handle_list_sensors():
    return get_sensores()

def handle_remove_sensor(nome):
    remove_sensor(nome)
    return get_sensores()
