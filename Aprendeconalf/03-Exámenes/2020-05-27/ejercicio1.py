#Escribir un programa al que al introducirle la altura de una línea sea capaz de dibujarla en diagonal con asteriscos. Por ejemplo, si introducimos altura = 5 dibujaría lo siguiente:
#     *
#    *
#   *
#  *
# *

altura = int(input('Ingrese altura: '))
cont = altura

for i in range(altura):
    cont -= 1
    print(' '*cont+'*')

