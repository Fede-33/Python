# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

datos = {}
campos = ('nombre', 'edad', 'direccion', 'tel')

for i in campos:
    datos[i] = input(f'Ingrese su {i}: ')


print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['tel']}.")
