# Escribe un programa en python que permita guardar las notas de un alumno conseguidas en un cuatrimestre. Guarda la información en un diccionario cuyas claves sean las asignaturas y los valores las notas de cada asignatura. El programa pedirá la asignatura y la nota para esa asignatura. Si se recibe un número negativo en la nota, el programa termina y muestra las asignaturas suspensas.

diccionario = {}
nota = 0

while nota >= 0:
    asignatura = input('Ingrese una asignatura: ')
    nota = int(input('Ingrese una nota: '))
    if nota >= 0 :
        diccionario[asignatura] = nota

for i in diccionario.keys():
    if diccionario[i] < 7:
        print (i)
