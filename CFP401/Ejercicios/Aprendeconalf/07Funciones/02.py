#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo(nom):
    print(f'¡hola {nom.title()}!')

nombre = input('Ingrese su nombre: ')
saludo(nombre)