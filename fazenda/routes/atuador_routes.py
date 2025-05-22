# app/routes/atuador_routes.py

from flask import Blueprint, request, render_template
from auth.decorators import admin_required
from controllers.atuador_controller import handle_add_atuador, handle_list_atuadores, handle_remove_atuador

atuadores_bp = Blueprint("atuadores", __name__, template_folder="templates")

@atuadores_bp.route('/register_atuador')
@admin_required
def register_atuador():
    return render_template('register_atuador.html')

@atuadores_bp.route('/add_atuador', methods=['POST'])
@admin_required
def add_atuador_route():
    atuadores = handle_add_atuador(request.form)
    return render_template('atuadores.html', atuadores=atuadores)

@atuadores_bp.route('/list_actuators')
def list_atuadores():
    atuadores = handle_list_atuadores()
    return render_template("atuadores.html", atuadores=atuadores)

@atuadores_bp.route('/remove_atuador')
@admin_required
def remove_atuador():
    atuadores = handle_list_atuadores()
    return render_template("remove_atuador.html", devices=atuadores)

@atuadores_bp.route('/del_atuador', methods=['POST'])
@admin_required
def del_atuador():
    atuadores = handle_remove_atuador(request.form['nome'])
    return render_template("atuadores.html", devices=atuadores)
