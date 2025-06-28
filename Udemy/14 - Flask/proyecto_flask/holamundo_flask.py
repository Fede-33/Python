from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página principal</h1>'

@app.route('/hello_world')
def hello():
    return '<h2>Hola Mundo</h2>'

@app.route('/contacto')
def contacto():
    return '<h3>Tel. nro. 6546546546</h3>'

@app.route('/hello/<nombre>')
def hola(nombre):
    return f'<h2>Hola, {nombre}</h2>'

@app.route('/datos/<nombre>/<int:edad>')
def data(nombre = None, edad = None):
    if nombre == None and edad == None:
        return 'Hola mundo.'
    elif edad == None:
        return f'Hola {nombre}.'
    else:
        return f'Hola {nombre}, tienes {edad} años.'

from markupsafe import escape

@app.route('/HTML/<path:codigo>')
def programa(codigo):
    return f'Codigo: {escape(codigo)}'
    

