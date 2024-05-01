#Simulate a 10 seconds countdown by displaying the numbers, and finaly display "TAKE OFF!"

import time # Importo la biblioteca time porque tiene la función sleep.
cntdwn = [10,9,8,7,6,5,4,3,2,1] # Declaro la lista.

for num in cntdwn: # Para cada elemento de la lista, que se asigne a la variable.
    print(num) # Imprimo la variable.
    time.sleep(1) # Un segundo de suspenso.

print("TAKE OFF!") # Imprimo el densenlace.
