# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def stats(lista):
    media = 0
    var = 0

    for i in lista:
        media += i
    media = media / len(lista)
    
    for i in lista:
        var += (i - media)**2
    var = var / (len(lista))

    desv = var ** (0.5)

    return {    
        'Media': media,
        'Varianza': var,
        'Desviación': desv
    }

print(stats([1, 2, 3, 4, 5]))


# Otra forma. Utilizando la función creada en el ejercicio anterior. En este caso se llama a la función con una lista

def square(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))

# Otra forma. Usando la función del ejercicio anterior, pero con un argumento variable, entonces pueden ingresar los números como valores libres, no solo somo una lista.

def square(*sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(*sample):
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(*sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics(1, 2, 3, 4, 5))
