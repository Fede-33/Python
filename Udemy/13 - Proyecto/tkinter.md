# TKINTER

Librería nativa de Python que permite crear elementos visuales de GUI (Graphical User Interface). Para comenzar a utilizar esta librería debe importarse, preferentemente en nuestro módulo principal *main.py*, que es dónde se van a crear las interfaces y ventanas, mediante la sintaxis *import tkinter as tk*, agregando un alias para simplificar el código ulterior.

## CREAR INTERFAZ:
Se debe definir la interfaz como un objeto, asignándole inicialmente su nombre. Siendo la ventana principal del programa puede llamarse *root* y se le asigna la clase *Tk()* de la librería *tkinter*. Cada personalización que se quiera realizar a la ventana, deberá ser codificada mediante los métodos de la clase *Tk()*. La interfaz se ejecutará ininterrumpidamente, hasta que se de por finalizada su ejecución en la línea de código *root.mainloop()*. 

    root = tk.Tk()
    # Modificaciones y personalización
    root.mainloop()

## PERSONALIZACIÓN:

### TÍTUTLO:
Se especifica el nombre del objeto, el método *.title()* y el contenido del título:
    
    root.title('Catálogo de películas')

### ÍCONO:
Es conveniente tener la imagen integrada en un archivo .xmb, dentro de una carpeta en la misma ubicación de nuestro módulo principal. Se importará mediante el método *.iconbitmap()* especificando el path del archivo:

    root.iconbitmap('./img/cp-logo.ico')

Existen ciertos inconvenientes al trabajar con este método en Linux y Mac.

### TAMAÑO:
Mediante el método *.resizable()* se puede especificar la posibilidad de modificar la ventana horizontal o verticalmente:

    root.resizable(1,0) # permite modificar horizontalmente (ancho).
    root.resizable(0,1) # permite modificar verticalmente (alto).
    root.resizable(1,1) # permite modificar en ambas direcciones (por defecto). 
    root.resizable(0,0) # bloquea ambas direcciones.

### CONTENEDOR:
El contenedor, o widget, de una ventana se define mediante el método *.Frame()* especificando entre paréntesis el objeto que contiene la interfaz. Posteriormente, el contenedor debe empaquetarse mediante el método *.pack()*, este paso es el que lo hace visible:

    contenedor = tk.Frame(root)
    contenedor.pack()

#### CONFIGURACIÓN:
En el contenedor pueden configurarse diversos aspectos mediante el método *.config()*, especificando:

* **Amplitud y altura:** mediante los parámetros *width* y *height* y especificando el valor en pixeles.
* **Color:** especificándo el nombre del color o su código hexadecimal en el parámetro *bg*

    contenedor.config(width=1080, height=720, bg='grey')

#### MODULARIDAD:
Es una buena práctica definir el contenedor como un módulo, para poder importarlo y reutilizarlo. Se codifica en otro archivo con un nombre característico como *gui_app.py*, en el que se creará una clase hija de *tk.Frame*, que herede su constructor en el que se especificará el objeto que contiene la interfaz. También pueden especificarse los parámetros de configuración en el constructor, ya que al heredarse de la clase original, se reemplazan en la definición del Frame. Y finalmente el constructor debe tener la instrucción de empaquetarse. 

    class Contenedor(tk.Frame):
        def __init__(self, interfaz):
            super().__init__(interfaz, width=1080, height=720, bg='grey')
            self.pack()

En el programa principal, entonces crearemos un objeto con la clase *Contenedor* cuando se quiera definir reutilizar el widget, especificando únicamente la interfaz que quiere mostrarse:

    app = Contenedor(root)

### MENÚ:
El menú de una ventana suele definirse como una función, dentro de esta se incluye la barra como un objeto *tk.Menu()* especificando el objeto padre al que se aplicará. El espacio de la barra también tendrá opciones de personalización mediante el método *.config()*, pero lo más importante que se debe incluir es la asignación de el objeto creado anteriormente al parámetro *menu*:

    def barra_menu(interfaz):
        barra_menu = tk.Menu(interfaz)
        interfaz.config(menu = barra_menu)

        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
        menu_inicio.add_command(label = 'Crear Registro')
        menu_inicio.add_command(label = 'Eliminar Registro')
        menu_inicio.add_command(label = 'Salir', command=interfaz.destroy)

Una vez creada y configurada la barra del menú, corresponde crear cada uno de los botones de la barra. En el ejemplo anterior se define *menu_inicio* como un objeto de la clase *tk.Menu()*, especificando que va a etar contendido en *barra_menu* y el parámetro *tearoff=0* por motivos estéticos. Lo siguiente es asignarle un comportamiento de cascada mediante el método *.add_cascade()* especificando un nombre en el parámetro *label* y asignándole al parámetro *menu* el nombre del objeto en cuestión *menu_inicio*. Finalmente, se define cada una de las opciones que se desplegarán en la cascada, cada una con su etiqueta. Particularmente, tan solo la opción *Salir* tiene un comportamiento en este caso, asignada mediante el parámetro *command*, siendo la de terminar la ejecución de *interfaz* ejecutando el método *.destroy*

### LABELS:
Se refiere a las etiquetas que se encuentran dentro de la ventana, que identifican a los campos sobre los que el usuario puede interactuar. Se declaran como un método de la clase del contendor. Dentro de método, definiremos cada label como un objeto del tipo *tk.Label()* pudiendo especificar entre paréntesis las propiedades y comportamiento del mismo.

    class Contenedor(tk.Frame):
        def __init__(self, interfaz):
            super().__init__(interfaz, width=2160, height=1440, bg='grey')
            self.pack()

        def campos_pelicula(self):
            self.label_nombre = tk.Label(self, text='Nombre: ')

