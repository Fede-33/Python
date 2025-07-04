# JINJA2
Motor de Python instalado junto con Flask que permite crear plantillas dinámicas, contenido HTML, XML, CSS, etc. Todo esto mediante código de Python, como estructuras de control, bucles, clases o herencias entre plantillas.

## CREACIÓN DE PLANTILLAS:
Al utilizar plantillas (templates) con Flask, estas se deben estructurar dentro de la carpeta templates en la raíz del proyecto, debido a que Flask las tratará de recuperar de este directorio por defecto.

Por ejemplo, si se quisiera crear una plantilla HTML para la página *index*, se debería crear un archivo *index.html* dentro de la carpeta templates, este archivo podría contener un código que inicialmente defina el tipo de archivo mediante la etiqueta *!DOCTYPE* defina un título, y en su cuerpo podría incluir código Python, siempre entre las etiquetas **{% %}**. También podría aceptar variables que provengan del código *Flask*, siempre y cuando estén entre llaves dobles **{}**, como el siguiente ejemplo:

    <!DOCTYPE html>
    <html>
        <head>
            <title>Mi Sitio Web</title>
        </head>
        <body>
            <h1>Bienvenido a mi Sitio Web</h1>
            {%if name %}
            <p>Hola, {{name}}</p>
            {% else %}
            <p>Hola, desconocido</p>
            {% endif %}
        </body>
    </html>

En este caso, se ejecuta una estructura de control *{%if%}*, que a diferencia de un código Python, requiere de su finalización mediante el *{%endif%}*. También recupera la variable {{name}} que proviene del código Flask, que podría ser el siguiente:

    from flask import Flask, render_template

    @app.route('/index')
    def index():
        nombre = 'Jorge'
        return render_template('index.html', name = nombre)

Para renderizar el código Flask y que se muestre como una web, es necesario importar la función *render_template()*, y dentro de ella incluir el path de la plantilla, sin considerar la ubicación dentro de la carpeta *templates* puesto que Flask la busca automáticamente allí. También se le indica a la función que envíe una variable al template, en este caso la definimos previamente como nombre, pero será llamada name dentro de la plantilla.

### ESTRUCTURAS DE DATOS:
Además de variables, se permite enviar datos estructurados a las plantillas, como diccionarios. Por ejemplo, si se define un diccionario en una función y se envía a una plantilla:

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

Luego puede recuperarse dentro del template, mediante las sintaxis de {% %} y doble llave {{}}

    {% if my_data['name'] == None and my_data['age'] == None: %}
            <p>Hola mundo.</p>
    {% elif my_data['age'] == None: %}
            <p>Hola {{my_data['name']}}.</p> 
    {% else: %}
           <p>Hola {{my_data['name']}}, tienes {{my_data['age']}} años. Correo: {{my_data['email']}}</p> 
    {% endif %}

## HERENCIA DE PLANTILLAS:
Los templates permiten la posibilidad de heredar contenido entre sí. Generalmente se crea un archivo de plantilla *base.html* en el que se definen los elementos comunes a todas las plantillas, y se definen bloques con los contenidos que serán variables, mediante la sintaxis *{% block **nombre** %} {% endblock %}* especificando el nombre del bloque. Luego, en cada plantilla se incluye el contenido de la plantilla base mediante la sintaxis *{%extends 'base.html' %}*, y se define el contenido que se vaya a incluir en el bloque *{% block **nombre** %} **contenido** {% endblock %}*. Siguiendo el ejemplo anterior, la plantilla *base.html* podría ser:

    <!DOCTYPE html>
    <html>
        <head>
            <title>Mi Sitio Web - {% block title %} {% endblock %}</title>
        </head>

        <body>
            {%block content%}
            {%endblock%}
        </body>
    </html>

Mientras que la plantilla *index.html* sería:

    {%extends 'base.html' %}
    
    {%block title%} Página de inicio {%endblock%}
    
    {%block content %}
    <h1>Bienvenido a mi Sitio Web</h1>
        {%if name %}
        <p>Hola, {{name}}</p>
        {% else %}
        <p>Hola, desconocido</p>
        {% endif %}
        <h2>Lista de amigos:</h2>
        <ul>
            {% for friend in friends %}
            <li>{{friend}}</li>
            {% endfor %}
        </ul>
    {%endblock%}

## FILTROS:
Los filtros permiten procesar valores antes de que sean mostrados a través de la plantilla. Existen filtros predeterminados como *|upper* (mayúsculas), *|lower* (minúsculas) o *|reverse* (invertir listas), pero puede definirse también filtros personalizados. Por ejemplo, al código de bloques anterior, se le agregan dos filtros junto a la variable del nombre y de la lista, antecedidos por una barra vertical:

    {%block content %}
    <h1>Bienvenido a mi Sitio Web</h1>
        {%if name %}
        <p>Hola, {{name | upper }}</p>
        {% else %}
        <p>Hola, desconocido</p>
        {% endif %}
        <h2>Lista de amigos:</h2>
        <ul>
            {% for friend in friends | reverse %}
            <li>{{friend}}</li>
            {% endfor %}
        </ul>
    {%endblock%}


Para crear filtros personalizados se deben definir mediante el método *add_template_filter*. Supongamos el siguiente código, en el que, además del nombre y una lista, también se envía la fecha actual a la plantilla:

    from flask import Flask, render_template
    from datetime import datetime

    @app.route('/index/<name>')
    def index(name):
        friends = ['Alex', 'Pepe', 'Ana', 'José']
        date = datetime.now()
        return render_template('index.html', name = name, friends = friends, date = date)

