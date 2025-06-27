# BASES DE DATOS

En un sistema de programación modular, tal como se creó un fichero para todo lo relacionado con el GUI, se creará uno para albergar la base de datos en sí, por convención llamado *database*. También, en este paso se creará otro fichero donde se incluirá el código que incluya la interacción con las bases de datos, por buena práctica, puede ser llamado *model*. Dentro de esa carpeta se recomienda crear un módulo separado para cada interacción.

## CONEXIÓN:
Por convencción se codificará la conexión en un módulo, que en este caso llamaremos **connect_db.py**. Dentro de ese archivo importaremos la librería *sqlite3* que nos permitirá crear una clase que cree/conecte con nuestra base de datos, y que guarde cambios y desconecte. Esta clase se definirá como *ConexionDB* en el ejemplo, con un método constructor que defina una variable *self.base_datos* con el path del archivo de base de datos. Luego se define otro atributo que llame al método *sqlite3.connect()* especificando el path. Si el archivo existe se conectará, si no, lo creará y conectará. Finalmente, el constructor define un nuevo atributo sobre el de la conexión, mediante el método *.cursor()*. Este cursor será el encargado de introducir los cambios que realice el usuario a la base de datos.

Dentro de la clase, se debe definir un método extra, en este caso *cerrar(self)* para guardar cambios, mediante el método *.commit()* y terminar la conexión, con el método *close()*. Ambos métodos aplicados sobre el atributo *self.conexion*.

    import sqlite3

    class ConexionDB:
        def __init__(self):
            self.base_datos = 'database/peliculas.db'
            self.conexion = sqlite3.connect(self.base_datos)
            self.cursor = self.conexion.cursor()

        def cerrar(self):
            self.conexion.commit()
            self.conexion.close()

## CREAR Y BORRAR TABLAS:
Es conveniente crear un nuevo módulo para definir estas tareas, convencionalmente en su nombre se debe incluir la sigla *dao* (Data Access Object). En el siguiente ejemplo se importará del módulo *.connect_db* la clase *ConexionDB* y se definirá una función *creaar_tabla()* que comenzará creando un objeto *conexion* de esa clase. Luego se define el código sql como un string en una variable, creando una tabla, definiendo sus columnas y tipos de dato, y la clave principal. Para ejecutar este código se llamará al módulo *execute()* del atributo *.cursor()* del objeto que contiene la conexión. Y finalmente se ejecutará el método *.cerrar()* definido en la clase ConexionDB().

Además, puede crearse la función *borrar_tabla()* que cree el objeto de la clase *ConexionDB* y ejecute el código sql para borrar una tabla, de la misma forma, mediante el módulo *execute()* del atributo *.cursor()* y luego el método *.cerrar()*.

    from .connect_db import ConexionDB

    def crear_tabla():
        conexion = ConexionDB()

        sql = '''
        CREATE TABLE peliculas(
            id_pelicula INTEGER,
            nombre VARCHAR(100),
            duracion VARCHAR(10),
            genero VARCHAR(100),
            PRIMARY KEY(id_pelicula AUTOINCREMENT)
        )'''

        conexion.cursor.execute(sql)
        conexion.cerrar()

    def borrar_tabla():
        conexion = ConexionDB()

        sql = '''DROP TABLE peliculas'''

        conexion.cursor.execute(sql)
        conexion.cerrar()

## CREAR REGISTROS:
Para ingresar datos en la tabla de la base de datos se utilizará el código sql correspondiente **INSERT INTO** teniendo en cuenta que el string que contenga el código deberá ser formateado para poder incluir las variables de las que se obtenga la información, en este caso particular, recuperadas de los campos del widget. Para luego ejecutar el código sql y realizar el correspondiente control de errores:

    def guardar(nombre, duracion, genero):
        conexion = ConexionDB()
        sql = f""" INSERT INTO 
                peliculas (nombre, duracion, genero)
                values('{nombre}', '{duracion}','{genero}' )
                """
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            mensaje(['i', 'Agregar película', 'Película agregada con éxito.'])        
        except:
            mensaje(['e', 'Agregar película', 'Base de Datos inexistente.'])

