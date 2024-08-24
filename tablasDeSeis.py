from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, PageBreak, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from generadorTablasIguales import tablasIguales
from plantillaClases import Plantilla

class tablaDeSeis(Plantilla):
    def __init__(self, pdf_file, num, organizado_por, direccion, fecha, nota, costo):
        super().__init__(pdf_file, organizado_por, direccion, fecha, nota, costo)
        self.tablas6 = tablasIguales()
        self.creacion_tablas(num)

    def creacion_tablas(self,num):
        self.aplicacion_estilos()
        self.creacion_pdf()

        for i in range(num):
            self.tablas6.tabla_principal()
            self.tablas6.primera_tabla()
            self.tablas6.segunda_tabla()
            self.tablas6.tercera_tabla()
            self.tablas6.cuarta_tabla()
            self.tablas6.quinta_tabla()
            self.tablas6.tabla_llena()
            long = len(self.direccion);a = 25; b = 100
            if long>=60 and self.direccion[60] != "\n":self.direccion=self.direccion[:60]+"\n\n"+self.direccion[60:]
            if long>60: a=50

            data_p = [[f"Organizado por: {self.organizado_por}"],
                    [f"Direccion: {self.direccion}"],
                    [f"Nota: {self.nota}"],
                    [f"Fecha: {self.fecha}"]]
            
            data_v = [[f"Valor:\n\n\n {self.costo}"]]
            
            data_p = Table(data_p, colWidths=[490],rowHeights=[25, a, 25, 25])
            data_v = Table(data_v, colWidths=[80], rowHeights=[b])
            
            data1 = self.asignar_tabla(self.tablas6.tabla1)
            data2 = self.asignar_tabla(self.tablas6.tabla2)
            data3 = self.asignar_tabla(self.tablas6.tabla3)
            data4 = self.asignar_tabla(self.tablas6.tabla4)
            data5 = self.asignar_tabla(self.tablas6.tabla5)
            data6 = self.asignar_tabla(self.tablas6.tablaLlena)


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

if __name__ == "__main__":
    tb4=tablaDeSeis("parao.pdf", 5, "","","","","00.50")
    tb4.organizado_por = "jerson tacuri Orellana"
    tb4.direccion = "juan jose aviles morla, sector las trancas y si te invito una copa y me hacerco a tu boca"
    tb4.nota = "Llevar plata para la comida"
    tb4.fecha = "22 de noviembre del 2024"

