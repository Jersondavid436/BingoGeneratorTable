from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

from generadorTablasIguales import tablasIguales

# Agrega el Encabezado bingo transformando el array numpy a una simple lista luego lo transforma en una tabla
def asignar_tabla(arr):  
        nf = ["B", "I", "N", "G", "O"]
        data = arr.tolist()
        data.insert(0, nf)
        table = Table(data, colWidths=[40, 40, 40, 40, 40], rowHeights=[40, 30, 30, 30, 30, 30])  # Creación y asignación de tamaño de las tablas
        return table

# Aplicar estilos a las tablas
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('VALIGN', (2, 3), (2, 3), 'MIDDLE'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 28),#Tamaño del encabezado de las tablas
                    ('FONTSIZE', (0, 1), (-1, -1), 20),#Tamaño de los numeros
                    ('FONTSIZE', (2, 3), (2, 3), 10),#Tamaño de los numeros
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

style2 = TableStyle([('ALIGN', (0, 0), (-1,-1), 'LEFT'),
                    ('FONTSIZE', (0,0), (-1,-1), 16),
                    ('VALIGN', (0,0), (-1,-1),'TOP'),
                    ('BOX', (0, 0), (-1, -1), 2, colors.black),  # Borde exterior grueso
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

tb6 = tablasIguales()

#crea el documento
pdf_file = "reporte_tablas_de_seis.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter,  
                            leftMargin=10, rightMargin=10,
                            topMargin=0, bottomMargin=10) #Tamaño del margen del pdf

content=[]

def creacion_tablas(num):
    for i in range(num):
        tb6.tabla_principal()
        tb6.primera_tabla()
        tb6.segunda_tabla()
        tb6.tercera_tabla()
        tb6.cuarta_tabla()
        tb6.quinta_tabla()
        tb6.tabla_llena()

        data_p = [["Organizado por:"],
                ["Direccion:"],
                ["Nota:"],
                ["Fecha:"]]
        
        data_p = Table(data_p, colWidths=[580],rowHeights=[25, 25, 25, 25])
        data1 = asignar_tabla(tb6.tabla1)
        data2 = asignar_tabla(tb6.tabla2)
        data3 = asignar_tabla(tb6.tabla3)
        data4 = asignar_tabla(tb6.tabla4)
        data5 = asignar_tabla(tb6.tabla5)
        data6 = asignar_tabla(tb6.tablaLlena)


        data1.setStyle(style)
        data2.setStyle(style)
        data3.setStyle(style)
        data4.setStyle(style)
        data5.setStyle(style)
        data6.setStyle(style)
        data_p.setStyle(style2)
        # Crear una tabla contenedora para alinear las tablas lado a lado con espaciado
        grupo_tablas = Table([[data1, Spacer(1, 0), data2], [data3, Spacer(1, 0), data4],[data5, Spacer(1, 0), data6]], colWidths=[300, 38, 210])

        # Crear el estilo del encabezado
        styles = getSampleStyleSheet()
        header_style = ParagraphStyle(name='CenteredHeader',
                                    parent=styles['Heading1'],
                                    alignment=1)  # 0=left, 1=center, 2=right

        # Crear el encabezado
        header = Paragraph("BINGO", header_style)
        # Crear el contenido del documento
        content.extend([header,Spacer(1,10), data_p, Spacer(1,20),grupo_tablas, PageBreak()])

    # Crear el documento PDF
    document.build(content)


    print(f"El archivo {pdf_file} ha sido creado.")

creacion_tablas(5)
