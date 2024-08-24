import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pdf2image import convert_from_path
from tablasDeSeis import tablaDeSeis
from tablaDeCuatro import tablasDeCuatro
from seisTablasLlenas import tablasLlenas

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

    def creacion_plantillas(self):
        tablasDeCuatro("plantilla4.pdf", 1,"","","","","")
        tablaDeSeis("plantilla6.pdf", 1, "","","", "","")
        tablasLlenas("plantillaLlena.pdf", 1, "", "", "", "", "")

    def nueva_ventana(self):
        self.creacion_plantillas()
        # Destruir la ventana principal
        self.ventana.destroy()

        # Crear la nueva ventana
        self.ventana2 = tk.Tk()
        self.ventana2.title("Generador De Bingo")
        self.ancho = 850
        self.alto = 650
        

        self.opciones = ["tabla de 4", "tabla de 6", "tablas llenas"]
        self.reportes = [
            "plantilla4.pdf", 
            "plantilla6.pdf",
            "plantillaLlena.pdf"
        ]

        self.ancho_pantalla = self.ventana2.winfo_screenwidth()
        self.alto_pantalla = self.ventana2.winfo_screenheight()
        
    
        self.pos_x = (self.ancho_pantalla // 2) - (self.ancho // 2)
        self.pos_y = (self.alto_pantalla // 2) - (self.alto // 2)

        self.ventana2.geometry(f"{self.ancho}x{self.alto}+{self.pos_x}+{self.pos_y}")
        self.ventana2.resizable(False, False)
        self.ventana2.config(bg="red", bd=10, relief="raised")

        self.frame_interno = tk.Frame(self.ventana2, bg="white", width=840, height=640)
        self.frame_interno.pack(padx=10,pady=10)

        self.crear_interfaz_secundaria()
        self.ventana2.mainloop()

    def crear_interfaz_secundaria(self):
        def solo_numeros(text):
            if text.isdigit() or text == "":
                return True
            return False
        
        def solo_flotantes(text):
            if text == "":  # Permite borrar el contenido
                return True
            try:
                return float(text) >= 0  # Acepta solo si el número es flotante y no negativo
            except ValueError:
                return False
        # Crear etiquetas y campos de entrada
        self.crear_label("Organizado por (Opcional):", 50)
        self.crear_label("Dirección (Opcional):", 100)
        self.crear_label("Nota (Opcional):", 150)
        self.crear_label("Fecha (Opcional):", 200)
        self.crear_label("Valor (Opcional):", 250)
        self.crear_label("Tipo De Juego:", 300)
        self.crear_label("Cantidad De Tablas:", 350)
        self.crear_label("Nombre del Archivo\n(no debe incluir\nsimbolos):", 400)

        self.entrada1 = tk.Entry(self.frame_interno) # Organizado Por:
        self.entrada1.place(x=230, y=50)

        self.entrada2 = tk.Entry(self.frame_interno) #Direccion:
        self.entrada2.place(x=230, y=100)

        self.entrada3 = tk.Entry(self.frame_interno) #Nota:
        self.entrada3.place(x=230, y=150)

        self.entrada4 = tk.Entry(self.frame_interno) #Fecha:
        self.entrada4.place(x=230, y=200)

        validacion = self.ventana2.register(solo_flotantes)
        self.entrada5 = ttk.Spinbox(self.frame_interno, from_=1, to=9999, increment=1, validate="key",
                                     validatecommand=(validacion, "%P")) #Valor
        self.entrada5.place(x=230, y=250)

        self.entrada6 = tk.Spinbox(self.frame_interno, from_=1, to=9999, increment=1, validate="key",
                                     validatecommand=(validacion, "%P")) #Cantidad De Tablas
        self.entrada6.place(x=230, y=350)

        self.entrada7 = tk.Entry(self.frame_interno) #Nombre del archivo
        self.entrada7.place(x=230, y=400)

        self.opcion_seleccionada = tk.StringVar() 
        self.opcion_seleccionada.set(self.opciones[0])

        check1 = tk.OptionMenu(self.frame_interno, self.opcion_seleccionada, *self.opciones) #Tipo de Juego
        check1.place(x=230, y=300)

        boton_generar = tk.Button(self.frame_interno, text="Generar", command=self.generar_pdf) #Generar
        boton_generar.place(x=40, y=500)

        # Vincular el cambio de opción a la actualización de imagen
        self.opcion_seleccionada.trace('w', self.actualizar_imagen)

        # Inicializar la imagen del PDF
        self.label_bingo = tk.Label(self.frame_interno, text="Tabla De Bingo")
        self.label_bingo.place(x=560, y=50)

        self.label_imagen = tk.Label(self.frame_interno, relief="groove", bd=10, background="blue")
        self.label_imagen.place(x=450, y=75)

        # Mostrar la imagen inicial
        self.mostrar_imagen_inicial()

    def crear_label(self, texto, y):
        label = tk.Label(self.frame_interno, text=texto)
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
        try:
            if self.opcion_seleccionada.get() == self.opciones[0]:
                tablasDeCuatro(self.entrada7.get()+".pdf", int(self.entrada6.get()), 
                               self.entrada1.get(), self.entrada2.get(), self.entrada3.get(), 
                               self.entrada4.get(), self.entrada5.get())
                print("se a creado correctamente")
            elif self.opcion_seleccionada.get() == self.opciones[1]: 
                tablaDeSeis(self.entrada7.get()+".pdf", int(self.entrada6.get()), 
                               self.entrada1.get(), self.entrada2.get(), self.entrada3.get(), 
                               self.entrada4.get(), self.entrada5.get())
            elif self.opcion_seleccionada.get() == self.opciones[2]: 
                tablasLlenas(self.entrada7.get()+".pdf", int(self.entrada6.get()), 
                               self.entrada1.get(), self.entrada2.get(), self.entrada3.get(), 
                               self.entrada4.get(), self.entrada5.get())
            
            label7 = tk.Label(self.frame_interno, text="Se ha generado el pdf")
            label7.place(x=40, y=470)
        
        except Exception as e:
            print(f"Error: {e}")

# Ejecutar la aplicación
if __name__ == "__main__":
    GeneradorBingoApp()
