import tkinter as tk
from tkinter import ttk

class Contenedor(tk.Frame):
    def __init__(self, interfaz):
        super().__init__(interfaz, width=1080, height=720, bg='Light Grey')
        self.pack()

        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
    
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        self.input_nombre = tk.StringVar()
        self.campo_nombre = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_nombre)
        self.campo_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.input_duracion = tk.StringVar()
        self.campo_duracion = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_duracion)
        self.campo_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.input_genero = tk.StringVar()
        self.campo_genero = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_genero)
        self.campo_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.boton_nuevo = tk.Button(self, text='Nuevo', bg='#158645', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#35BD6F', command=self.habilitar_campos)
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', bg='#1658A2', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#3586DF', command=self.guardar_datos)
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', bg='#BD152E', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#E15370', command=self.deshabilitar_campos)
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    def borrar_campos(self):
        self.input_nombre.set('')
        self.input_duracion.set('')
        self.input_genero.set('')

    def habilitar_campos(self):
        self.borrar_campos()
        self.campo_nombre.config(state='normal')
        self.campo_duracion.config(state='normal')
        self.campo_genero.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.borrar_campos()
        self.campo_nombre.config(state='disabled')
        self.campo_duracion.config(state='disabled')
        self.campo_genero.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        self.deshabilitar_campos()

    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=5, column=0, columnspan=4)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACIÓN')
        self.tabla.heading('#3',text='GENERO')
        
        self.tabla.insert('',0,text='1', values = ('Vengadores','2.35', 'Acción'))

        self.boton_editar = tk.Button(self, text='Editar', bg='#158645', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=6, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text='Eliminar', bg='#BD152E', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=6, column=2, padx=10, pady=10)


def barra_menu(interfaz):
    barra_menu = tk.Menu(interfaz)
    interfaz.config(menu = barra_menu)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label = 'Crear Registro')
    menu_inicio.add_command(label = 'Eliminar Registro')
    menu_inicio.add_command(label = 'Salir', command=interfaz.destroy)

    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=menu_configuracion)

    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)