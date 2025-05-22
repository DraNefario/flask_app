# fazenda/models/db.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Instância do SQLAlchemy
db = SQLAlchemy()

def init_db(app: Flask):
    # Configuração da conexão
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test1:test1@localhost:3306/exp3pra3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
