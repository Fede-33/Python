# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Veg: Pimiento, Tofu
# No Veg: Pepperoni, Jamón, Salmón
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipo = None
ingred = None

def rta(tip, ing):
    print(f'Ordenó una pizza {tip} de Mozarella y {ing}.')

while tipo == None:
    try :
        tipo = input('¿Es vegetariano? (S/N)').upper()
        if tipo != 'N' and tipo != 'S':
            tipo = None
            raise RuntimeError
    except RuntimeError :
        print('Respuesta incorrecta\n')

if tipo == 'S' :
    while ingred == None:
        try :
            ingred = int(input('Seleccione ingrediente (Pimiento = 1, Tofu = 2)'))
            if ingred != 1 and ingred != 2:
                ingred = None
                raise RuntimeError
        except (ValueError, RuntimeError):
            print('Respuesta incorrecta\n')
    if ingred == 1 :
        rta('Vegetariana', 'Pimiento')
    else :
        rta('Vegetariana', 'Tofu')
else:
    while ingred == None:
        try :
            ingred = int(input('Seleccione ingrediente (Pepperoni = 1, Jamón = 2, Salmón = 3)'))
            if ingred < 1 or ingred > 3:
                ingred = None
                raise RuntimeError
        except (ValueError, RuntimeError):
            print('Respuesta incorrecta\n')
    if ingred == 1 :
        rta('No vegetariana', 'Pepperoni')
    elif ingred == 2:
        rta('No vegetariana', 'Jamón')
    else :
        rta('No vegetariana', 'Salmón')


        
    
