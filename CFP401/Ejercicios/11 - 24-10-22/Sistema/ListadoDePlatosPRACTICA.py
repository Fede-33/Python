##nuestros imports
import sqlite3
# son para crear graficos o ventanas
import tkinter as tk
from tkinter import messagebox, ttk

##Funcion para consultar la base de datos y buscar los platos con su respectiva categoria
def ver_platos():
    try:
        ruta = 'restaurante.db'
        conn = sqlite3.connect( ruta )
        cursor = conn.cursor()
        cursor.execute('''SELECT plato.nombre, categoria.nombre FROM plato, categoria
                            WHERE plato.categoria_id = categoria.id;''')#Hace un join de las dos tablas
        registros = cursor.fetchall()
        #print(registros) ## Este print solo sirve a modo debug o log, para ver si la consulta trae resultados.
        conn.close()
        ## Esta logica limpia el listado de resultados
        ## primero lo limpia y luego agrega los resultados
        for i in tree.get_children():
            tree.delete(i)
        for registro in registros:
            tree.insert("", tk.END, values=registro)

    except Exception as e:
        messagebox.showerror("Error", str(e))

##aca termina mi funcion e inicia el programa
app = tk.Tk()
app.title("Mi RESTO :-)")
#app.geometry("800x600") #en caso de querer darle tamano a la ventana

frame = tk.Frame(app)
frame.pack(pady=10)

##se agrega a la ventana un boto VER PLATOS
btn_ver_listado = tk.Button(frame, text="(+) Ver Platos", command=ver_platos)
btn_ver_listado.pack()

##Encabezado del listado, muestra dos columnas: Nombres y Categoria
tree = ttk.Treeview(app, columns=("Nombre", "Categoria"), show='headings')
tree.heading("Nombre", text="Nombre")
tree.heading("Categoria", text="Categoria")
tree.pack(pady=20)
tree.pack(fill=tk.BOTH, expand=True)

app.mainloop()
