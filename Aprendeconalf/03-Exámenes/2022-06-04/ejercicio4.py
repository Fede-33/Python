# Escriba un programa que obtenga el máximo y el mínimo de una serie de datos proporcionados en Hexadecimal. Para ello se le pasará una lista de datos en formato hexadecimal, y tendrá que convertirlos primero a formato Binario, y a continuación a formato Decimal. Para ello, se pide lo siguiente:

hexadec = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

    #1 Crear una función de conversión de formato hexadecimal a binario: 

def hex_bin (claves):
    conversion = ''
    while True:
        try:
            ingreso = input('Introduce un valor hexadecimal: ').upper()
            for i in ingreso:
                conversion = conversion + claves[i]
            break
        except KeyError:
            print(f'{ingreso} No es un valor hexadecimal.\n')
    
    return conversion

    #2 Crear una función de conversión de formato binario a decimal. El procedimiento se detalla a continuación:

def bin_dec(valor):
    decimal = 0
    valor = list(valor)
    valor.reverse()

    for i in range(len(valor)):
        decimal += int(valor[i])*(2**i)

    return decimal

#3 Crear una función que reciba una lista de números hexadecimales y devuelva una tupla con el máximo y su valor decimal.

def max_dec(lista, claves):
    diccionario = {}
    
    for i in lista:
        conversion = ''
        decimal = 0

        for j in i:
            conversion = conversion + claves[j]
        
        conversion = list(conversion)
        conversion.reverse()
        for k in range(len(conversion)):
            decimal += int(conversion[k])*(2**k)
        
        diccionario[i] = decimal

    maximo = max(diccionario.values())

    for l in diccionario.keys():
        if diccionario[l] == maximo:
            retorno = (l,diccionario[l])
    
    return retorno


lista_ejem = ["AA55", "1010", "BEBE", "0101", "0FEA"]

print(f'En binario es: {hex_bin(hexadec)}')
print(f'En decimal es: {bin_dec('1010101001010101')}')
print(f'Máximo: {max_dec(lista_ejem, hexadec)}')







#def max_dec(lista):

