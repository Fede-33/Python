# SLICING

Las cadenas pueden ser administradas mediante índices, accediento a los diferentes caracteres de su contenido, tal como las listas mediante una sintaxis de corchetes con los siguientes parámetros **[inicio:final:salto]** donde, la posición de *inicio* se incluye en la extracción, pero la final no.

    EJEMPLO    
        >>> text = 'Python'
        >>> print(text[2:])
        thon
        >>> print(text[:2])
        Py
        >>> print(text[::2])
        Pto

# MODIFICACIÓN

Los strings en Python son inmutables. Es decir, que no puede accederse a una posición de la cadena y modificar su contenido. Por ejemplo, si quisiéramos modificar la primera letra del texto *Python*:

    >>> text = 'Python'
    >>>print(text[0])
    P
    >>>text[0] = 'S'
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

Este error surge porque no puede asignarse un nuevo valor a una posición individual de la cadena. Pero sí podría reasignarse todo el contenido de la variable, agregando la letra deseada y concatenando parte del contenido anterior, de esta manera:
    
    >>> text = 'S' + text[1:]
    >>> print(text)
    Sython

De esta manera modificamos la variable por completo, asignándole una cadena de una letra, y los caracteres de la cadena anterior, excepto la primera letra.