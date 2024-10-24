import sqlite3

def crear_bd() :
    conexion = sqlite3.connect ('restaurante.db') #Conecta con la BD
    cursor = conexion.cursor() #Crea un objeto (cursor) que sirve para ejecutar comandos SQL

    try:
        cursor.execute (''' CREATE TABLE categoria (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nombre VARCHAR(100) UNIQUE NOT NULL)''') #El cursor ejecuta el código SQL
    except sqlite3.OperationalError:
        print('La Tabla de Categorías ya existe.')
    else:
        print('La tabla de Categorías se ha creado correctamente.')
    
    try:
        cursor.execute ('''CREATE TABLE plato(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nombre VARCHAR(100) UNIQUE NOT NULL,
                         categoria_id INTEGER NOT NULL,
                         FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print ('La tabla de Platos ya existe.')
    else:
        print('La tabla de Platos se ha creado correctamente.')

def agregar_categoria ():
    categoria = input('Nombre de la nueva categoría:\n')
    conexion =sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria)) #Intenta agregar la categoría mediante SQL
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe.".format(categoria))
    else:
        print("Categoría '{}' creada correctamente".format(categoria))
    
    conexion.commit() #Guarda los cambios en SQL
    conexion.close() #Cierra la conexión (buena práctica)

def agregar_plato() :
    conexion =sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute ('SELECT * FROM categoria').fetchall() #Trae todas las categorías
    print('Selecciona una categoría para añadir el plato: ')
    for categoria in categorias:
        print('[{}] {}'.format(categoria[0], categoria[1])) #Muestra las categorías
    
    categoria_usuario = int(input('> '))

    plato = input('Nombre del nuevo plato:\n')

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', '{}')".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("Plato '{}' creado correctamente.".format(plato))
    
    conexion.commit()
    conexion.close()

def mostrar_menu ():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        print("\t{}".format(plato[1]))
    
    conexion.close()

# Crear la base de datos
crear_bd()

# Menu de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante.")
    opcion = input (
        "\nIntroduce una opción:" \
        "\n[1] Agregar categoría" \
        "\n[2] Agregar plato" \
        "\n[3] Mostrar menú" \
        "\n[4] Salir\n\n>")
    
    if opcion == '1':
        agregar_categoria()
    elif opcion == '2':
        agregar_plato()
    elif opcion == '3':
        mostrar_menu()
    elif opcion == '4':
        print ('Adios')
        break
    else:
        print('Opción incorrecta.')
