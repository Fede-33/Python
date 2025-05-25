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

# ARCHIVOS

El manejo de archivos o ficheros es un principio de la *persistencia de datos*, es decir, que cuando es necesario reutilizar los datos, como en una base de datos, se deberán almacenar en otros archivos, no tan solo en variables locales de programa.