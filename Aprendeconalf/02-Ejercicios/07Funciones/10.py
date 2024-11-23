#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def dec_bi (n):
    binario = []
    while n != 0:
        binario.append (str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario)

def bi_dec(n):
    n = list(n)
    n.reverse()
    dec = 0
    for i in range(len(n)):
        dec += int(n[i]) * 2 ** i
    return dec

print(dec_bi(22))
print(bi_dec('10110'))