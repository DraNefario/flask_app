# app/models/atuador_model.py

atuadores = []

def add_atuador(atuador):
    atuadores.append(atuador)

def get_atuadores():
    return atuadores

def remove_atuador(nome):
    global atuadores
    atuadores = [a for a in atuadores if a['nome'] != nome]
