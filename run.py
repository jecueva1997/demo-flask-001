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
    return  "<h2>Carreras de la UTPL</h2> <ul> <li type='circle'>Esto es un tipo de punto.</li> <li type='square'>Este es otro.</li> <li type='disc'>Y este es otro diferente.</li></ul>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
