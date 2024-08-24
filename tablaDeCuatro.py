from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from generadorTablasIguales import tablasIguales
from plantillaClases import Plantilla

# Agrega el Encabezado bingo transformando el array numpy a una simple lista luego lo transforma en una tabla
class tablasDeCuatro(Plantilla):
    def __init__(self, pdf_file, num, organizado_por, direccion, fecha, nota, costo):
        super().__init__(pdf_file, organizado_por, direccion, fecha, nota, costo)
        self.tablas4 = tablasIguales()
        self.creacion_tablas(num)

    def asignar_tabla(self, arr):  
        nf = ["B", "I", "N", "G", "O"]
        data = arr.tolist()
        data.insert(0, nf)
        table = Table(data, colWidths=[50, 50, 50, 50, 50], rowHeights=[50, 40, 40, 40, 40, 40])  # Creación y asignación de tamaño de las tablas
        return table
    
    def aplicar_estilos(self):
        # Aplicar estilos a las tablas
        self.estilo_cuerpo = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('VALIGN', (2, 3), (2, 3), 'MIDDLE'), # alineacion del centro
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0,0), (-1,0), 32),#Tamaño del encabezado de las tablas
                            ('FONTSIZE', (0,1), (-1,-1),22),#Tamaño de los numeros
                            ('FONTSIZE', (2, 3), (2, 3), 12),#Tamaño del Centro de la Tabla
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
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

    def creacion_tablas(self,num):
        self.aplicar_estilos()
        self.creacion_pdf()

        for i in range(num):
            self.tablas4.tabla_principal()
            self.tablas4.primera_tabla()
            self.tablas4.segunda_tabla()
            self.tablas4.tercera_tabla()
            self.tablas4.tabla_llena()
            long = len(self.direccion);a = 25; b = 100
            if long>=60 and self.direccion[60] != "\n":self.direccion=self.direccion[:60]+"\n\n"+self.direccion[60:]
            if long>60: a=50;b=125

            data_p = [[f"Organizado por: {self.organizado_por}"],
                    [f"Direccion: {self.direccion}"],
                    [f"Nota: {self.nota}"],
                    [f"Fecha: {self.fecha}"]]
            
            data_v = [[f"Valor:\n\n\n {self.costo}"]]

            data_p = Table(data_p, colWidths=[490],rowHeights=[25, a, 25, 25])
            data_v = Table(data_v, colWidths=[80], rowHeights=[b])

            data1 = self.asignar_tabla(self.tablas4.tabla1)
            data2 = self.asignar_tabla(self.tablas4.tabla2)
            data3 = self.asignar_tabla(self.tablas4.tabla3)
            data4 = self.asignar_tabla(self.tablas4.tablaLlena)

            data1.setStyle(self.estilo_cuerpo)
            data2.setStyle(self.estilo_cuerpo)
            data3.setStyle(self.estilo_cuerpo)
            data4.setStyle(self.estilo_cuerpo)
            data_p.setStyle(self.estilo_info)
            data_v.setStyle(self.estilo_costo_tabla)

            # Crear una tabla contenedora para alinear las tablas lado a lado con espaciado
            grupo_tablas = Table([[data1, Spacer(1, 0), data2], [data3, Spacer(1, 0), data4]], colWidths=[300, 38, 262])
            grupo_datos = Table([[data_p, data_v]])

            # Crear el estilo del encabezado
            styles = getSampleStyleSheet()
            header_style = ParagraphStyle(name='CenteredHeader',
                                        parent=styles['Heading1'],
                                        alignment=1)  # 0=left, 1=center, 2=right

            # Crear el encabezado
            header = Paragraph("Gran Bingo", header_style)
            # Crear el contenido del documento
            self.content.extend([header,Spacer(1,10), grupo_datos, Spacer(1,20),grupo_tablas, PageBreak()])

        # Crear el documento PDF
        self.document.build(self.content)
        
        print(f"El archivo {self.pdf_file} ha sido creado.")

tablasDeCuatro("parao.pdf", 5, "","","","","00.50")