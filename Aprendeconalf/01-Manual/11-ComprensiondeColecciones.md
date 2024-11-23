# COMPRENSIÓN DE COLECCIONES

Cuando sea necesario operar con los elementos de una colección (Lista, Tupla o Diccionario) puede hacerse mediante bucles iterativos, o mediante la función *map()*. Pero existen mecanismos más simples en Python.

## COMPRENSIÓN DE LISTAS:

> [expresion **for** variable **in** lista **if** condicion]

Esa instrucción genera una lista que aplica la expresión a los valores de variable, iterados de una lista, si, y solo si, satisfacen la condición.

### EJEMPLO:
Aplicar el cuadrado (expresión) a cada elemento (variable) de un rango (lista) que sean pares (condición):

    [x ** 2 for x in range(10) if x % 2 == 0]
    >>> [0, 4, 16, 36, 64]

## COMPRENSIÓN DE DICCIONARIOS:

> {expresion-key:expresion-valor **for** variables **in** lista **if** condicion}

Esa instrucción genera un diccionario formado por los pares cuya expresión-key y expresión-valor cumplen con la condición.

### EJEMPLO:

Dado el siguiente arreglo:

    notas = {
        'Carmen':5, 
        'Antonio':4, 
        'Juan':8, 
        'Mónica':9, 
        'María': 6, 
        'Pablo':3
        }

Crear un nuevo arreglo con los alumnos con notas iguales o mayores a 6:

    {nombre: nota for (nombre, nota) in notas.items() if nota >= 6}
    >>> {'Carmen': 6, 'Juan': 9, 'Mónica': 10, 'María': 7}

