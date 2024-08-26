from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
"""Con el fin de reducir la repeticion de codigo en algunos archivos de creo
una plantilla para heredar metodos similares que contenian los mismo archivos"""

class Plantilla():
    def __init__(self,pdf_file, organizado_por, direccion, fecha, nota, costo):
        self.pdf_file = pdf_file
        self.estilo_cuerpo = ""
        self.estilo_info = ""
        self.organizado_por = organizado_por
        self.direccion = direccion
        self.fecha = fecha
        self.nota = nota
        self.costo = costo
        self.content = []
        
    """ En esta seccion los arrays numpy se convierten en array simples para luego agregarles algunas caracteristicas
      como la palabra 'BINGO' como encabezado de cada tabla ademas del tamaño de cada celda de la tabla"""
    def asignar_tabla(self, arr):  
            nf = ["B", "I", "N", "G", "O"]
            data = arr.tolist()
            data.insert(0, nf)
            table = Table(data, colWidths=[40, 40, 40, 40, 40], rowHeights=[40, 30, 30, 30, 30, 30])  # Creación y asignación de tamaño de las tablas
            return table
    
    """ Este metodo creara el archivo pdf ademas del tamaño del mismo"""
    def creacion_pdf(self):        
        #crea el documento
        self.document = SimpleDocTemplate(self.pdf_file, pagesize=letter,  
                                    leftMargin=10, rightMargin=10,
                                    topMargin=0, bottomMargin=10) #Tamaño del margen del pdf
        
    """ Se asignan a las propiedades de la clase los estilos para cada seccion de la tabla de bingo como los
    juegos de las tablas y el encabezado"""
    def aplicacion_estilos(self):
        # Aplicar estilos a las tablas
        self.estilo_cuerpo = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
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

        self.estilo_costo_tabla = TableStyle([('ALIGN', (0, 0), (-1,-1), 'LEFT'),
                            ('FONTSIZE', (0,0), (-1,-1), 20),
                            ('VALIGN', (0,0), (-1,-1),'TOP'),
                            ('BOX', (0, 0), (-1, -1), 2, colors.black),  # Borde exterior grueso
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)
                            ])

        self.estilo_info = TableStyle([('ALIGN', (0, 0), (-1,-1), 'LEFT'),
                            ('FONTSIZE', (0,0), (-1,-1), 16),
                            ('VALIGN', (0,0), (-1,-1),'TOP'),
                            ('BOX', (0, 0), (-1, -1), 2, colors.black),  # Borde exterior grueso
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
