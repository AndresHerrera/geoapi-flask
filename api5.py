from flask import Flask , jsonify
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
    
@app.route('/saludo/<usuario>/<int:edad>')
def saludo_personalizado_edad(usuario,edad):
    return 'Hola <b> %s </b> de %d años' % ( escape(usuario) , edad )

@app.route("/contacto")
def datoscontactojson():
    return jsonify({
        "nombre": "Andres",
        "apellido": "Herrera",
        "correo": "fabio.herrera@correounivalle.edu.co",
    })