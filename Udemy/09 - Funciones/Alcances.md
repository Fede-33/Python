# ALCANCE DE VARIABLES Y FUNCIONES:

## VARIABLES GLOBALES Y LOCALES:
Todas las variables definidas dentro de una función, solo podrán ser utilizadas dentro de la misma función, no serán variables globales. En caso de que una variable global sea redefinida o modificada dentro de una función, tan solo cambiará su valor dentro de esa función, pero no en el código global. Por ejemplo, definiremos una variable global **resultado** igual 0, y una función que sume dos números, retornando una variable local de la función también llamada **resultado**.

    resultado = 0
    def suma(n_1, n_2):
        resultado = n_1 + n_2
        return resultado
    
    print(suma(10,20))
    print(resultado)

Este código al ser ejecutado arrojará la siguiente resupesta:

    30
    0

Es decir, que la función **suma** realizó el procedimiento, sumando los números, almacenándolos en la variable local **resultado**, y retornándolo. Mientras que la variable global **resultado** no cambió.
    
## FUNCIONES INTERNAS Y EXTERNAS:

Cuando una función se define dentro de otra función, entonces esa función interna pasará a ser local de la función externa. Poir ejemplo:

    def f_ext():
        def f_int():
            print('lalala')

    f_ext()
    f_int()

El código anterior incurriría en un error cuando se intenta llamar a **f_int()** desde la línea de código general, retornando el mensaje que indica que **f_int()** no se encuentra definida. 

## GLOBAL:

Mediante la palabra clave **global** en Python se indica cuando una variabla o función podrá ser utilizada globalmente, es decir, que cuando se defina o redefina dentro de otra función, modificará la variable en todas sus instancias, tanto localmente como globalmente. Esta orden se debe especificar antes de que se declare localmente la función o variable. Retornando a los ejemplos anteriores:

    resultado = 0
    def suma(n_1, n_2):
        global resultado
        resultado = n_1 + n_2
        return resultado
    
    print(suma(10,20))
    print(resultado)

Este código al ser ejecutado arrojará la siguiente resupesta:

    30
    30

Mientras que el siguiente código no arrojará ningún tipo de error:

    def f_ext():
        global f_int()
        def f_int():
            print('lalala')

    f_ext()
    f_int()
