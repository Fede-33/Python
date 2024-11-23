# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = None

nom = input('Ingrese su nombre: ').capitalize()
while sexo == None :
    sexo = input('Ingrese su sexo (M/F): ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo incorrecto.')
        sexo = None
        
if sexo == 'M' :
    if nom[0] > 'N':
        print('\nGrupo A.')
    else :
        print('\nGrupo B.')
else :
    if nom[0] > 'N':
        print('\nGrupo B.')
    else :
        print('\nGrupo A.')