# EXCEPCIONES

Cuando ocurre un error durante la ejecución de un programa, Python crea un objeto especial llamado *excepción*. Si no se controla esta excepción la ejecución del programa se detiene y se muestra el error o *traceback*.

    >>> print(1 / 0)  # Error al intentar dividir por 0.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

## TIPOS DE EXCEPCIONES:

Los principales excepciones definidas en Python son:

|EXCEPCIÓN|SIGNIFICADO|
|-|-|
|TypeError | Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
|ZeroDivisionError | Ocurre cuando se itenta dividir por cero.
|OverflowError | Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
|IndexError | Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
|KeyError | Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
|FileNotFoundError | Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
|ImportError | Ocurre cuando falla la importación de un módulo.

Consultar la documentaciónde Python para ver la lista de exepciones predefinidas.

## CONTROL DE EXCEPCIONES:

Para evitar la interrupción de la ejecución del programa cuando se produce un error, es posible controlar la exepción con la siguiente instrucción:

>try:
>>**código 1**

>except **excepción**:
>>**código 2**

>else:
>>**código 3**

Esta instrucción ejecuta el *código 1* y si se produce un error que genera una excepción del tipo *excepción* entonces ejecuta el *código 2*, mientras que si no se produce ningún error, se ejecuta el *código 3*.

### EJEMPLO:

    >>> def division(a, b):
    ...     try:
    ...         result = a / b
    ...     except ZeroDivisionError:
    ...         print('¡No se puede dividir por cero!')
    ...     else:
    ...         print(result)
    
    >>> division(1, 0)
    ¡No se puede dividir por cero!
    >>> division(1, 2)
    0.5

    >>> try:
    ...     f = open('fichero.txt')  # El fichero no existe
    ... except FileNotFoundError:
    ...     print('¡El fichero no existe!')
    ... else:
    ...     print(f.read())
    
    ¡El fichero no existe!

