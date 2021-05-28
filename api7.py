from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from collections import namedtuple

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:user@localhost/uvruteo"
db = SQLAlchemy(app)


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

@app.route("/obtieneTodosLosSitiosInteres")
def obtieneTodosLosSitiosInteres():  
    result = db.session.execute("""SELECT row_to_json(fc)
             FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
             FROM (SELECT 'Feature' As type
                , ST_AsGeoJSON(lg.the_geom)::json As geometry
                , row_to_json((SELECT l FROM (SELECT osm_id , name, type ) As l
                  )) As properties
               FROM sitiosinteres_univalle As lg  where ST_IsValid(the_geom) ) As f )  As fc;""" )
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    return jsonify(records[0].row_to_json)
    
@app.route("/obtieneSitiosInteres/<sitiointeres>")
def obtieneSitiosInteres(sitiointeres):  
    result = db.session.execute("""SELECT row_to_json(fc)
             FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
             FROM (SELECT 'Feature' As type
                , ST_AsGeoJSON(lg.the_geom)::json As geometry
                , row_to_json((SELECT l FROM (SELECT osm_id , name, type ) As l
                  )) As properties
               FROM sitiosinteres_univalle As lg  where ST_IsValid(the_geom) 
               AND type = :val
               ) As f )  As fc;""", {'val': sitiointeres} )
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    return jsonify(records[0].row_to_json)