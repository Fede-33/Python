# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

ingreso = ''

while ingreso != 'salir':
    print(ingreso)
    ingreso = input('Ingrese algo o "salir" para terminar: ')
    