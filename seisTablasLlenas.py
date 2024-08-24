from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Table, Spacer, PageBreak, Paragraph

from generadorTablasIguales import tablasIguales
from plantillaClases import Plantilla

# Agrega el Encabezado bingo transformando el array numpy a una simple lista luego lo transforma en una tabla
class tablasLlenas(Plantilla):
    def __init__(self, pdf_file, num, organizado_por, direccion, fecha, nota, costo):
        super().__init__(pdf_file, organizado_por, direccion, fecha, nota, costo)
        self.tabla_Llena = tablasIguales()
        self.creacion_tablas(num)

    def tabla_resultado(self, i):
        i.tabla_llena()
        return i.tablaLlena

    def creacion_tablas(self, num):
        self.aplicacion_estilos()
        self.creacion_pdf()

        for i in range(num):
            self.tabla_Llena.tabla_principal()
            tb1= self.tabla_resultado(self.tabla_Llena)
            tb2= self.tabla_resultado(self.tabla_Llena)
            tb3= self.tabla_resultado(self.tabla_Llena)
            tb4= self.tabla_resultado(self.tabla_Llena)
            tb5= self.tabla_resultado(self.tabla_Llena)
            tb6= self.tabla_resultado(self.tabla_Llena)
            long = len(self.direccion);a = 25; b = 100
            if long>=60 and self.direccion[60] != "\n":self.direccion=self.direccion[:60]+"\n\n"+self.direccion[60:]
            if long>60: a=50;b=125

            data_p = [[f"Organizado por: {self.organizado_por}"],
                    [f"Direccion: {self.direccion}"],
                    [f"Nota: {self.nota}"],
                    [f"Fecha: {self.fecha}"]]
            
            data_v = [[f"Valor:\n\n\n {self.costo}"]]
            
            #ajuste del tamaño y dimensiones de la tabla info
            data_p = Table(data_p, colWidths=[490],rowHeights=[25, a, 25, 25])
            data_v = Table(data_v, colWidths=[80], rowHeights=[b])

            #conversion de arrays a listas
            data1 = self.asignar_tabla(tb1)
            data2 = self.asignar_tabla(tb2)
            data3 = self.asignar_tabla(tb3)
            data4 = self.asignar_tabla(tb4)
            data5 = self.asignar_tabla(tb5)
            data6 = self.asignar_tabla(tb6)
            
            #asignacion de estilos a cada tabla
            data1.setStyle(self.estilo_cuerpo)
            data2.setStyle(self.estilo_cuerpo)
            data3.setStyle(self.estilo_cuerpo)
            data4.setStyle(self.estilo_cuerpo)
            data5.setStyle(self.estilo_cuerpo)
            data6.setStyle(self.estilo_cuerpo)
            data_p.setStyle(self.estilo_info)
            data_v.setStyle(self.estilo_costo_tabla)

            # Crear una tabla contenedora para alinear las tablas lado a lado con espaciado
            grupo_tablas = Table([[data1, Spacer(1, 0), data2], [data3, Spacer(1, 0), data4],[data5, Spacer(1, 0), data6]], colWidths=[300, 38, 210])
            grupo_datos = Table([[data_p, data_v]])
            # Crear el estilo del encabezado
            styles = getSampleStyleSheet()
            header_style = ParagraphStyle(name='CenteredHeader',
                                        parent=styles['Heading1'],
                                        alignment=1)  # 0=left, 1=center, 2=right

            # Crear el encabezado
            header = Paragraph("BINGO", header_style)
            # Crear el contenido del documento
            self.content.extend([header,Spacer(1,10), grupo_datos, Spacer(1,20),grupo_tablas, PageBreak()])

        # Crear el documento PDF
        self.document.build(self.content)


        print(f"El archivo {self.pdf_file} ha sido creado.")

tablasLlenas("jerson.pdf",7,"","","","","")