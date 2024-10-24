import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title('Bar Mitz Vah - Menú')
root.resizable(0,0)
root.config(bd=25, relief='sunken')

Label(root, text='   Bar Mitz Vah   ', fg='darkgreen', font=('Times New Roman', 24, 'bold italic')).pack()
Label(root, text='Menú', fg='green', font=('Times New Roman', 18, 'bold italic')).pack()

# Separación de títulos y categorías
Label(root, text='').pack()

conexion = sqlite3.connect('restaurante.db')
cursor = conexion.cursor()

# Busca las categorías y platos de la bd
categorias = cursor.execute('SELECT * FROM categoria').fetchall()
for categoria in categorias:
    Label(root, text=categoria[1], fg='black', font=('Times New Roman', 14, 'bold italic')).pack()
    platos = cursor.execute('SELECT * FROM plato WHERE categoria_id={}'.format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg='gray', font=('Courier', 12, 'italic')).pack()

    # Separación entre categorías
    Label(root, text='').pack()

conexion.close()

# Precio del menú
Label(root, text='$12000 (IVA incl.)', fg='darkgreen', font=('Times New Roman', 18, 'bold italic')).pack(side='right')

#Finalmente ejecutamos el bucle
root.mainloop()