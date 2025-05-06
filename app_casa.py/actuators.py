#actuators.py
from flask import Blueprint, request, render_template, redirect, url_for


actuators = Blueprint("atuador",__name__, template_folder="templates")

# Lista de atuadores cadastrados
atuadores = []

# Rota para cadastrar atuador
@actuators.route('/register_atuador')
def register_atuador():
    return render_template('register_atuador.html')

# Rota para adicionar sensor
@actuators.route('/add_atuador', methods=['POST'])
def add_atuador():
    global atuadores
    nome = request.form['nome']
    tipo = request.form['tipo']
    valor = request.form['valor']

    atuador = {'nome': nome, 'tipo': tipo, 'valor': valor}
    atuadores.append(atuador)  # Adiciona o sensor na lista
    return render_template('atuadores.html', atuadores=atuadores)

# Rota para listar atuadores
@actuators.route('/list_actuators')
def list_actuators():
    return render_template("atuadores.html", atuadores=atuadores)

# Rota para remover atuador
@actuators.route('/remove_atuador')
def remove_atuador():
    return render_template("remove_atuador.html", devices=atuadores)

@actuators.route('/del_atuador', methods=['POST'])
def del_atuador():
    global atuadores
    nome_atuador = request.form['nome']
    # Remove o atuador baseado no nome
    atuadores = [atuador for atuador in atuadores if atuador['nome'] != nome_atuador]
    return render_template("atuadores.html", devices=atuadores)
