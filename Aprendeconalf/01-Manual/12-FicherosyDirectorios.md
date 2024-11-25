# FICHEROS

Al utilizar ficheros para guardar los datos estos perdurarán tras la ejecución del programa, pudiendo ser consultados o utilizados más tarde. Las operaciones más frecuentes son:

## CREACIÓN Y ESCRITURA:

Se utiliza la siguiente función:

> **var** = open (**path**, 'w')

Que crea el fichero en la ruta especificada en *path* y, mediante el argumento *'w'* lo abre en modo escritura. esta función devuelve un objeto *var* que referencia al fichero. Se debe tener en cuenta que, si el fichero ya existe, será reescrito.

Una vez creado el fichero, ya puede escribirse en el mediante la sintaxis:

> **var**.write(**'texto'**)

Escribe el *'texto'* en el fichero referenciado como *var*. Este método devolverá, por consola, la cantidad de caracteres escritos.

### EJEMPLO:

    >>> f = open('saludo.txt', 'w')
    >>> f.write('¡Bienvenido a Python!')
    21

## AÑADIR DATOS:

Si se necesita añadir datos a un fichero existente, sin sobreescribirlo:

> **var** = open (**path**, 'a')

Abre el fichero existente en el *path* mediante el argumento *'a'*, en modo *append*, asignándolo al objeto *var*. Todo lo que se añada con el método *.write* se agregará al final del fichero.

### EJEMPLO:

    >>> f = open('saludo.txt', 'a')
    >>> f.write('\n¡Hasta pronto!')
    15

## LEER DATOS:

Abrir un fichero en modo solo letura con la función:

> **var** = open (**path**, 'r')

Abre el fichero existente en el *path* mediante el argumento *'r'*, en modo *read*, asignándolo al objeto *var*. Esto permite leer el fichero completo mediante la función:

> var.read()

Que devuelve toda la información de *var* como una cadena de caracteres. O puede ejecutarse la función:

> var.readlines()

Que retorna una lista de cadenas, donde cada cadena es una línea del fichero *var*.

### EJEMPLO:

    >>> f = open('saludo.txt', 'r')
    >>> print(f.read())
    ¡Bienvenido a Python!
    ¡Hasta pronto!

    >>> f = open('saludo.txt', 'r')
    >>> lineas = f.readlines()
    >>> print(lineas)
    ['Bienvenido a Python!\n', '¡Hasta pronto!']

## LECTURA DE INTERNET

Para obtener los datos de un fichero on line se debe importar la librería *urllib*, específicamente el módulo *request*, que contiene la función *urlopen()* mediante la sintaxis:

> from urllib import request
> **var** = request.urlopen(**path**)

Esto asignará a un objeto *var* el contenido de la web que contenga el *path*, y se podrá acceder mediante los métodos descriptos anteriormente

### EJEMPLO:

    >>> from urllib import request
    >>> f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
    >>> datos = f.read()
    >>> print(datos.decode('utf-8'))
    Aprende con Alf
    ===============

## CERRAR:

Es conveniente cerrar los ficheros al finalizar de trabajar con ellos, debido a que no podrán ser accedidos por otra aplicación mientras estén abiertos por el programa. Además de que puede ocupar excesivo espacio de memoria y se corre el riesgo de producir cambios accidentales con código ulterior. Para cerrar un fichero se utiliza la finción:

> **var**.close()

### EJEMPLO:

    >>> f = open('saludo.txt'):
    >>> print(f.read())
    ¡Bienvenido a Python!
    ¡Hasta pronto!
    
    >>> f.close()  # Cierre del fichero
    
    >>> print(f.read())  # Produce un error
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file.

## APERTURA Y CIERRE:

La siguiente estructura permite abrir un fichero, ejecutar un código, y que se cierre automáticamente al finalizar la ejecución:

>with open (**path**, **modo**) as **var**:
>> **código**

Se abre el fichero contenido en el *path*, espedificando el *modo* ('w', 'a', 'r'), y se lo asigna al objeto *var*. Se ejecuta el *código* especificado, y al finalizar se cierra automáticamente el fichero.

### EJEMPLO:

    >>> with open('saludo.txt', 'w') as f:
    ...     f.write("Hola de nuevo")
     
    13
    >>> with open('saludo.txt', 'r') as f:
    ...     print(f.read())
     
    Hola de nuevo
    >>> print(f.read())  # Produce un error al estar el fichero cerrado
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file.

## RENOMBRADO O BORRADO:

Para esto se debe importar la librería *os* con todas sus funciones, mediante la sintaxis:

> import os

Para renombrar un fichero se utilizará la función:

> os.rename(**path**, **path2**)

Que tiene la facultad de mover y renombrar el fichero desde el *path* hacia el *path2*. Si lo que se necesita es eliminar el fichero, se recurre a la función:

> os.remove(**path**)

Previo al borrado o eliminado, es conveniente comprobar si el fichero existe, para evitar un error. Se logra mediante la función:

> os.path.isfile(**path**)

Que retorna *True* si existe un fichero en el *path* especificado, o *False* en caso contrario.

### EJEMPLO:

    >>> import os
    
    >>> f = 'saludo.txt'
    
    >>> if os.path.isfile(f):
    ...     os.rename(f, 'bienvenida.txt') # renombrado
    ... else:
    ...     print('¡El fichero', f, 'no existe!')
    
    >>> f = 'bienvenida.txt'
    >>> if os.path.isfile(f):
    ...     os.remove(f) # borrado
    ... else:
    ...     print('¡El fichero', f, 'no existe!')
    
# DIRECTORIOS

Para trabajar con directorios se utiliza la librería *os*, las siguientes son algunas de sus funciones:

|SINTAXIS| FUNCIÓN|
|-|-|
|os.listdir(**path**)| Retorna una lista con los ficheros y directorios que contiene la ruta *path*.|
|os.mkdir(**path**)| Crea un nuevo directorio en la ruta *path*.|
|os.chdir(**path**)| Cambia el directorio actual y se posiciona en el de la ruta *path*.|
|os.getcwd()| Retorna una cadena con la ruta del directorio actual.|
|os.rmdir(**path**)| Elimina el directorio de la ruta *path*, siempre que esté vacío.|
|os.rename(**path**, **path2**)| Funciona de la misma forma con directorios que con ficheros.|

Para realizar operaciones de alto nivel será necesaria la librería *shutil* que importaremos mediante la sintaxis:

> import shutil

Y las siguientes son algunas de sus principales funciones:

|SINTAXIS| FUNCIÓN|
|-|-|
|shutil.rmtree(**path**)| Elimina el directorio especificado en la ruta *path* y todo lo que contiene.|
|shutil.copy(**path**, **path2**)| Copia el archivo *path* a la ubicación *path2*. No conserva los metadatos.
|shutil.copy2(**path**, **pat2**)| Similar a copy(), pero conserva los metadatos como los tiempos de acceso y modificación.
|shutil.copytree(**path**, **pat2**)| Copia un directorio  todo su contenido a una nueva ubicación.
|shutil.move(**path**, **path2**)| Mueve un archivo o directori de *path* a *path2*. Si *path* es un directorio existente, el archivo se moverá dento de ese directorio.
|shutil.make_archive(**nombre**, **formato**, **path**)| Crea un archivo llamado *nombre* comprimido en el *formato* especificado (ZIP, TAR, RAR, etc) a partir de un directorio *path*.
|shutil.unpack_archive(**nombre**, **path**)| Extrae los contenidos de un archivo comprimido llamado *nombre* a un directorio especificado en el *path*.
