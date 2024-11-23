# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

def calificar (notas):
    calificaciones = []
    for i in notas:
        if i >= 7:
            calificaciones.append('Aprobado')
        else:
            calificaciones.append('Reprobado')
    return calificaciones

lista = [5, 8, 3, 6, 9, 10, 4]
calificado = calificar(lista)

for i in range(len(calificado)):
    print (lista[i], " : ", calificado[i])
