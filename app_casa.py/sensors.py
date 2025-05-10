#sensors.py
from flask import Blueprint, request, render_template, redirect, url_for, session
from auth import admin_required, login_required


sensors = Blueprint("sensor",__name__, template_folder="templates")

# Lista de sensores cadastrados
sensores = []

# Rota para cadastrar sensor
@sensors.route('/register_sensor')
@admin_required
def register_sensor():
    return render_template('register_sensor.html')

# Rota para adicionar sensor
@sensors.route('/add_sensor', methods=['POST'])
@admin_required
def add_sensor():
    global sensores
    nome = request.form['nome']
    tipo = request.form['tipo']
    valor = request.form['valor']

    sensor = {'nome': nome, 'tipo': tipo, 'valor': valor}
    sensores.append(sensor)  # Adiciona o sensor na lista
    return render_template('sensors.html', sensores=sensores)

# Rota para listar sensores
@sensors.route('/list_sensors')
@admin_required
def list_sensors():
    return render_template("sensors.html", sensores=sensores)

# Rota para remover sensor
@sensors.route('/remove_sensor')
@admin_required
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensores)

@sensors.route('/del_sensor', methods=['POST'])
@admin_required
def del_sensor():
    global sensores
    nome_sensor = request.form['nome']
    # Remove o sensor baseado no nome
    sensores = [sensor for sensor in sensores if sensor['nome'] != nome_sensor]
    return render_template("sensors.html", devices=sensores)
