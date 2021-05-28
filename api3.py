from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    return 'Pagina Principal'

@app.route('/saludo')
def saludo_bienvenida():
    return '<h1>Hola Clase Geoinformacion</h1>'

@app.route('/saludo/<usuario>')
def saludo_personalizado(usuario):
    return 'Hola <b> %s <b>' % escape(usuario)