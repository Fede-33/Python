# ERRORES

## TIPOS:

* **INTERPRETACIÓN:** Errores de sintaxis, asignaciones incorrectas, o faltas a las buenas prácticas y convenciones. Suelen ser detectados por los editores de código.
* **TIEMPO DE EJECUCIÓN:** Errores que no son detectados por el editor de código, pero que generan *EXCEPCIONES* durante su ejecución.

## EXCEPCIONES:
Indica un problema en tiempo de ejecución. La consola detendrá el programa y retornará un mensaje que identifica el error y la línea de código en la que se produjo.

### GESTIÓN DE EXCEPCIONES:
Para manejar las posibles excepciones se utilizan los bloques de "try-except-else". Este bloque intentará realizar ciertas acciones, en caso de que surja una excepción ejecutará otra línea de código, y finalmente, de forma opcional, puede ejecutar otra linea final en caso de que no se produzcan excepciones. Por ejemplo:

    while True:
        try:
            n = int(input('Ingrese 1 para continuar o 2 para salir: '))
            if n != 1 and n != 2:
                raise ValueError
            elif n == 2:
                print('Adios')
                break
        except ValueError:
            print ('Ingreso incorrecto')
        else:
            print('Continuar')

Se intenta ingresar un número entero para continuar y otro para salir. En caso de que el ingreso no sea ninguno de esos números, se disparará una excepción (ValueError). Al dispararse la excepción, se ejecuta el código de *except*. En caso de que no haya excepción, pero se ingrese 2, el código se detiene. Si se ingresa 1, el código continua sin problemas.

#### CAPTURAR EXCEPCIONES:
Es posible almacenar el mensaje de la excepción surgida en una variable, para luego mostrarla por pantalla, y que no sea necesario detener la ejecución para saber lo que ocurrió. Por ejemplo:

    while True:
        try:
            n = int(input('Ingrese 1 para continuar o 2 para salir: '))
            if n != 1 and n != 2:
                raise Exception ('Opción incorrecta')
            if n == 2:
                print('Adios')
                break
        except Exception as error:
            print ('Ocurrió un error: ', error)
        else:
            print('Continuar') 

En el ejemplo anterior tenemos dos tipos de excepciones posibles. Que el usuario ingrese un número enterio distinto de 1 o 2, lo cual lanzará una excepción personalizada con el mensaje *Opción incorrecta*. O que el usuario ingrese un valor distinto a un número entero, que producirá una excepción de *ValueError* con el mensaje *invalid literal for int() with base 10:*. Cualquiera de las dos excepciones, se almacenará en la variable *error*. Cuando se produzca cualquiera de las dos, se ejecutará el código que indica el tipo de error imprimiando su mensaje por pantalla.

    while True:
        try:
            n = int(input('Ingrese 1 para continuar o 2 para salir: '))
            if n != 1 and n != 2:
                raise Exception ('Opción incorrecta')
            if n == 2:
                print('Adios')
                break
        except Exception as error:
            print ('Ocurrió un error: ', type(error).__name__)
        else:
            print('Continuar')

Esta variación del código extrae el nombre del tipo de error. Las excepciones son clases, siendo *Exception* la clase padre de todas las demás. el método *.__name__* retorna el nombre de la subclase de excepción que se produzca. Por ejemplo, si el usuario ingresa una letra, el retorno no será *invalid literal for int() with base 10:* (mensaje de la excepción), sino que será *ValueError* (nombre de la excepción).

#### EXCEPCIONES MÚLTIPLES:
Si es posible que se produzca más de una excepción, deberían intentarse subsanar todas, mediante una repetición de *except*:

    while True:
        try:
            n = int(input('Ingrese 1 para realizar una división o 2 para salir: '))
            if n != 1 and n != 2:
                raise Exception ('Opción incorrecta')
            if n == 2:
                print('Adios')
                break
            a = int(input('Ingrese dividendo: '))
            b = int(input('Ingrese divisor: '))
            print(f'\nLa división entre {a}/{b} es: {a/b}')
        except ValueError:
            print('Ingrese un número entero')
        except ZeroDivisionError:
            print('No se puede dividir por 0')        
        except Exception as error:
            print ('Ocurrió un error: ', error)

