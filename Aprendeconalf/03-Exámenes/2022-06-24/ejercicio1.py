# Las matemáticas financieras, resumidas en una frase, las podríamos definir como la rama de las matemáticas que estudia los flujos de dinero a través del tiempo. Básicamente se presupone que el dinero tiene menos valor en el futuro que en el presente, ya sea por un tema inflacionario o por la preferencia natural de las personas a priorizar el consumo presente. El valor futuro es el valor alcanzado por un determinado capital al final del período determinado (para el ejemplo usaremos la fórmula del interés compuesto). Para calcularlo se utiliza la siguiente fórmula:

                # VF = VA * (1+i)**n 

# El valor presente de una inversión es cuando calculamos el valor actual que tendrá una determinada cantidad que recibiremos o pagaremos en un futuro. Para calcularlo se utiliza la siguiente fórmula:

                # VA = VF / ((1+i)**n)
            
            # Donde 
                # VF es el valor futuro, 
                # VA es el valor actual o inicial de la inversión, 
                # i es el tipo de interés 
                # n es número de años de la inversión.

    #1 Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el valor futuro de la inversión cada año del periodo indicado.

def valor_futuro(va, i, tiempo):
    print('VALOR FUTURO:')
    for n in range(1, tiempo+1):
        vf = round((va * (1 + i/100)**n),2)
        print(f'Año {n} valor: {vf}')

    # Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el valor actual del capital cada año del periodo indicado.

def valor_actual(vf, i, tiempo):
    print('VALOR ACTUAL:')
    for n in range(1, tiempo+1):
        va = round(vf / ((1 + i/100)**n),2)
        print(f'Año {n} valor: {va}')


while True:
    try: 
        capital = float(input('ingrese capital:'))
        interes = float(input('ingrese tipo de interés:'))
        tiempo = int(input('ingrese cantidad de años:'))
        break
    except:
        print('Valor incorrecto')


valor_futuro(capital, interes, tiempo)
valor_actual(capital, interes, tiempo)
