# Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.

def p_tipica (lista):
    media = sum(lista)/len(lista)
    for i in lista:
        sumatoria = (i-media)**2
    desviacion = (sumatoria/len(lista))**0.5

    solucion= []
    for i in lista:
        puntipica = (i - media)/desviacion
        if puntipica < -3 or puntipica > 3:
            solucion.append(i)
    
    return solucion

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]

print(p_tipica(valores))