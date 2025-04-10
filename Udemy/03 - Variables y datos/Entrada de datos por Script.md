# LIBRERÍA SYS

Puede importarse la librería **sys** para ejecutar el código por terminal, agregándole argumentos en la línea de ejecución.
La función **sys.argv** retornará una lista en la que el primer elemento es el nombre del archivo que contiene el código, y los elementos sucesivos son cada uno de los argumentos ingresados en la terminal al momento de ejecutar el fichero.

    CODIGO:
        import sys
        data = sys.argv
        print(data)

    EJECUCIÓN:
        > python3 entrada_por_script.py blabla pepepe 234 'Juan Pérez'
            ['entrada_por_script.py', 'blabla', 'pepepe', '234', 'Juan Pérez']

Si se desea ingresar un solo argumento compuesto por dos o más palabras, debe hacerse entre comillas (simples o dobles) para que sea considerado un solo elemento.