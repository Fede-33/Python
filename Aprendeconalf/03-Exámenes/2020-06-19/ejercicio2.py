#Escribir una función que tome una lista de números enteros desordenados y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

def listar(nums):
    pares = []
    impares = []
    nums.sort()

    for i in nums:
        if (i % 2) == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    return pares, impares

tupla = listar([0,1,2,3,4,5,6,7,8,9,10])
print(f'Pares: {tupla[0]}')
print(f'Impares: {tupla[1]}')
