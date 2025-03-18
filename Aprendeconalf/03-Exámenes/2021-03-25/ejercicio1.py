# El cálculo del IRPF en la Hacienda española se define como progresivo. Hacienda divide los ingresos (tu renta) en tramos y asigna un porcentaje a pagar en cada uno de ellos. Estos tramos son los siguientes:

    #Desde 0 hasta 12.450€	19%
    #De 12.450€ a 20.200€	24%
    #De 20.200€ a 35.200€	30%
    #De 35.200€ en adelante	37%

#Por ejemplo, para una persona con una renta de 65.000€, el cálculo del impuesto se haría así:
#Primer tramo IRPF: se paga el 19% de 12.450 euros, es decir, 2.365,5 euros
#Segundo tramo IRPF: se paga el 24% de 7.750 euros (la diferencia entre el primer y segundo tramo), es decir, 1.860 euros.
#Tercer tramo IRPF: se paga el 30% de 15.000 euros (la diferencia entre el segundo y tercer tramo), es decir, 4.500 euros.
#Cuarto tramo IRPF: se paga el 37% de 29.800 euros (la diferencia entre su renta y el límite del tercer tramo), es decir, 11.026 euros.
#La suma de las anteriores cantidades es el total a pagar: 19.751,5 euros.

#Escribir un programa que pregunte por la renta del usuario y muestre por pantalla el IRPF que debe pagar a Hacienda.

renta = float(input('Ingrese renta anual: '))

if renta <= 12450:
    impuesto = renta * 0.19
elif renta <= 20200:
    impuesto = (2365.5) + (renta-12450) * 0.24
elif renta <= 35200:
    impuesto = (2365.5) + (1860) + (renta-20200)*0.3
else:
    impuesto = (2365.5) + (1860) + (4500) + (renta-35200)*0.37

print(f'Debe pagar €{impuesto}')
