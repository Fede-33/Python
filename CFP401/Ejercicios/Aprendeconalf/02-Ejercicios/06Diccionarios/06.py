# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

datos = {}
continuar = True


while continuar != 'N':
    clave = input('Dato a introducir: ')
    datos[clave] = input(f'Ingrese {clave}: ')
    print(datos)
    continuar = input('¿Desea continuar? (S/N) ').upper()

