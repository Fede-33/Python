# Tuplas

Una tupla es una secuencia ordenadas de objetos de distintos tipos. Se usan habitualmente para representar colecciones de datos una determinada estructura semántica, como por ejemplo un vector o una matriz. Se caracterizan por:

* Tienen orden.
* Pueden contener elementos de distintos tipos.
* Son inmutables, es decir, no pueden alterarse durante la ejecución de un programa.

## CREACIÓN:

Se construyen poniendo los elementos entre paréntesis ( ) separados por comas.

    # Tupla vacía
    type(())
    <class 'tuple'>
    # Tupla con elementos de distintos tipos
    (1, "dos", True)
    # Vector
    (1, 2, 3)
    # Matriz
    ((1, 2, 3), (4, 5, 6))

Otra forma de crear tuplas es mediante la función tuple(). Crea una tupla con los elementos de la secuencia que se especifica entre paréntesis. Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de elementos iterable.

    >>> tuple()
    ()
    >>> tuple(1, 2, 3)
    (1, 2, 3)
    >>> tuple("Python")
    ('P', 'y', 't', 'h', 'o', 'n')
    >>> tuple([1, 2, 3])
    (1, 2, 3)

## OPERACIONES:

El acceso a los elementos de una tupla se realiza del mismo modo que en las listas. También se pueden obtener subtuplas de la misma manera que las sublistas. Las operaciones de listas que no modifican la lista también son aplicables a las tuplas.

    >>> a = (1, 2, 3)
    >>> a[1]
    2
    >>> len(a)
    3
    >>> a.index(3)
    2
    >>> 0 in a
    False
    >>> b = ((1, 2, 3), (4, 5, 6))
    >>> b[1]
    (4, 5, 6)
    >>> b[1][2]
    6

