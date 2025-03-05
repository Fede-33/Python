#1 Definir funciones para codificar y decodificar mensajes en código morse. Definir una función para codificar una palabra en código morse. Debe cumplir los siguientes requisitos:
    #Debe usarse el diccionario que se da.
    #El único parámetro de entrada de la función es una cadena con una palabra.
    #Debe devolver una cadena con el código morse correspondiente a la palabra, separando los bloques de código correspondientes a cada letra por punto y coma ;.

morse = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..'}

def morse_1 (cadena):
    resultado = ''
    for i in cadena.upper():
        try:
            resultado += morse[i] + ';'
        except:
            resultado += i + ';'
    return resultado

#2 Definir una función para decodificar una palabra en código morse. Debe cumplir los siguientes requisitos:
    # A partir del diccionario que se da se debe crear el diccionario invertido, es decir, un diccionario cuyas claves son los códigos morse y sus valores las letras correspondientes. Se valorará especialmente el uso de comprensión de diccionarios.
    # El único parámetro de entrada de la función es una cadena de código morse, donde los bloques de código correspondientes a cada letra van separados por puntos y coma ;.
    # Debe devolver una cadena con la palabra decodificada.

morse_inv={}
for i in morse.keys():
    morse_inv[morse[i]] = i

def morse_2(cadena):
    resultado = ''
    for i in cadena.upper().split(';'):
        try:
            resultado += morse_inv[i]
        except:
            resultado += i
    return resultado

#3 Definir una función para codificar un mensaje en código morse. Debe cumplir los siguientes requisitos:
    #Debe usarse la función anterior para codificar palabras.
    #El único parámetro de entrada de la función es una cadena con un mensaje (palabras separadas con espacios).
    #Debe devolver una cadena con las palabras del mensaje codificadas y separadas por espacios.
    #Se valorará especialmente el uso de programación funcional.

def morse_1 (cadena):
    resultado = ''
    for i in cadena.upper():
        try:
            resultado += morse[i] + ';'
        except:
            resultado += i + ';'
    return resultado

#4 Definir una función para decodificar un mensaje en código morse. Debe cumplir los siguientes requisitos:
    #Debe usarse la función anterior para decodificar palabras.
    #El único parámetro de entrada de la función es una cadena con un mensaje en código morse (letras separadas por punto y coma, y palabras separadas con espacios).
    #Debe devolver una cadena con las palabras del mensaje decodificadas y separadas por espacios.
    #Se valorará especialmente el uso de programación funcional.

def morse_2(cadena):
    resultado = ''
    for i in cadena.upper().split(';'):
        try:
            resultado += morse_inv[i]
        except:
            resultado += i
    return resultado