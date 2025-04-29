from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired()])
    password = PasswordField('Senha', validators=[InputRequired()])
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Senha', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirme a senha', validators=[
        InputRequired(), EqualTo('password', message='Senhas devem coincidir.')
    ])
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Cadastrar')
