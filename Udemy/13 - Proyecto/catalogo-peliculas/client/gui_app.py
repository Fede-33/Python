import tkinter as tk
from tkinter import ttk
from model.box import mensaje
from model.pelicula_dao import crear_tabla, borrar_tabla, guardar, listar, editar, eliminar

class Contenedor(tk.Frame):
    def __init__(self, interfaz):
        super().__init__(interfaz, width=1080, height=720, bg='Light Grey')
        self.pack(fill='both', expand=True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)

        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
    
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky = 'ew')

        self.label_duracion = tk.Label(self, text='Duración: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10, sticky = 'ew')

        self.label_genero = tk.Label(self, text='Género: ', bg='Light Grey', font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10, sticky = 'ew')

        self.input_nombre = tk.StringVar()
        self.campo_nombre = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_nombre)
        self.campo_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky = 'ew')
        
        self.input_duracion = tk.StringVar()
        self.campo_duracion = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_duracion)
        self.campo_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky = 'ew')

        self.input_genero = tk.StringVar()
        self.campo_genero = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_genero)
        self.campo_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky = 'ew')

        self.boton_nuevo = tk.Button(self, text='Nuevo', bg='#158645', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#35BD6F', command=self.habilitar_campos)
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10, sticky = 'ew')

        self.boton_guardar = tk.Button(self, text='Guardar', bg='#1658A2', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#3586DF', command=self.guardar_datos)
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10, sticky = 'ew')

        self.boton_cancelar = tk.Button(self, text='Cancelar', bg='#BD152E', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#E15370', command=self.deshabilitar_campos)
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10, sticky = 'ew')

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
        self.id_pelicula = None

    def guardar_datos(self):

        if self.id_pelicula == None:
            guardar(self.input_nombre.get(), self.input_duracion.get(), self.input_genero.get())
        else:
            editar(self.id_pelicula, self.input_nombre.get(), self.input_duracion.get(), self.input_genero.get())

        self.deshabilitar_campos()
        self.tabla_peliculas()

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.durac_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.campo_nombre.insert(0, self.nombre_pelicula)
            self.campo_duracion.insert(0, self.durac_pelicula)           
            self.campo_genero.insert(0, self.genero_pelicula)            
        except:
            mensaje(['e','Editar película', 'Seleccione un registro.'])

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            
            confirma = mensaje(['a','Eliminar película', f'Se eliminará {self.nombre_pelicula}.'])

            if confirma:
                eliminar(self.id_pelicula)
                self.tabla_peliculas()
            else:
                mensaje(['i','Eliminar película', 'Operacion cancelada.'])
                self.id_pelicula = None
        except:
            mensaje(['e','Eliminar película', 'Seleccione un registro.'])

    def tabla_peliculas(self):

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        style.configure("Treeview", font=('Arial', 10), rowheight=30)
         
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género'), selectmode='browse')
        self.tabla.grid(row=5, column=0, columnspan=3, sticky='nsew', padx=10, pady=10) 

        self.tabla.column('#0', width=50, stretch=tk.NO, anchor='center') 
        self.tabla.column('Nombre', width=200, stretch=tk.YES, anchor='w')
        self.tabla.column('Duración', width=100, stretch=tk.YES, anchor='center')
        self.tabla.column('Género', width=150, stretch=tk.YES, anchor='w')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACIÓN')
        self.tabla.heading('#3',text='GENERO')
        
        style.configure("Vertical.TScrollbar", width=30)
        self.scroll_v = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll_v.grid(row=5, column=3, sticky='ns') 
        self.tabla.configure(yscrollcommand=self.scroll_v.set)

        style.configure("Horizontal.TScrollbar", height=30)
        self.scroll_x = ttk.Scrollbar(self, orient='horizontal', command=self.tabla.xview)
        self.scroll_x.grid(row=6, column=0, columnspan=3, sticky='ew') 
        self.tabla.configure(xscrollcommand=self.scroll_x.set)

        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        for pelicula in self.lista_peliculas:
            self.tabla.insert('',0,text=pelicula[0], values = (pelicula[1], pelicula[2], pelicula[3]))

        self.boton_editar = tk.Button(self, text='Editar', bg='#158645', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#35BD6F', command=self.editar_datos)
        self.boton_editar.grid(row=7, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text='Eliminar', bg='#BD152E', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#E15370', command=self.eliminar_datos)
        self.boton_eliminar.grid(row=7, column=2, padx=10, pady=10)

def barra_menu(interfaz):

    barra_menu = tk.Menu(interfaz)
    interfaz.config(menu = barra_menu)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label = 'Crear Base de Datos', command=crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Base de Datos', command=borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command=interfaz.destroy)

    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=menu_configuracion)

    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)