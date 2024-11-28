#El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:
#Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
#Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
#Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

def diccionario():
    with open('./archivo_calif/calificaciones.csv', 'r') as f:
        datos = f.readlines()
        datos = [datos[0]] + sorted(datos[1:])
        claves = datos[0].split(';')
        claves[-1] = claves[-1].split('\n')[0]
        lista = []
        
        for i in range(1,len(datos)):
            diccionario = {}
            for j in range(len(claves)):
                valores = datos[i].split(';')
                valores[-1] = valores[-1].split('\n')[0]
                valores[j] = valores[j].replace(',', '.')
                if valores [j] == '':
                    valores[j] = 0
                try:
                    valores[j] = round(float(valores[j]), 2)
                except:
                    nada = ''
                diccionario[claves[j]] = valores[j]
            lista.append(diccionario)

    return lista
        
def notafinal(lista):
    for i in lista:
        nota = i['Parcial1'] *0.3 + i['Parcial2'] *0.3 + i['Ordinario1'] *0.3 + i['Ordinario2'] *0.3 + i['Practicas'] *0.4 + i['OrdinarioPracticas'] *0.4
        i['NotaFinal'] = round(nota, 2)
    
    return lista

def listados(lista):
    aprobados = []
    suspensos = []
    for i in lista:
        nombre = i['Apellidos'] +' '+ i['Nombre']
        if i['Asistencia'] >= '75%' and (i['Parcial1']+i['Ordinario1']) >= 4 and (i['Parcial2']+i['Ordinario2']) >= 4 and (i['Practicas'] + i['OrdinarioPracticas']) >= 4 and i['NotaFinal'] >= 5 :
            aprobados.append(nombre)
        else:
            suspensos.append(nombre)
    
    return (aprobados, suspensos)

def mostrar(a, s):
    print('LISTADO DE APROBADOS:\n')
    for i in a:
        print('\t',i)
    print('\n\nLISTADO DE SUSPENSOS:\n')
    for i in s:
        print('\t',i)


apr, sus = listados(notafinal(diccionario()))
mostrar(apr, sus)