import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pdf2image import convert_from_path
from tablasDeSeis import tablaDeSeis

class GeneradorBingoApp:
    def __init__(self):
        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Generador De Bingo")
        self.ancho = 800
        self.alto = 500

        self.ancho_pantalla = self.ventana.winfo_screenwidth()
        self.alto_pantalla = self.ventana.winfo_screenheight()

        self.pos_x = (self.ancho_pantalla // 2) - (self.ancho // 2)
        self.pos_y = (self.alto_pantalla // 2) - (self.alto // 2)

        self.ventana.geometry(f"{self.ancho}x{self.alto}+{self.pos_x}+{self.pos_y}")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="red")

        self.crear_interfaz_principal()

    def crear_interfaz_principal(self):
        label_bienvenida = tk.Label(
            self.ventana, 
            text="Bienvenido Al Generador\n de Tablas De Bingo",
            background="Blue",
            borderwidth=10, 
            relief="groove"
        )
        label_bienvenida.grid(column=0, row=0, padx=250, pady=100)
        label_bienvenida.config(font=("Arial", 20, "bold"), foreground="white")

        boton_inicio = tk.Button(self.ventana, text="Empezar", command=self.nueva_ventana)
        boton_inicio.grid(column=0, row=1)

        self.ventana.mainloop()

    def nueva_ventana(self):
        # Destruir la ventana principal
        self.ventana.destroy()

        # Crear la nueva ventana
        self.ventana2 = tk.Tk()
        self.ancho = 800
        self.alto = 600

        self.opciones = ["tabla de 4", "tabla de 6", "tablas llenas"]
        self.reportes = [
            "reporte_tablas_de_cuatro.pdf", 
            "reporte_tablas_de_seis.pdf",
            "reporte_tablas_de_seis_llenas.pdf"
        ]

        self.ancho_pantalla = self.ventana2.winfo_screenwidth()
        self.alto_pantalla = self.ventana2.winfo_screenheight()

        self.pos_x = (self.ancho_pantalla // 2) - (self.ancho // 2)
        self.pos_y = (self.alto_pantalla // 2) - (self.alto // 2)

        self.ventana2.geometry(f"{self.ancho}x{self.alto}+{self.pos_x}+{self.pos_y}")
        self.ventana2.resizable(False, False)
        self.ventana2.config(bg="blue")

        self.crear_interfaz_secundaria()
        self.ventana2.mainloop()

    def crear_interfaz_secundaria(self):
        # Crear etiquetas y campos de entrada
        self.crear_label("Organizado por (Opcional):", 50)
        self.crear_label("Dirección (Opcional):", 100)
        self.crear_label("Nota (Opcional):", 150)
        self.crear_label("Fecha (Opcional):", 200)
        self.crear_label("Cantidad de tablas:", 300)

        entrada1 = tk.Entry(self.ventana2)
        entrada1.place(x=230, y=50)

        entrada2 = tk.Entry(self.ventana2)
        entrada2.place(x=230, y=100)

        entrada3 = tk.Entry(self.ventana2)
        entrada3.place(x=230, y=150)

        entrada4 = tk.Entry(self.ventana2)
        entrada4.place(x=230, y=200)

        self.entrada5 = tk.Entry(self.ventana2)
        self.entrada5.place(x=230, y=300)

        # Tipo de Juego (OptionMenu)
        label_tipo_juego = tk.Label(self.ventana2, text="Tipo de Juego:")
        label_tipo_juego.place(x=40, y=250)

        self.opcion_seleccionada = tk.StringVar()
        self.opcion_seleccionada.set(self.opciones[0])

        check1 = tk.OptionMenu(self.ventana2, self.opcion_seleccionada, *self.opciones)
        check1.place(x=230, y=250)

        boton_generar = tk.Button(self.ventana2, text="Generar", command=self.generar_pdf)
        boton_generar.place(x=40, y=350)

        # Vincular el cambio de opción a la actualización de imagen
        self.opcion_seleccionada.trace('w', self.actualizar_imagen)

        # Inicializar la imagen del PDF
        self.label_bingo = tk.Label(self.ventana2, text="Tabla Bingo")
        self.label_bingo.place(x=450, y=50)

        self.label_imagen = tk.Label(self.ventana2)
        self.label_imagen.place(x=450, y=70)

        # Mostrar la imagen inicial
        self.mostrar_imagen_inicial()

    def crear_label(self, texto, y):
        label = tk.Label(self.ventana2, text=texto)
        label.place(x=40, y=y)

    def mostrar_imagen_inicial(self):
        self.actualizar_imagen()

    def actualizar_imagen(self, *args):
        # Obtener el índice de la opción seleccionada
        reporte_seleccionado = self.opciones.index(self.opcion_seleccionada.get())
        # Convertir el PDF a imágenes
        imagenes = convert_from_path(self.reportes[reporte_seleccionado])
        # Seleccionar la primera página del PDF
        imagen = imagenes[0]
        # Redimensionar la imagen
        imagen_renderizada = imagen.resize((300, 400), Image.Resampling.LANCZOS)
        # Convertir la imagen para usarla en tkinter
        imagen_tk = ImageTk.PhotoImage(imagen_renderizada)
        # Actualizar el label con la nueva imagen
        self.label_imagen.config(image=imagen_tk)
        self.label_imagen.image = imagen_tk  # Guardar la referencia para evitar que Python elimine la imagen

    def generar_pdf(self):
        num = int(self.entrada5.get())
        tablaDeSeis("prueba.pdf", num)
        label7 = tk.Label(self.ventana2, text="Se ha generado el pdf")
        label7.place(x=40, y=450)
        pass

# Ejecutar la aplicación
if __name__ == "__main__":
    GeneradorBingoApp()
