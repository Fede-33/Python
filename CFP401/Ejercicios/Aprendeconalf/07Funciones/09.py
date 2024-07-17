#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcd (n1, n2):
    div_n1 = []
    div_comun = []

    for i in range(1, n1 + 1 ):
        if (n1 % i) == 0:
            div_n1.append(i)
    
    for i in range (1, n2 + 1):
        if (n2 % i) == 0 and i in div_n1 :
            div_comun.append(i)

    return(max(div_comun))

def mcm (n1, n2):
    if n1 > n2:
        mayor = n1
    else:
        mayor = n2
    while (mayor % n1 != 0) or (mayor % n2 != 0):
        mayor += 1
    return mayor


print(mcd(24,36))
print(mcm(24,36))


#Otra forma mcd:

def mcd2(n1, n2):
    rest = 0
    while(n2 > 0):
        rest = n2
        n2 = n1 % n2
        n1 = rest
    return n1

print(mcd2(24,36))