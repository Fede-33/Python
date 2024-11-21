import sqlite3
from fpdf import FPDF  # type: ignore

# Conexión a la base de datos
conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

# Obtener datos de las categorías y platos
categorias = cursor.execute("SELECT * FROM categoria").fetchall()

# Crear el documento PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Iterar sobre las categorías y sus platos
for categoria in categorias:
    pdf.cell(200, 10, txt=categoria[1], ln=1, align='L')  # Imprimir el nombre de la categoría
    platos = cursor.execute("SELECT nombre FROM plato WHERE categoria_id={}".format (categoria[0])).fetchall()
    for plato in platos:
        pdf.cell(200, 10, txt="  - {}".format(plato[0]), ln=1, align='L')  # Imprimir los platos

# Guardar el PDF
pdf.output("menu.pdf")

# Cerrar la conexión a la base de datos
conn.close()