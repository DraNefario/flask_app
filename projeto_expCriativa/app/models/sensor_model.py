# app/models/sensor_model.py

sensores = []

def add_sensor(sensor):
    sensores.append(sensor)

def get_sensores():
    return sensores

def remove_sensor(nome):
    global sensores
    sensores = [s for s in sensores if s['nome'] != nome]