#### GRID:
El úso de guillas es útil para ubicar los distintos elementos dentro de la ventana del contenedor. El método *.grid()* será llamado junto al objeto que se quiera posicionar, y se especificará entre paréntesis la fila y columna correspondiente mediante los parámetros *row* y *column*, siempre teniendo en cuenta que sus valores serán enteros positivos, comenzando por 0. También puede especificarse un padding y demás personalizaciones:

    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ', font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ', font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ', font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

### ENTRIES:
Un entry es un campo que puede o no acompañar a un label. Este campo será el espacio en el que el usuario podrá ingresar datos o seleccionar opciones para interactuar con el sistema. Se definirán mediante el método *tk.Entry()* de una forma similar a los labels. En el siguiente ejemplo, en su grid se indica el parámetro *columnspan=2* que configura el campo para que ocupe dos columnas:

    self.campo_nombre = tk.Entry(self, width=65, state='disabled', font=('Arial', 12))
    self.campo_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    
    self.campo_duracion = tk.Entry(self, width=65, state='disabled', font=('Arial', 12))
    self.campo_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    
    self.campo_genero = tk.Entry(self, width=65, state='disabled', font=('Arial', 12))
    self.campo_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

El contenido del campo será un elemento variable que debe estar contenido en un objeto, para poder ser editado, borrado y recuperado. Para definir cada objeto puede utilizarse una clase *tk.StringVar* (Aunque también existen IntVar, FloatVar, BoolVar, y demás). Este objeto será definido previo a la creación del entry, y dentro de las propiedades del entry se definirá *textvariable* como el nombre del objeto StringVar. Quedando la sintaxis de esta manera:

    self.input_nombre = tk.StringVar()
    self.campo_nombre = tk.Entry(self, width=65, font=('Arial', 12), textvariable=self.input_nombre)
    self.campo_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

De esta forma, el contenido del campo será dinámico. Podrá ser reasignado o borrado mediante el método *.set()*, por ejemplo si se quisiera borrar su contenido:

    self.input_nombre.set('')

También puede ser extraido mediante el método *.get()*:

    sdfdfgsdfg

### BOTONES:
Los botones se definen similarmente a los labels y entries, pero con el método *tk.Button()*. Entre los parámetros de configuración, se puede considerar:
* **text:** contenido del texto.
* **bg:** color de fondo.
* **fg:** color de letra.
* **font:** fuente de letra.
* **cursor:** tipo de cursor cuando se pasa por encima.
* **activebackground:** color de fondo cuando se presiona.
* **command:** La función que tendrá ese botón.

Por ejemplo:

    self.boton_nuevo = tk.Button(self, text='Nuevo', bg='#158645', fg='#DAD5D6', width=30, font=('Arial', 12), cursor='hand2', activebackground='#35BD6F')
    self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

### HABILITAR O DESHABILITAR ELEMENTOS:
Se deberá definir un método dentro de la clase Constructor que defina la propiedad del objeto que se quiera habilitar o deshabilitar, mediante el método *.config* y la propiedad *state*, especificando 'disabled' o 'normal':

    def habilitar_campos(self):
        self.campo_nombre.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.campo_nombre.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

Este método podrá ser llamado cuando se ejecute el disparador de la acción, por ejemplo en el parámetro *command* de un botón.

### TABLAS:
Para la creación de una estructura jerarquizada como una tabla se recomienda utilizar el módulo *ttk* de *tkinter*, y particularmente la función *Treeview*. Requiere se especifiquen las columnas que se mostrarán, teniendo en cuenta que *Treeview* automáticamente creará una columna predeterminada inicial, y también que se defina la posición dentro del widget mediante *.grid*. Luego, mediante el método *.heading()* se especificará el título de cada una de las columnas. 

En el siguiente ejemplo, también se inserta en la tabla un elemento para mostrar, mediante el método *.insert()*. En este caso el primer argumento es una cadena vacía, si fuera un sub elemento debería ingresarse su elemento padre, el siguiente argumento es 0 para indicar que ocupa el primer lugar, luego *text='1'* mostrará el número 1 en la columna ID, predeterminada de *Treeview*, y los values serán los que se asignarán a las columnas definidas:

    from tkinter import ttk

    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=5, column=0, columnspan=4)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACIÓN')
        self.tabla.heading('#3',text='GENERO')
        
        self.tabla.insert('',0,text='1', values = ('Vengadores','2.35', 'Acción'))

### SCROLLBAR:
Para incluir una barra de navegación lateral puede utilizarse la clase *.Scrollbar* de la librería *ttk*, en el siguiente caso incluyendo una barra de navegación vertical, especificando el espesor, la orientación, y la ubicación.
        
    style.configure("Vertical.TScrollbar", width=30)
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=5, column=3, sticky='ns') 
    self.tabla.configure(yscrollcommand=self.scroll.set)

### MENSAJES:
Para mostrar una ventana emergente con un mensaje al usuario puede utilizarse el módulo *messagebox* de tkinter. El mismo puede mostrar tres tipos de mensajes, informativo(.showinfo), error (.showerror) y advertencia (.showwarning). Dentro de cada uno de esos modos, deben ingresarse los parámetros del título y el mensaje de la ventana.

En el siguiente ejemplo se define una función que recibe un tipo de ventana, un título y un mensaje, y evaluando el tipo de mensaje, muestra la ventana del modo correspondiente: 

    from tkinter import messagebox 

    def emergente(tipo, titulo, mensaje):
        if tipo == 'info':
            messagebox.showinfo(titulo, mensaje)
        elif tipo == 'error':
            messagebox.showerror(titulo, mensaje)
        elif tipo == 'warning':
            messagebox.showwarning(titulo, mensaje)