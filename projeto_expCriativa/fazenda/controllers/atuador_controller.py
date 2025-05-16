# app/controllers/atuador_controller.py

from models.iot.atuador_model import add_atuador, get_atuadores, remove_atuador

def handle_add_atuador(form):
    atuador = {
        'nome': form['nome'],
        'tipo': form['tipo'],
        'valor': form['valor']
    }
    add_atuador(atuador)
    return get_atuadores()

def handle_list_atuadores():
    return get_atuadores()

def handle_remove_atuador(nome):
    remove_atuador(nome)
    return get_atuadores()
