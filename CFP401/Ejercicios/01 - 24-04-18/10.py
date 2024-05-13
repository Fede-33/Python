#Ingrese una contraseña, pregunte por la contraseña e indique si coinciden sin tener en cuenta mayúsculas o minúsculas:

contras = input("Ingrese una contraseña: ")
comparar = input("Ingrese la contraseña nuevamente: ")

contras = contras.lower() #transforma la variable en minúsculas
comparar = comparar.lower()

if contras == comparar :
    print("Constraseña correcta.")
else :
    print("Constraseña incorrecta.")

