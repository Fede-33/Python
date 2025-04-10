# Desarrollar un programa para verificar si una palabra ingresada es un palíndromo:

texto = input('Ingresar palabra o frase a comprobar: ')

texto_formateado = texto.replace(' ', '').lower()

print(f'"{texto}" es palíndromo.' if texto_formateado == texto_formateado[::-1] else f'"{texto}" no es palíndromo.')