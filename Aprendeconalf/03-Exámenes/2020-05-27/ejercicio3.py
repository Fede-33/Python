#El fichero horas-trabajo.csv contiene el número de horas mensuales trabajadas por los empleados de una empresa durante el primer cuatrimestre. Crear un programa que realice las siguientes operaciones sin utilizar la librería Pandas:

    #1 Leer el fichero de internet https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2020-05-27/horas-trabajo.csv y crear una lista con las líneas del fichero.
from urllib import request

f = request.urlopen('https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2020-05-27/horas-trabajo.csv')
lineas_bytes = f.readlines()
f.close()

lista = []
for i in lineas_bytes:
    lista.append(i.decode('utf-8').strip().split(';')) #para sacar el formato bytes de importación, y luego separar los valores (formando una lista de listas)

    #2 Mostrar por pantalla las horas totales del primer operario.

total = 0
for i in range(2, len(lista[1])):
    total += float(lista[1][i])

print(f'Horas trabajadas por el primer operario: {total}')

    #3 Crear un diccionario de diccionarios tal que las claves del diccionario principal serán los identificadores de los operarios y sus valores serán, a su vez, otros diccionarios cuyas claves serán los meses y sus valores las horas trabajadas en esos meses para cada operario. Es decir, un diccionario como el siguiente:

        #{'OP1': {'Enero': '180', 'Febrero': '160', 'Marzo': '140', 'Abril': '180'}, 'OP2': {'Enero': '120', 'Febrero': '140', 'Marzo': '', 'Abril': '100'}, ... }

diccionario = {}

for i in range (1, len(lista)):
    dicc_temp = {}
    for j in range (2, len(lista[i])):
        dicc_temp[lista[0][j]] = lista[i][j]
    diccionario[lista[i][0]] = dicc_temp

    #4 Crear una función que reciba la base de datos de las horas trabajadas (puede utilizarse el diccionario del apartado anterior u otra estructura de datos), el identificador de un operario y el precio de la hora, y devuelva una tupla con el número totales de horas trabajadas y el salario de ese operario.

def salario(datos, id, valor):

    horas = 0
    
    try:
        for i in datos[id].values():
            horas += float(i)
    except:
        print(f'El operario {id} no existe.')
    
    sueldo = horas * valor

    return (horas, sueldo)

print(salario(diccionario, 'OP1', 10))