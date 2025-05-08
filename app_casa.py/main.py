from flask import Flask, render_template, request
from actuators import actuators
from login import user
from sensors import sensors

# Inicializa o aplicativo Flask
app = Flask(__name__)

app.secret_key = 'newton'

app.register_blueprint(actuators)
app.register_blueprint(user)
app.register_blueprint(sensors)

# Iniciar o app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
