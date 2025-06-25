import tkinter as tk
from client.gui_app import Contenedor, barra_menu

def main ():
    root = tk.Tk()
    root.title('Catálogo de películas')

    try:
        root.iconbitmap('img/logo.ico')
    except Exception as error:
        print(f'Error: {type(error).__name__}')
    root.resizable(1,1)

    app = Contenedor(root)
    barra_menu(root)
      
    app.mainloop()


if __name__ == '__main__':
    main()