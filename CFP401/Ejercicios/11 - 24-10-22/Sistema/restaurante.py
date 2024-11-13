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

def eliminar_plato ():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    platos = cursor.execute ('SELECT id, nombre FROM plato ORDER BY id ASC ;').fetchall() #Trae todos los platos
    print('Selecciona el plato a eliminar: ')
    for plato in platos:
        print('[{}] {}'.format(plato[0], plato[1])) #Muestra los platos
    
    plato_eliminar = int(input('> '))

    try:
        cursor.execute("DELETE FROM plato WHERE id = '{}'".format(plato_eliminar)) #intenta eliminar el plato
    except sqlite3.IntegrityError:
        print("El plato seleccionado no existe.")
    else:
        print("Plato eliminado correctamente")
    
    conexion.commit()
    conexion.close()

def eliminar_categoria ():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute ('SELECT id, nombre FROM categoria ORDER BY id ASC ;').fetchall() #Trae todas las categorias
    print('Selecciona la categoría a eliminar: ')
    for categoria in categorias:
        print('[{}] {}'.format(categoria[0], categoria[1])) #Muestra las categorías
    
    categoria_eliminar = int(input('> '))
    cont = False
    
    for numero, plato in categorias :
        if categoria_eliminar == numero:
            cont = True
    
    if cont == True :

        contiene = cursor.execute("SELECT nombre FROM plato WHERE categoria_id = '{}'".format(categoria_eliminar)).fetchall()
        confirma = 'N'
        
        if contiene:
            print('La categoría seleccionada contiene los siguientes platos:')
            for i in contiene:
                print(i)
            print('Si elimina la categoría, se perderán los platos anteriores. ')
            
            while confirma != 'S':
                try:
                    confirma = input('¿Eliminar de todas formas? (S/N) ').upper()
                    if confirma != 'S' and confirma != 'N':
                        raise Exception
                    elif confirma == 'N':
                        break    
                except :
                    print('Opción incorrecta.')
            
        if confirma == 'S':
            try:
                cursor.execute("DELETE FROM categoria WHERE id = '{}'".format(categoria_eliminar)) #intenta eliminar el plato
            except sqlite3.IntegrityError:
                print("La categoría seleccionada no existe.")
            else:
                print("Categoría eliminada correctamente")
    
    else:
        print('La categoria no existe')
    
    conexion.commit()
    conexion.close()

def modificar_plato ():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    platos = cursor.execute ('SELECT id, nombre FROM plato ORDER BY id ASC ;').fetchall() #Trae todos los platos
    print('Selecciona el plato a modificar: ')
    for plato in platos:
        print('[{}] {}'.format(plato[0], plato[1])) #Muestra los platos
    
    plato_modificar = int(input('> '))
    nuevo_nombre = input("Ingrese nuevo nombre: ")

    try:
        cursor.execute("UPDATE plato SET nombre = '{}' WHERE id = '{}'".format(nuevo_nombre, plato_modificar)) #intenta modificar el plato
    except sqlite3.IntegrityError:
        print("El plato seleccionado no existe.")
    else:
        print("\nPlato '{}' modificado correctamente".format(nuevo_nombre))
    
    conexion.commit() #Guarda los cambios en SQL
    conexion.close() #Cierra la conexión (buena práctica)    

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
        "\n[4] Eliminar plato"\
        "\n[5] Modificar plato"\
        "\n[6] Eliminar categoría"\
        "\n[7] Salir\n\n>")
    
    if opcion == '1':
        agregar_categoria()
    elif opcion == '2':
        agregar_plato()
    elif opcion == '3':
        mostrar_menu()
    elif opcion == '4':
        eliminar_plato()
    elif opcion == '5':
        modificar_plato()
    elif opcion == '6':
        eliminar_categoria()
    elif opcion == '7':
        print ('Adios')
        break
    else:
        print('Opción incorrecta.')
