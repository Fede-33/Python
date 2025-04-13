# ENUMERATE

Se trata de una función que, en una iteración **for**, permite extraer tanto los elementos de una lista, como sus índices, mediante la sintaxis *for **i**, **v** in enumerate(**lista**)* donde **i** es el índice y **v** es el valor del elemento en cada iteración de la colección **lista**. Por ejemplo

    >>>lista = ["Papa","Batata","Cebolla"]
    >>>for i , v in enumerate(lista):
        print(i, v)
    0 Papa
    1 Batata
    2 Cebolla

Una de las personalizaciones de la función, implica elegir el valor de inicio del índice, mediante la sintaxis *for **i**, **v** in enumerate(**lista**, start = **n**)* donde **n** es un número entero. Ejemplo:

    >>>lista = ["Papa","Batata","Cebolla"]
    >>>for i , v in enumerate(lista, start = 1):
        print(i, v)
    1 Papa
    2 Batata
    3 Cebolla