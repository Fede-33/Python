#Ask the user to insert numbers or insert the key word "done" to finish. All the numbers must be stored in a list, that has to be displayed at the end.

list = [] # Defino la lista y la variable sin valores.
var = ''

while var != 'done': # Mientras var sea distinto de done.
    if var : # Chequeo que var tenga un valor
        list.append(int(var)) # Agrego el elemento al final de la lista.
    var = input("Insert a number (or 'done' to finish): ").lower() #Pido el numero y, si es la palabra done, la pongo en minúsculas.

print("You inserted: ", list) # Muestro la lista.