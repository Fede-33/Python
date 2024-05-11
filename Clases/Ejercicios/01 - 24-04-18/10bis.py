#Ingrese una contraseña, pregunte por la contraseña e indique si coincide sin tener en cuenta mayúsculas o minúsculas:

contras = input("Ingrese una contraseña: ").upper() #transforma el input en mayúsculas
comparar = input("Ingrese la contraseña nuevamente: ").upper()

if contras == comparar :
    print("Constraseña correcta.")
else :
    print("Constraseña incorrecta.")

