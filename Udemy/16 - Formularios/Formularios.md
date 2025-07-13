# FORMULARIOS
Son conjuntos de campos y botones, que permiten recibir y enviar información al usuario. En aplicaciones web pueden crearse mediante *HTML* y *CSS*, adicionalmente en Flask pueden realizarse con bibliotecas particulares, que incluyen características como la validación de datos y ciertas medidas de seguridad. Entre los usos que se les puede dar, incluyen, inicio de sesión, registro de usuario, búsqueda de datos, etc.

## CREACIÓN:
Un formulario se define en código *HTML*, mediante la etiqueta *form*, y al estar trabajando con *Flask*, especificando el método *post* que permite que los datos sean capturados por la plantilla y enviados al programa. Cada campo se define mediante la etiquera *label* especificando un parámetro *for* con el nombre de la variable local que recibirá el contenido del campo, y un texto que le antecede entre las etiquetas. Debe declararse un *input* definiendo su *type* y *name* que será el argumento que capture el dato ingresado y sea enviado al código *flask* de la app. 

En el siguiente ejemplo se define un formulario de registro de usuario, dentro de un archivo *register.html*, que envía las variables *username* y *password*. Este último se define como *type='password'* que muestra puntos en vez de los caracteres ingresados. Al final se define un botón con la etiqueta *input* y el tipo *submit*. El método *post* permite enviar los datos de los campos hacia la app *flask* sin que se muestren en los argumentos de la barra de direcciones, lo que visualizaría el nombre de usuario y la contraseña en el URL. 

    <form action="" method="post">
        <label for="username">Nombre de usuario</label>
        <input type="text" name="username" id="username">
        <br>
        <br>
        <label for="password">Contraseña</label>
        <input type="password" name="password" id="password">
        <br>
        <br>
        <input type="submit" value="Registrar">
    </form>

Nuevamente en el código de la app de *flask*, se debe crear el la ruta al archivo *HTML*, especificando los métodos de entrada, mediante el argumento *methods*. Por defecto, considera que se utiliza el método *GET*, pero al requerir el método *POST*, deben ser ambos especificados. Para definir el template, debe ser realizado dentro de una función, que retorne el *render_template* con el path del archivo *HTML*, y en la que también se definiran las variables que capturarán los datos que se reciben desde el formulario, mediante el método *.request.form()*, que debe ser importado desde la biblioteca de *Flask*. 

