from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
      __tablename__ = 'user'
      id = db.Column('id', db.Integer, primary_key=True)
      username = db.Column(db.String(50), unique=True)
      email = db.Column(db.String(128), unique=True)
      senha_hash = db.Column(db.String(200))
      is_admin = db.Column(db.Boolean, default=False)

      def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

      def verificar_senha(self, senha):
          return check_password_hash(self.senha_hash, senha)
      