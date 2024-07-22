# INTRODUCCIÓN A PYTHON:

Python es un lenguaje de programación de alto nivel multiparadigma que permite:
* Programación imperativa
* Programación funcional
* Programación orientada a objetos

Creado por Guido van Rossum en 1990 aunque actualmente es desarrollado y mantenido por la Python Software Foundation

## VENTAJAS DE PYTHON:

* Es de código abierto (certificado por la OSI).
* Es interpretable y compilable.
* Es fácil de aprender gracias a que su sintaxis es bastante legible para los humanos.
* Es un lenguaje maduro (29 años).
* Es fácilmente extensible e integrable en otros lenguajes (C, java).
* Esta mantenido por una gran comunidad de desarrolladores y hay multitud de recursos para su aprendizaje.

## TIPOS DE EJECUCIÓN:

### CONSOLA:

Se ejecuta cada instrucción que introduce el usuario de manera interactiva.

    > python3
    >>> name = "Alf"
    >>> print("Hola ", name)
    Hola Alf

### FICHEROS:

Se leen y se ejecutan una a una todas las instrucciones del fichero.

    # Fichero hola.py
    name = "Alf"
    print("Hola ", name)

    > python3 hola.py
    Hola Alf

También se puede hacer el fichero ejecutable indicando en la primera línea la ruta hasta el intérprete de Python.

    #!/usr/bin/python3
    name = "Alf"
    print("Hola", name)

    > chmod +x hola.py
    > ./hola.py
    Hola Alf

### COMPILADO A BYTECODE:

    # Fichero hola.py
    name = "Alf"
    print("Hola " + name)

    > python -O -m py_compile hola.py
    > python __pycache__/hola.cpython-37.pyc
    Hola Alf

### COMPILAR A EJECUTABLE DEL SISTEMA:

Hay distintos paquetes que permiten compilar a un ejecutable del sistema operativo usado, por ejemplo pyinstaller.

    > conda install pyinstaller
    > pyinstaller hola.py
    > ./dist/hola/hola
    Hola Alf

