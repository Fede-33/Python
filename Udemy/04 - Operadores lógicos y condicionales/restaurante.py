# Solicitando al usuario el monto consumido en el restaurante, calcular descuentos según:
    #  Consumo > $50 descuento 10%
    #  Consumo > $100 descuento 20%
    #  Consumo > $200 descuento 30%
# Mostrar resumen con Consumo, Descuento, Precio Final

consumo = float(input('Ingrese monto consumido: '))

if consumo > 50:
    desc = consumo * 0.1
    if consumo > 200:
        desc = consumo * 0.3
    elif consumo > 100:
        desc = consumo * 0.2
    total = consumo - desc
    print(f'{'-'*30}\nConsumo: ${consumo:.2f}\nDescuento: ${desc:.2f}\n{'-'*30}\nTotal:{total:.2f}\n{'-'*30}')
else:
    print(f'{'-'*30}\nConsumo: ${consumo:.2f}\nSin descuento\n{'-'*30}\nTotal:{consumo:.2f}\n{'-'*30}')
            