from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Pagina Principal'

@app.route('/saludo')
def saludo_bienvenida():
    return 'Hola Clase Geoinformacion'  