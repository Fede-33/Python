# FORMAS DE IMPORTAR:

## import *modulo*

De esta forma se importa el módulo completo y cada vez que se llame alguna función del mismo, se deberá especificar **modulo.función**. Ejemplo, iportando el módulo **math** debemos llamar a la función **sqrt()** (raíz) y **fabs()** (valor absoluto) con la sintaxis de punto:

    import math

    print(math.sqrt(25))
    print(math.fabs(-25))

## from *modulo* import *función*

Esta sintaxis importa solo funciones específicas del módulo, y estas pueden invocarse por su nombre, sin necesidad de especificar el módulo al que pertenecen. Pueden importarse varias funciones en la misma línea de código, separándolas por coma. Por ejemplo, importando las funciones **sqrt()** y **fabs()** del módulo **math()** podemos llamar directamente a las funciones:  

    from math import sqrt, fabs

    print(sqrt(25))
    print(fabs(-25))

## as

La sentencia **as** puede utilizarse para agregar un alias tanto al módulo, como a las funciones importadas. Siguiendo con los ejemplos anteriores, podrían asignarse llos siguientes alias:

    import math as mt

    print(mt.sqrt(25))
    print(mt.fabs(-25))
    
    ---------------------------------------

    from math import sqrt as sq , fabs as fb

    print(sq(25))
    print(fb(-25))