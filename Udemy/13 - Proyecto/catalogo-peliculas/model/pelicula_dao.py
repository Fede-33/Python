from .connect_db import ConexionDB
from .box import mensaje

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje(['i', 'Crear Base de datos', 'Base de Datos creada.'])    
    except:
        mensaje(['w', 'Crear Base de datos', 'La Base de Datos ya existe.'])    

def borrar_tabla():
    conexion = ConexionDB()
    
    sql = '''DROP TABLE peliculas'''

    try:
        if mensaje(['a', 'Borrar Base de datos', 'Se borrará la Base de datos.']):
            conexion.cursor.execute(sql)
            return True
        else:
            mensaje(['i', 'Borrar Base de datos', 'Operacion cancelada.'])
        conexion.cerrar()
    except:
        mensaje(['e', 'Borrar Base de datos', 'Base de Datos inexistente.'])    
        
def guardar(nombre, duracion, genero):
    conexion = ConexionDB()
    sql = f""" INSERT INTO 
            peliculas (nombre, duracion, genero)
            values('{nombre}', '{duracion}','{genero}' )
            """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje(['i', 'Agregar película', 'Película agregada con éxito.'])        
    except:
        mensaje(['e', 'Agregar película', 'Base de Datos inexistente.'])

def listar():
    conexion = ConexionDB()
    
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        mensaje(['e', 'Conexión a Base de Datos', 'Base de Datos inexistente.'])
    
    return lista_peliculas

def editar(id, nombre, duracion, genero):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas
            SET NOMBRE = '{nombre}', duracion = '{duracion}', genero = '{genero}'
            WHERE id_pelicula = {id}
            """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje(['e', 'Editar película', 'Base de Datos inexistente.'])

def eliminar(id):
    conexion = ConexionDB()
    sql = f'''DELETE FROM peliculas
            WHERE id_pelicula = {id}
            '''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje(['e', 'Editar película', 'Base de Datos inexistente.'])