En el ejemplo se trata de gestionar el error de ingreso de un valor no numérico, luego del error matemático de la división por 0, y finalmente de la excepción lanzada como *Opción incorrecta*.

#### CREAR EXCEPCIONES:
Tal como se ha dicho, las excepciones son clases hijas de la clase *Exception*. Es posible entonces definir excepciones personalizadas por el usuario mediante la sintaxis de clases:

    class OperadorExcepcion(Exception):
        def __init__(self, mensaje):
            super().__init__(mensaje)
    
    def dividir(a, b):
        if b == 0:
            raise OperadorExcepcion('Error: No se puede dividir por 0')
        else:
            return a / b
    
    dividir(4,0)

En este caso, se crea la excepción y se lanza al llamar a la función. No se está atrapando ni gestionando la excepción. El programa finalizará con la excepción definida por el usuario.

# ARCHIVOS

El manejo de archivos o ficheros es un principio de la *persistencia de datos*, es decir, que cuando es necesario reutilizar los datos, como en una base de datos, se deberán almacenar en otros archivos, no tan solo en variables locales de programa.

## GESTIÓN DE ARCHIVOS:
Para trabajar con archivos se importará la función *open* de la librería *io*. Siempre es conveniente invocar la función *open()* dentro de un módulo personalizado con otras funciones específicas de acuerdo al modo de apertura deseado, entre los que encontramos:

### **'w'** CREACIÓN Y ESCRITURA.

    from io import open

    def escribir_archivo(nombre, texto):
        archivo = open(nombre, 'w')
        archivo.write(texto)
        archivo.close()
        return 'Archivo creado.\n'

Esta función creará un archivo nuevo y escribirá dentro del mismo. Si lo que se busca es borrar el contenido completo de un archivo, se invoca esta función con texto vacío, y eso reescribirá el contenido, en este caso, eliminándolo aparentemente.

### **'r'** SOLO LECTURA.

    from io import open

    def leer_archivo(nombre):
        archivo = open(nombre, 'r')
            texto = archivo.read()
        archivo.close()
        return f'\n{nombre}:\n{texto}\n'
        
### **'r+'** LECTURA Y ESCRITURA.

    from io import open

    def modificar_archivo(nombre):
        archivo = open(nombre, 'r+')
        print(f'\n{nombre}:\n{archivo.read()}\n')
        texto = input('Ingrese nuevo texto: ')
        archivo.seek(0)
        archivo.write(texto)
        archivo.close()
        return'Archivo modificado.\n'

La modificación de texto puede personalizarse tanto si se trabaja el contenido del archivo como un string o como listas mediante el método *readlines()* y *writelines()*. Para esto se utiliza el método *seek()* que permite indicar la posición del cursor donde es necesario leer o escribir. En este ejemplo, el cursos se posiciona en 0, es decir, al comienzo del string que recupera el archivo. 

### **'a'** CREACIÓN O ACTUALIZACIÓN.

    from io import open

    def actualizar_archivo(nombre, texto):
        archivo = open(nombre, 'a')
        archivo.write(texto)
        archivo.close()
        return'Archivo actualizado.\n'

### COMPROBAR ARCHIVO:
Para comprobar la existencia de un archivo se utiliza el módulo *path* de la librería *os* que permite interactuar con el sistema:

    from os import path
    
    def existe_archivo(nombre):
        if path.isfile(nombre):
            return True
        else:
            return False

Esta función práctica puede definirse para invocarla antes de realizar cualquier otro trabajo con archivos. Se comprueba la existencia del mismo, en base a eso, se procede a su escritura, reescritura, letcura, etc. Evita tener que gestionar excepciones del tipo *FileNotFoundError*. 