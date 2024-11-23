# Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

matriz1 = ((1, 2, 3), 
           (4, 5, 6))
matriz2 = ((-1, 0), 
           (0, 1), 
           (1, 1))
resultante= [[0, 0],
             [0, 0]]



for i in range(len(matriz1)):
    for j in range(len(matriz2[i])):
        for k in range(len(matriz2)):
            resultante [i][j] += matriz1[i][k] * matriz2[k][j]
    


for i in range(len(resultante)):
    print(resultante[i])


