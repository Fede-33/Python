from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

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


# Formulario clasico
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username)>=6 and len(username)<=25 and len(password)>=6 and len(password)<=25:
            return f'Nombre de usuario: {username} Contraseña: {password}'
        else: 
            return render_template('auth/register.html', error = 'El nombre de usuario y la contraseña deben contener entre 6 y 25 caracteres.')    
    elif request.method == 'GET':
        return render_template('auth/register.html')

#Formulario con WTForm
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class FormularioWTForm(FlaskForm):
    username = StringField('Nombre de usuario: ', validators= [DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Contraseña:', validators= [DataRequired(), Length(min=6, max=25)])
    button = SubmitField('Enviar')

@app.route('/auth/register_wtform', methods = ['GET', 'POST'])
def registrar():
    formulario = FormularioWTForm()
    if formulario.validate_on_submit():
        usuario = formulario.username.data
        contras = formulario.password.data
        return f'Nombre de usuario: {usuario} Contraseña: {contras}'

        
    elif request.method == 'GET':
        return render_template('auth/register_wtform.html', form=formulario)    

