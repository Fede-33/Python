# A veces, al tratar con tuplas, podemos tener un problema en el que necesitamos extraer solo K elementos extremos, es decir, los K máximos y mínimos. Este problema puede tener aplicaciones en campos como el desarrollo web y la ciencia de datos. Desarrollar un programa que dada una tupla y un número K devuelva otra tupla con los K elementos máximos y mínimos.

# Ejemplo:

# La tupla original es: (5, 20, 3, 7, 6, 8) 
# La tupla con los k = 2 máximos y mínimos es: (3, 5, 8, 20) 

tupla = (5, 20, 3, 7, 6, 8)
k = 2
lista = list(tupla)

res=[]

for i in range(k):
    res.append(lista.pop(lista.index(min(lista))))
    res.append(lista.pop(lista.index(max(lista))))

res.sort()

tupla_2 = tuple(res)

print(tupla_2)
