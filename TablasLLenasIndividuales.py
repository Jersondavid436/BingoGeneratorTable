from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak

from generadorTablasIguales import tablasIguales

# Agrega el Encabezado bingo transformando el array numpy a una simple lista luego lo transforma en una tabla
def asignar_tabla(arr):  
    nf = ["B", "I", "N", "G", "O"]
    data = arr.tolist()
    data.insert(0, nf)
    table = Table(data, colWidths=[45, 45, 45, 45, 45], rowHeights=[45, 35, 35, 35, 35, 35])  # Creación y asignación de tamaño de las tablas
    return table

# Aplicar estilos a las tablas
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,0), 28), # Tamaño del encabezado de las tablas
                    ('FONTSIZE', (0,1), (-1,-1),18), # Tamaño de los números
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

style2 = TableStyle([('ALIGN', (0, 0), (-1,-1), 'LEFT'),
                    ('FONTSIZE', (0,0), (-1,-1), 12),
                    ('VALIGN', (0,0), (-1,-1),'TOP'),
                    ('BOX', (0, 0), (-1, -1), 2, colors.black),  # Borde exterior grueso
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

tb4 = tablasIguales()

# Crea el documento
pdf_file = "reporte_tablas_Llenas_individuales.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter,  
                            leftMargin=10, rightMargin=10,
                            topMargin=0, bottomMargin=10) # Tamaño del margen del pdf

content = []

def creacion_tablas(num):
    for i in range(num):
        tb4.tabla_principal()
        tb4.tabla_llena()

        # Crear la tabla superior con la información
        data_p = [["Organizado por:"],
                  ["Dirección:"],
                  ["Nota:"],
                  ["Fecha:"]]
        data_p = Table(data_p, colWidths=[240], rowHeights=[25, 25, 25, 25])

        # Crear la tabla con los datos principales (bingo)
        data4 = asignar_tabla(tb4.tablaLlena)
        data4.setStyle(style)
        data_p.setStyle(style2)

        # Organizar data_p arriba y data4 abajo en un contenedor vertical
        vertical_layout = Table([[data_p], [Spacer(1, 20)], [data4]])

        # Agregar la estructura al contenido
        content.extend([vertical_layout, Spacer(1, 20), PageBreak()])

    # Crear el documento PDF
    document.build(content)

    print(f"El archivo {pdf_file} ha sido creado.")

