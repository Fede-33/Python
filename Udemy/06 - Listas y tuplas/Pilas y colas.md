# PILAS

Para el manejo de listas existen dos paradigmas, el de **pilas** se administra mediante el principio **LIFO (Last In First Out)** Es decir, que el último elemento en ingresar es el primero en ser eliminado. Es la forma más sencilla de trabajar en Python, ya que los métodos *.append()* y *.pop()* tienen una sintaxis directa para hacerlo.

    EJEMPLO    
        >>> lista = []
        >>> lista.append(1)
        >>> lista.append(2)
        >>> lista.append(3)
        >>> print(lista)
        [1, 2, 3]
        >>> lista.pop()
        3
        >>> print(lista)
        [1, 2]

# COLAS

El paradigma de **colas** se administra mediante el principio **FIFO (First In First Out)** Es decir, que el primer elemento en ingresar es el primero en eliminarse. Esto puede realizarse utilizando los métodos de listas *.append()* y *.pop(0)* especificando en este último el índice 0, para que se elimine el primer elemento. 

    EJEMPLO    
        >>> lista = []
        >>> lista.append(1)
        >>> lista.append(2)
        >>> lista.append(3)
        >>> print(lista)
        [1, 2, 3]
        >>> lista.pop(0)
        1
        >>> print(lista)
        [2, 3]

También existe una librería llamada *collections* que incluye a la función *deque()*, que retorna una objeto *deque([])* que funciona como una lista pero tiene sus propios métodos, por ejemplo *.popleft()* que elimina el primer elemento del objeto.

    EJEMPLO    
        >>> from collections import deque
        >>> print(lista)
        deque([])
        >>> print(type(lista))
        <class 'collections.deque'>
        >>> lista.append(1)
        >>> lista.append(2)
        >>> lista.append(3)
        >>> print(lista)
        deque([1, 2, 3]) 
        >>> lista.popleft()
        1
        >>> print(lista)
        [2, 3]