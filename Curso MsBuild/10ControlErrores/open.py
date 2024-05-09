def func():
    try:
        open("text.txt")
    #except (FileNotFoundError, IsADirectoryError):
     #   print("El archivo text.txt no existe, o es inaccesible")
    except Exception as error:
        print("Error desconocido.", error)    
if True :
    func()
