# Escribir un programa que simule el famoso juego del ahorcado. El programa debe cumplir los siguientes requisitos:

#El programa debe preguntar al usuario la palabra a adivinar. A partir de la palabra introducida debe crear una lista con los caracteres de la palabra.
#Después debe ir preguntando al usuario por letras hasta un máximo de 5 fallos o hasta que no queden letras en la lista. En ambos casos el programa terminará pero mostrará el mensaje “Perdiste” si se comenten 5 fallos y el mensaje “Ganaste” si no quedan palabras en la lista.
#Cada vez que el usuario introduzca una nueva letra, si la letra está en la lista la eliminará y mostrará el mensaje “Acierto”, mientras que si la letra no está en la lista mostrará el mensaje “Fallo”. Si la letra está más de una vez en la lista, sólo se eliminará la primera instancia que aparezca.
#El programa debe guardarse dentro de la carpeta respuestas con el nombre ejercicio3.py.
#Cuando el programa esté terminado, añadir el fichero ejercicio3.py a la zona de intercambio temporal y hacer un commit con el mensaje “Añadida respuesta ejercicio 3”.
#Requisito adicional para un punto extra: Cada vez que el usuario acierte una letra debe mostrar la palabra a adivinar con las letras acertadas hasta el momento y el resto reemplazadas por asteriscos.

ingreso = input('Ingrese la palabra a adivinar: ').lower()
palabra = list(ingreso)
cont = 5
listacontrol = palabra
resultado = []

resultado = ['*'] * len(palabra)

while cont != 0 and palabra != []:
    print(f'Quedan {cont} fallos - Su palabra es {"".join(resultado)}')
    letra = input('Ingrese una letra: ')
    if letra in palabra:
        print('Acierto')
        for i in range(len(resultado)):
            if list(ingreso)[i] == letra:
                resultado[i] = letra
                palabra.remove(letra)
    else:
        cont -= 1
        print('Fallo')

if palabra == []:
    print(f'Ganaste, la palabra es {ingreso}')
else:
    print(f'Perdiste, la palabra es {ingreso}')
    
    