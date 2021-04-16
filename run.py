"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo desde Flask por Jeferson Cueva</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

@app.route('/listado')
def lista():
    return  "<h2>Carreras de la UTPL de la Área Técnica</h2> <ul> <li type='circle'>Arquitectura</li> <li type='circle'>Arte y Diseño</li> <li type='circle'>Electrónica y Telecomunicaciones</li> <li type='circle'>Geología y Minas</li> <li type='circle'>Ingeniería Civil</li> <li type='circle'>Sistemas Informátiocos</li></ul>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
