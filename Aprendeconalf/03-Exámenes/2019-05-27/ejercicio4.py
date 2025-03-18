# Definir una función que reciba un número entero entre 0 y 999, y devuelva una cadena con la cantidad introducida en palabras. Por ejemplo, si se introduce 647 debe devolver la cadena “seiscientos cuarenta y siete”. La función debe cumplir los siguientes requisitos:

#El único parámetro de entrada de la función es un número entero entre 0 y 999.
#Deben usarse diccionarios para emparejar cada dígito con la palabra correspondiente para las unidades, decenas y centenas.
#Debe devolver una cadena con la cantidad introducida en palabras.

def numero_a_palabras(numero):

    if not isinstance(numero, int) or numero < 0 or numero > 999:
        return "Número fuera de rango (0-999)"

    unidades = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }

    decenas = {
        10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
        15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
        20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
        60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa"
    }

    centenas = {
        100: "ciento", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos",
        500: "quinientos", 600: "seiscientos", 700: "setecientos", 800: "ochocientos", 900: "novecientos"
    }

    if numero == 0:
        return unidades[0]

    palabras = []

    if numero >= 100:
        centena = (numero // 100) * 100
        palabras.append(centenas[centena])
        numero %= 100

    if numero >= 10:
        if numero in decenas:
            palabras.append(decenas[numero])
            numero = 0
        else:
            decena = (numero // 10) * 10
            palabras.append(decenas[decena])
            numero %= 10

    if numero > 0:
        palabras.append(unidades[numero])

    return " ".join(palabras)

print(numero_a_palabras(647))   
print(numero_a_palabras(83))   
print(numero_a_palabras(100))  
print(numero_a_palabras(0))    
print(numero_a_palabras(999))  