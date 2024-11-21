# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

def reporte (notas):
    reporte = {}
    for i in notas.keys():
        if notas [i] >= 7:
            reporte [i.capitalize()] = 'Aprobado'
        else :
            reporte [i.capitalize()] = 'Reprobado'
    return reporte

alumnotas = {
    'matemática' : 7,
    'lengua' : 5,
    'sociales' : 6,
    'naturales' : 9
}

print(reporte(alumnotas))