En el siguiente ejemplo sobre el formulario de registro de usuario, se importa el método *request*, se define la ruta y los métodos de entrada necesarios. Se define la función *register()* que comienza con una condición sobre el método de entrada, en caso de ser *GET*, es decir, provenir de la ejecución por defecto del código, retorna el template. En caso de ser *POST*, es decir, provenir desde el botón *submit* del formulario, captura los datos recibidos en las vriables *usuario* y *contras*, mediante el método *request.form()* especificando entre préntesis los nombres de las variables que se definieron en el *input* de la plantilla *HTML.  

    from flask import Flask, render_template, url_for, request

    @app.route('/auth/register', methods = ['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('auth/register.html')
        elif request.method == 'POST':
            usuario = request.form['username']
            contras = request.form['password']
            return f'Nombre de usuario: {usuario} Contraseña: {contras}'

## VALIDACIÓN:
La validación de datos debe realizarse dentro del código *flask* de la app, una vez obtenidos los datos desde el template html, se introducen los requisitos, usualmente mediante una sentencia *if*, en caso de que se cumplan, se continúa con el programa. En caso de que no se cumplan los requisitos, se retornará el *render_template()* de la plantilla, con el parámetro *error* asignándole un mensaje para el usuario.

En el ejemplo siguiente, se toma el código anterior de registro de usuario, y se incluye la condición de que el *username* y el *password* tengan entre 6 y 25 caracteres, en caso de no cumplirse, se asigna ese mensaje al parámetro *error*.


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

Luego en el template del que provienen los datos, se debe agregar una sentencia que verifique el parámetro *error* y en caso de estar definido, lo muestre al usuario.

En el siguiente ejemplo, se agrega un condicional *{%if%}* mediante la sintaxis correspondiente al template, que verifica si el parámetro *error* contiene información, en tal caso, muestra un párrafo debajo del formulario en color rojo llamativo, con el contenido del error que se definió en el código de la app.

    {%if error%}
        <p style="color: red;">{{error}}</p>
    {%endif%}

## WTFORMS
Es una biblioteca interna de *Flask* especialmente diseñada para el manejo de formularios. Para su instalación dentro del entorno virtual, en línea de comandos se debe ejecutar **pip install flask-wtf**.

Para realizar el mismo formulario del ejemplo anterior con *WTForms*, en primera instancia se debe importar las dependencias instaladas. En este caso se utilizará la clase *FlaskForm* de la librería *flask_wtf*, las clases *StringField()*, *PaswordField()* y *SubmitField()* del módulo *wtforms.fields* y las clases *DataRequired* y *Length* del módulo *wtforms.validators*:

    from flask_wtf import FlaskForm
    from wtforms.fields import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired, Length

Posteriormente se debe crear una subclase de la clase *FlaskForm* en este caso llamada *FormularioETForm*, en la que se definen tres atributos *username*, *password* y *button*. El atributo *username* es de la clase *StringField*, que construye campos de entrada de texto, pudiendo especificar su etiqueta, e incluir los validadores importados, en este caso, *DataRequired()* que obliga a que el campo tega datos, y *Lenght()* que especifica una cantidad mínima y máxima de caracteres. El atributo *password* es de la clase *PasswordField*, similar a *Stringfield* pero cubriendo el ingreso del usuario con puntos. El atributo *button*, de la clase *SubmitField* construye un botón con el texto indicado:

    class FormularioWTForm(FlaskForm):
        username = StringField('Nombre de usuario: ', validators= [DataRequired(), Length(min=6, max=25)])
        password = PasswordField('Contraseña:', validators= [DataRequired(), Length(min=6, max=25)])
        button = SubmitField('Enviar')

Una vez creada la clase que da forma al formulario, se procede a definir la ruta los métodos de entrada, a definir una función llamada *registrar()* y dentro de ella instanciar un objeto *formulario* de la clase *FormularioWTForm()*. Cómo condición se verifica el método *objeto.validate_on_submit()* que retorna *True* si los validadores definidos en la clase *FormularioWTForm* fueron correctos en este caso, sobre el objeto *formulario*. En tal caso, recupera los datos enviados desde los campos mediante el método *objeto.atributo.data*, en este caso *formulario.username.data*, y la función retorna el mensaje en el navegador. En caso de que los validadores sean rechazados, renderizará la planilla enviando como parámetro el objeto formulario, con el nombre *form*: 

    @app.route('/auth/register_wtform', methods = ['GET', 'POST'])
    def registrar():
        formulario = FormularioWTForm()
        if formulario.validate_on_submit():
            usuario = formulario.username.data
            contras = formulario.password.data
            return f'Nombre de usuario: {usuario} Contraseña: {contras}'
        elif request.method == 'GET':
            return render_template('auth/register_wtform.html', formu=formulario)   

En el template *HTML* se define el formulario y el método de salida, mediante el parámetro *formu* que incluye el objeto creado en el código de *flask* y se le aplican una serie de métodos. En primer lugar *.hidden_tag()* que genera un token CSRF (Cross-Site Request Forgery token) único para esa sesión, para verificar que la solicitud proviene de tu propio sitio web y no de un ataque malicioso. El método *.label* aplicado a cada atributo de campo, y a continuación el atributo en sí, para mostrar la etiqueta y el espacio a completar. Y finalmente se llama al atributo *button*. Esto presentará el código en el sitio web:

    <form action="" method="post">
        {{formu.hidden_tag()}}
        {{formu.username.label}} {{form.username}}
        {{formu.password.label}} {{form.password}}
        {{formu.button}}
    </form>