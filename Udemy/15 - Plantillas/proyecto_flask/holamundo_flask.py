from flask import Flask, render_template, url_for
from markupsafe import escape
from datetime import datetime

app = Flask(__name__)

#Filtro:
@app.add_template_filter
def ddmmaaaa(date):
    return date.strftime('%d-%m-%Y')

# app.add_template_filter(ddmmaaaa, 'formato_fecha')

def repetir_cadena(cadena, repetir):
    return cadena * repetir

@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    print(url_for('data'))
    print(url_for('programa', codigo = ''))
    name = 'Pepe '
    friends = ['Alex', 'Pepe', 'Ana', 'José']
    date = datetime.now()
    return render_template('index.html', name = name, friends = friends, date = date, repetir_cadena = repetir_cadena)

@app.route('/hello_world')
def hello():
    return '<h2>Hola Mundo</h2>'

@app.route('/contacto')
def contacto():
    return '<h3>Tel. nro. 6546546546</h3>'

@app.route('/hello/<nombre>')
def hola(nombre):
    return f'<h2>Hola, {nombre}</h2>'

@app.route('/datos')
@app.route('/datos/<nombre>')
@app.route('/datos/<nombre>/<int:edad>')
@app.route('/datos/<nombre>/<int:edad>/<email>')
def data(nombre = None, edad = None, email = None):
    diccionario = {
        'name' : nombre,
        'age' : edad,
        'email' : email
    }
    return render_template('hello.html', my_data = diccionario)

@app.route('/HTML/<path:codigo>')
def programa(codigo):
    return f'Codigo: {escape(codigo)}'
    

