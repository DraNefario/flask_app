from flask import Flask, render_template, request
from actuators import actuators
from login import user
from sensors import sensors

# Inicializa o aplicativo Flask
app = Flask(__name__)

app.register_blueprint(actuators)
app.register_blueprint(user)
app.register_blueprint(sensors)

@app.route('/')
def index():
    return render_template("login.html")

# Página inicial
@app.route('/home')
def home():
    rotas = {'Página Inicial': '/', 'Quarto': '/quarto', 'Sala': '/sala'}
    return render_template("home.html", rotas=rotas)

# Rota para a página do quarto
@app.route('/quarto')
def quarto():
    sensores = {'Umidade': 22, 'Temperatura': 17, 'Luminosidade': 1}
    return render_template("quarto.html", sensores=sensores)

# Rota para a página da sala
@app.route('/sala')
def sala():
    atuadores = {'Servo motor': 90, 'Lâmpada': 1, 'Ar condicionado': 27}
    return render_template("sala.html", atuadores=atuadores)

# Iniciar o app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
