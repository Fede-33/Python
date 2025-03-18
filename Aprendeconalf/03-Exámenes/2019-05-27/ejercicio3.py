# Escribir un programa para ver los beneficios de una empresa en un periodo de años. El programa debe cumplir los siguientes requisitos:

#El programa tiene que preguntar al usuario por un año inicial y otro final, y después preguntar por los ingresos y los gastos de cada año desde el año inicial hasta el año final.
#Con los datos introducidos se deben crear dos listas, una con los ingresos y otra con los gastos, de manera que los ingresos y los gastos de cada año aparezcan en la misma posición de las listas.
#El programa debe crear otra lista con el beneficio de cada año (ingresos menos gastos) y mostrarla por pantalla.
#El programa debe crear otra lista booleana que indique para cada año si ha habido beneficios o no y mostrarla por pantalla.
#Finalmente el programa debe mostrar por pantalla la lista de los años con beneficios la lista de los años con pérdidas.

ingreso = []
gasto = []
beneficio = []
booleana = []
fecha = []

inicio = int(input('Ingrese año inicial: '))
fin = int(input('Ingrese año final: '))
for i in range(inicio, fin+1):
    fecha.append(i)

for i in range(len(fecha)):
    ingreso.append(float(input(f'Ingresos del año {fecha[i]}: ')))
    gasto.append(float(input(f'Gastos del año {fecha[i]}: ')))
    beneficio.append(ingreso[i]-gasto[i])
    if beneficio[i] > 0:
        booleana.append(True)
    else:
        booleana.append(False)


print ('Beneficios por año:')
for i in range(len(fecha)):
    print (f'Año {fecha[i]}: {beneficio[i]} - Beneficio: {booleana[i]}')

print ('Años con Beneficios:')
for i in range(len(fecha)):
    if booleana[i] == True:
        print(fecha[i])

print ('Años con Pérdidas:')
for i in range(len(fecha)):
    if booleana[i] == False:
        print(fecha[i])

