# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')
c = 0

for i in range(len(frase)):
    if frase[i] == letra:
        c += 1

print(f'La letra {letra} está {c} veces en la frase.')