Esa fecha se enviará en el formato *datetime* que incluye año, mes, día, hora, minutos y segundos con cienmilésimas. Podría crearse un filtro que de formato DD-MM-AAA a esa fecha. Esto puede lograrse de dos maneras. invocando el método *add_template_filter* mediante un decorador, e inmediatamente debajo definir el filtro como una función:

    @app.add_template_filter
    def ddmmaaaa(date):
        return date.strftime('%d-%m-%Y')

O podría también definir el filtro como función, y luego registrar el filtro, mediante la sintaxis del método *.add_template_filter()*, especificando entre paréntesis la función que contiene el filtro, y luego un nombre identificador:

    def ddmmaaaa(date):
        return date.strftime('%d-%m-%Y')
    
    app.add_template_filter(ddmmaaaa, 'formato_fecha')

La diferencia es que la segunda opción permite asignarle un alias al filtro para ser invocado en el template. Por ejemplo, en el primer caso, en el código del bloque de la plantilla, el filtro deberá ser invocado mediante el nombre de la función:
    
    <p>La fecha de hoy es: {{ date | ddmmaaaa }}</p>

Mientras que en el segundo caso, el nombre de la función produciría un error, ya que debe ser utilizado mediante el alias registrado:

    <p>La fecha de hoy es: {{ date | formato_fecha }}</p>

## FUNCIONES:
De la misma forma que se pueden enviar variables u otro tipo de datos, también es posible enviar funciones a un template, previamente definidas en el código principal. En el siguiente ejemplo se define la función *repetir_cadena* y se envía mediante *render_template* en el código que se utilizó en los ejemplos anteriores:

    def repetir_cadena(cadena, repetir):
        return cadena * repetir

    @app.route('/index/<name>')
    def index(name):
        friends = ['Alex', 'Pepe', 'Ana', 'José']
        date = datetime.now()
        return render_template('index.html', name = name, friends = friends, date = date, repetir_cadena = repetir_cadena)

Luego, será posible invocarla en el bloque de código del template:

    <p>Repetir nombre 3 veces: {{ repetir_cadena(name, 3) }}</p>

Sin embargo, existe una forma más sintética de enviar una función al template, mediante un decorador y el método *.add_template_global*, de la siguiente manera:

    @app.add_template_global
    def repetir_cadena(cadena, repetir):
        return cadena * repetir

Esta forma de definir una función global, permitirá que sea utilizada dentro de cualquier template que sea utilizado para este código, sin necesidad de enviarlo mediante *render_template*. Y finalmente, esta sintaxis también admite que se registre con un alias, mediante el método *.add_template_global*, de la siguiente manera:

    def repetir_cadena(cadena, repetir):
        return cadena * repetir

    app.add_template_global(repetir_cadena, 'repetidor')

En este último caso, se debe invocar la función mediante su alias registrado.

## ENLACES:
Entre varias páginas de una app web o un sitio, debe haber interacción y navegación. Estas referencias y enlaces se logran mediante la finción *url_for()*. Por ejemplo, retomando el ejemplo original:

    @app.route('/')
    @app.route('/index')
    def index():
        print(url_for('index'))
        print(url_for('data'))
        print(url_for('programa', codigo = ''))
        name = 'Pepe '
        friends = ['Alex', 'Pepe', 'Ana', 'José']
        date = datetime.now()
        return render_template('index.html', name = name, friends = friends, date = date, repetir_cadena = repetir_cadena)rint(url_for('programa', codigo = '<h1> code </h1>'))

En la función que define toda la página principal, se llama a la función *url_for()* y se especifica como destinos las funciones que contienen las otras páginas del sitio. Es decir, *url_for()* crea enlaces a otras funciones, no confundir especificando las direcciones de esas páginas o rutas. También existe la posibilidad de incluir los valores de las variables que recupera la función especificada en cada página, por ejemplo, se especificó un valor para *codigo* en el enlace de la función *programa*, que lleva hacia la ruta de la página */HTML/*. Se especifica una cadena vacía, porque la variable no puede ser enviada con valor *None*.

A continuación, esos enlaces definidos por la función *url_for()* deben ser creados en una plantilla. En este caso, el código se incluiría en la plantilla *base.html* para que luego se herede y replique en el resto de las páginas. El siguiente código estaría en el *<body>* de la template *base.html*

    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Inicio</a></li>
            <li><a href="{{ url_for('data') }}">Trabajando con datos</a></li>
            <li><a href="{{ url_for('programa', codigo = '<h1> código </h1>') }}">HTML</a></li>
        </ul>
    </nav>

Esto crearía una lista con los enlaces de las páginas principales, en cada una de las páginas que hereden de la plantilla *base.html*. En la creación del enlace a la función *programa* se debe especificar el valor de la variable *codigo*, puesto que en la definición del enlace, se especifica que tendrá un valor. Claramente, el enlace a la función *data* no especifica valores, por ende, el diccionario que se genera estará vacío, y la web actuará en consecuencia, mostrando 'Hola mundo.'

## ARCHIVOS ESTÁTICOS:
En una aplicación web probablemente sea necesario ingresar código CSS, JavaScrip, o de otros lenguajes, que serán necesariamente cargados como archivos estáticos. Por convención, todos los archivos estáticos se incluirán dentro de la carpeta *static*, y allí se ordenarán en subcarpetas como *css*, *js* o *img*. Una hoja de estilos *css* podría ser importada con la siguiente sintaxis: 

    <link rel="stylesheet" href="{{ url_for('static', filename = 'css/style.css') }}">

Por ejemplo, en el template *base.html* en la sección *<head>*, para que tenga efecto en las páginas que la heredan desde allí. De esta manera, el código de estilos se vuelve menos complejo, ya que la herencia puede manejarse por templates, según página, en vez de tener solo una hoja de estilos con distintas definiciones. 

