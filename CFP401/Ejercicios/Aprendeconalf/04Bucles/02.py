# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = None

while edad == None:
    try:
        edad = int(input('Ingrese su edad: '))
        if edad < 0:
            edad = None
            raise RuntimeError            
    except (ValueError, RuntimeError):
        print('Ingrese una edad válida.\n')

for i in range(1, edad+1):
    print(i)