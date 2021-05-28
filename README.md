# geoapi-flask

### Instalación pip
~~~
$ sudo apt-get install python3-pip
$ python3 --version
$ pip3 --version
~~~
### Instalación Flask
~~~
$ sudo pip3 install flask
~~~
### Instalación psycopg3 y Flask-SQLAlchemy
~~~
$ sudo pip3 install git+https://github.com/psycopg/psycopg3.git#subdirectory=psycopg3
$ pip3 install SQLAlchemy
$ pip3 install Flask-SQLAlchemy
~~~
### Exportar variable de entorno
~~~
$ export FLASK_APP=api.py
~~~
### Ejecutar aplicación
~~~
$ flask run --host=0.0.0.0
~~~


