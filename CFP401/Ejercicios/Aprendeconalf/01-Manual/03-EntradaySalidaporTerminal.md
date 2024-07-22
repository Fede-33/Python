#ENTRADA Y SALIDA POR TERMINAL

## ENTRADA:

Para asignar a una variable un valor introducido por el usuario en la consola se utiliza la instrucción *input()*

**input(n)** Muestra la cadena **n** por la terminal y devuelve una cadena con la entrada del usuario. El valor devuelto siempre es una cadena, incluso si el usuario introduce un dato numérico.

    >>> language = input('¿Cuál es tu lenguaje favorito? ')
    ¿Cuál es tu lenguaje favorito? Python
    >>> language
    'Python'
    >>> age = input('¿Cuál es tu edad? ')
    ¿Cuál es tu edad? 20
    >>> age
    '20'

## SALIDA:

Para mostrar un dato por la terminal se utiliza la instrucción *print()*

**print(dato1, ..., sep=' ', end='\n', file=sys.stdout)**

* **dato1, ...** son los datos a imprimir y pueden indicarse tantos como se quieran separados por comas.
* **sep** establece el separador entre los datos, que por defecto es un espacio en blanco ' '.
* **end** indica la cadena final de la impresión, que por defecto es un cambio de línea \n.
* **file** indica la dirección del flujo de salida, que por defecto es la salida estándar sys.stdout.

      >>> print('Hola')
      Hola
      >>> name = 'Alf'
      >>> print('Hola', name)
      Hola Alf
      >>> print('El valor de pi es', 3.1415)
      El valor de pi es 3.1415
      >>> print('Hola', name, sep='')
      HolaAlf
      >>> print('Hola', name, end='!\n')
      Hola Alf!

