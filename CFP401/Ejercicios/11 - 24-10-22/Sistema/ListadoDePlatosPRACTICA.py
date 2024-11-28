##nuestros imports
import sqlite3
# son para crear graficos o ventanas
import tkinter as tk
from tkinter import messagebox, ttk

##Funcion para consultar la base de datos y buscar los platos con su respectiva categoria
def ver_platos():
    try:
        conn = sqlite3.connect( 'restaurante.db' )
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

def crear_categoria():
    formulario = tk.Toplevel()
    formulario.title('Nueva categoría')
    formulario.geometry('300x150')

    categoria_entry = tk.Entry(formulario)
    categoria_entry.pack(pady=5)

    def guardar_categoria():
        nueva_categoria = categoria_entry.get().strip()

        if not nueva_categoria:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una categoría.")
            return

        # Aquí va el código para guardar en la base de datos
        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO categoria VALUES (null, ?)", (nueva_categoria,))
            conn.commit()
            messagebox.showinfo("Éxito", "Categoría creada correctamente")
            formulario.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "La categoría ya existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
        finally:
            conn.close()

    boton_guardar = tk.Button(formulario, text='Guardar', command=guardar_categoria)
    boton_guardar.pack(pady=20)

##aca termina mi funcion e inicia el programa
app = tk.Tk()
app.title("Mi RESTO :-)")
#app.geometry("800x600") #en caso de querer darle tamano a la ventana

frame = tk.Frame(app)
frame.pack(pady=10)

##se agrega a la ventana un boto VER PLATOS
btn_ver_listado = tk.Button(frame, text="(+) Ver Platos", command=ver_platos)
btn_ver_listado.pack()

##se agrega a la ventana un boto CREAR CATEGORIA
btn_crear_categoria = tk.Button(frame, text="Crear Categoria", command=crear_categoria)
btn_crear_categoria.pack()


##Encabezado del listado, muestra dos columnas: Nombres y Categoria
tree = ttk.Treeview(app, columns=("Nombre", "Categoria"), show='headings')
tree.heading("Nombre", text="Nombre")
tree.heading("Categoria", text="Categoria")
tree.pack(pady=20)
tree.pack(fill=tk.BOTH, expand=True)

app.mainloop()
