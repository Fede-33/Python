# INTRODUCCIÓN
Flask es un microframework de Python para desarrollo de aplicaciones web. Proporciona un enrutador URL y herramientas básicas para manejar solicitudes y respuestas HTTP. Admite todo tipo de tecnología y librerías de la arquitectura de Python, dándole flexibilidad al desarrollador para elegir las que más se adecúen a su proyecto, pudiendo ser aplicaciones pequeñas de un solo Script de código, como directorios de numerosos módulos, o incluso aplicaciones simples pero escalables con sucesivas actualizaciones. Flask se caracteriza por:

* Fácil de usar.
* Flexibilidad.
* Pequeño y ligero.
* Comunidad activa.
* Bajo nivel de abstracción.
* Compatibilidad con otros servicios.

## INSTALACIÓN:
Primeramente se debe tener instalada una versión de Python superior a 3.7 en el sistema. Se recomienda instalarlo en un entorno virtual para cada proyecto que se realice, para que no se afecte la compatibilidad con otros proyectos que utilicen otros frameworks.

Una vez dentro del entorno virtual configurado para el proyecto, el comando de instalación de Flask es:

    pip install flask

## APLICACIÓN:
Para crear una app simple es necesario importar Flask en el script .py y luego definir una instancia de la clase *Flask*, en el siguiente ejemplo con la variable *__name__* que siempre contiene el nombre del módulo actual. Esto le indica a Flask dónde debería buscar archivos de recursos en caso de ser necesarios. El objeto *app* es la instancia de la clase *Flask* que ahora representa a la aplicación.
A continuación se agrega un decorador, que modifica el comportamiento de la función que se define luego. En este caso *@app.route('/')* indica que la función *hello()* se ejecutará automáticamente cuando se navegue por el path indicado, que siendo *'/'* se refiere a la raíz de la app web. Finalmente se define la función:

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hola mundo'

Para iniciar una app de Flask por terminal se debe ejecutar el comando **flask --app *path* run** donde el path es la ruta de acceso al archivo que contiene el módulo principal, en este caso, en el que se instanció la clase Flask con el parámetro *__name__*:

    flask --app holamundo_flask run

Flask tiene una función debug, que permite el monitoreo en tiempo real de nuestro servidor, sin necesidad de ejecutar el comando de inicio constantemente. Para eso se debe ejecutar el comando **flask --app *path* --debug run**. Esto iniciará el modo debug en la consola, y cada vez que se guarden cambios en los archivos de la app, se mostrarán en la misma. Para visualizarlos en el servidor, será necesario actualizar el navegador.

Una características útil del modom debug es que, en caso de haber errores de sintaxis o de lógica en nuestro código, se mostrará su descripción tanto en la terminal, como en la ventana en que se está ejecutando la app web.

## RUTAS Y VISTAS:
El método *.route()* permite definir la ruta en que se ejecutará una función, dentro de nuestra app web. Para su utilización se deben tener ciertas consideraciones como que:
* Si se define la misma ruta dos veces, el servidor considerará la que se definió primero.
* Definir dos veces la misma función provocará un error.
* Pueden definirse dos rutas para la misma función.
* Dentro de las funciones puede incluirse código HTML o un path a otro Script.

El código de ejemplo podría modificarse de la siguiente manera:

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

Siendo la dirección del servidor local **http://127.0.0.1:5000**, entonces:

* **Página principal** se verá en las direcciones *http://127.0.0.1:5000/* y *http://127.0.0.1:5000/index* en formáto de título.
* **Hola Mundo** se verá en la dirección *http://127.0.0.1:5000/hello_world* en formato de subtítulo.
* **Tel. nro. 6546546546** se verá en la dirección *http://127.0.0.1:5000/contacto* en formato subtítulo menor.

## VARIABLES:
Pueden definirse variables para obtenerlas por URL y luego recuperarlas en la función. Los datos ingresados serán almacenados como cadenas de texto, a menos que se especifique otro tipo de dato:

    @app.route('/datos/<nombre>/<int:edad>')
    def data(nombre = None, edad = None):
        if nombre == None and edad == None:
            return 'Hola mundo.'
        elif edad == None:
            return f'Hola {nombre}.'
        else:
            return f'Hola {nombre}, tienes {edad} años.'

## ESCAPE HTML:
Si en la variable que se ingresa por URL se escribiera código HTML, este sería ejecutado en la ventana principal. Esto sucede porque Flask retorna siempre una plantilla HTML, por defecto. Sin embargo, podría ser necesario que el código se muestre como texto simple, y no se ejecute. Para ello se debe importar la función *escape()* de la librería *markupsafe* que se incluye en la instalación de *Flask*. Al momento de incluir la variable en la ruta, se debe especificar que se trata de código, indicando que el tipo de dato es *path:* y luego, al ser retornado por la función, ese string que contiene código debe ser llamado a través de la función importada *escape()*:

    from markupsafe import escape
    
    @app.route('/HTML/<path:codigo>')
    def programa(codigo):
        return f'Código: {escape(codigo)}'

Esta función es fundamental cuando se permite entrada de datos por URL, puesto que si un usuario intenta ingresar código HTML, este se ejecutaría en ventana directamente, pudiendo así vulnerar la app.