Para insertar efectivamente el registro en la base de datos, se le debe asignar la función al boton correspondiente. El mismo está definido de esta manera:

    self.boton_guardar = tk.Button(self, text='Guardar', bg='#1658A2', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#3586DF', command=self.guardar_datos)

Siendo que su parámetro *command* ejecuta la función *self.guardar_datos()*, se llamará a la función *guardar()* importada del módulo *model.pelicula_dao* con los parámetros obtenidos desde los *tk.StringVAR()* definidos en los campos del widget, mediante el método *.get()*

    def guardar_datos(self):
        guardar(self.input_nombre.get(), self.input_duracion.get(), self.input_genero.get())
        self.deshabilitar_campos()

De esta manera, la función *guardar()* ejecutará el código sql con los datos rcuperados de los campos del widget. Finalmente se deshabilitarán los campos mediante otra función definida anteriormente.

##LISTAR REGISTROS:
El código para obtener los registros será similar, pero utilizando la instrucción sql *SELECT * FROM', y luego el cursor deberá utilizarse con el método *.fetchall()* que obtiene todos los registros de la tabla, siendo almacenados en formato de lista:

    def listar():
        conexion = ConexionDB()

        lista_peliculas = []
        sql = 'SELECT * FROM peliculas'

        try:
            conexion.cursor.execute(sql)
            lista_peliculas = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            mensaje(['e', 'Conexión a Base de Datos', 'Base de Datos inexistente.'])

        return lista_peliculas

la función creada deberá ser importada en el archivo del widget y agregada al contenido de la tabla principal. Se debe tener en cuenta que la lista obtenida estará invertida, por lo que se aplica el método *.reverse()* para ordenarla según el primer elemento *ID*. Luego se realiza una iteración de esa lista y los valores se incluyen en la tabla mediante el método *.insert()*, teniendo en cuenta en este caso que el primer parámetro es una cadena vacía ya que no existe un elemento padre, el segundo parámetro es la posición 0 puesto que se listará al principio de la tabla, el nro de ID se encuentra en la posición [0] de cada elemento, y luego se asignan los *values* correspondientes a cada posición:

    self.lista_peliculas = listar()
    self.lista_peliculas.reverse()
    for pelicula in self.lista_peliculas:
        self.tabla.insert('',0,text=pelicula[0], values = (pelicula[1], pelicula[2], pelicula[3]))

## EDITAR REGISTROS:
Similarmente a los métodos anteriores, se debe definir un código sql con las instrucciones *UPDATE*, *SET* y *WHERE*

    def editar(id, nombre, duracion, genero):
        conexion = ConexionDB()
        sql = f"""UPDATE peliculas
                SET NOMBRE = '{nombre}', duracion = '{duracion}', genero = '{genero}'
                WHERE id_pelicula = '{id}'
                """
        
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except:
            mensaje(['e', 'Editar película', 'Base de Datos inexistente.'])

Particularmente en este ejemplo se vincula el botón a un método de la clase contenedor en el archivo *gui* que obtiene datos del elemento seleccionado de la tabla, mediante el método *.selection()* y los almacena en diferentes atributos internos. Luego se habilitan los campos y se ingresan esos datos en ellos para que el usuario pueda modifcarlos. 

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.durac_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.campo_nombre.insert(0, self.nombre_pelicula)
            self.campo_duracion.insert(0, self.durac_pelicula)           
            self.campo_genero.insert(0, self.genero_pelicula)            
        except:
            tk.messagebox.showerror('Editar película', 'Seleccione un registro.')

Entre los atributos definidos está *self.id_pelicula* conteniendo el número de identificación del registro modificado. Puesto que la carga en la base de datos se realizará con el botón *GUARDAR*, se debe modificar el comportamiento del mismo:

    def guardar_datos(self):

        if self.id_pelicula == None:
            guardar(self.input_nombre.get(), self.input_duracion.get(), self.input_genero.get())
        else:
            editar(self.id_pelicula, self.input_nombre.get(), self.input_duracion.get(), self.input_genero.get())

        self.deshabilitar_campos()
        self.tabla_peliculas()

En este código se añade una condición para evaluar si el atributo *self.id_pelicula* está vacío (tal como se define al inicio del metodo constructor del contenedor), en tal caso el botón ejecuta la función guardar, para agregar un nuevo registro a la base de datos. En caso de que *self.id_pelicula* contienga un dato, es decir, que provenga desde el método *editar_datos()*, se procede con la función *editar()* que modifica el registro existente en la base de datos, vinculado a ese nro de ID.

## ELIMINAR REGISTROS:
Similarmente a los métodos anteriores, se debe definir un código sql con las instrucciones *DELETE FROM* y *WHERE*

    def eliminar(id):
        conexion = ConexionDB()
        sql = f'''DELETE FROM peliculas
                WHERE id_pelicula = {id}
                '''

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except:
            mensaje(['e', 'Editar película', 'Base de Datos inexistente.'])

Adicionalmente, se podrá crear un método del *Contenedor* que obtenga el id y el nombre de la película seleccionada y mediante un *messagebox.askokcancel* solicite una confirmación:

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            
            confirma = mensaje(['a','Eliminar película', f'Se eliminará {self.nombre_pelicula}.'])

            if confirma:
                eliminar(self.id_pelicula)
                self.tabla_peliculas()
            else:
                mensaje(['i','Eliminar película', 'Operacion cancelada.'])
                self.id_pelicula = None
        except:
            mensaje(['e','Eliminar película', 'Seleccione un registro.'])

## EJECUCIÓN:
Para que todos estos cambios tengan efecto, se deberán incluir en la funcionalidad de los botones y menúes del archivo con la interfaz de usuario (GUI), como se especificó en la descripción de la librería **tkinter**. Para ello, se deben importar las funciones y módulos, y asignarlos a los parámetros *command* de los elementos del menú. 