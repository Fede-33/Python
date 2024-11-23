#CONDICIONALES:

## IF:

    if condición1:
        bloque código
    elif condición2:
        bloque código
    …
    else :
        bloque código

Evalúa la expresión lógica *condición1* y ejecuta el primer bloque de código si es *True*, si no, evalúa la siguientes condiciones hasta llegar a la primera que es *True* y ejecuta el bloque de código asociado. Si ninguna condición es *True* ejecuta el bloque de código después de *else:*. Pueden aparecer varios bloques elif pero solo uno else al final. Los bloques de código deben estar indentados por 4 espacios. La instrucción condicional permite evaluar el estado del programa y tomar decisiones sobre qué código ejecutar en función del mismo.

    >>> edad = 14
    >>> if edad <= 18 : 
    ...     print('Menor')
    ... elif edad > 65:
    ...     print('Jubilado')
    ... else:
    ...     print('Activo')
    ...
    Menor
    >>> age = 20
    >>> if edad <= 18 : 
    ...     print('Menor')
    ... elif edad > 65:
    ...     print('Jubilado')
    ... else:
    ...     print('Activo')
    ...
    Activo

