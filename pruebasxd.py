import tkinter as tk
from PIL import Image, ImageTk
from pdf2image import convert_from_path

def cambiar_pdf():
    # Convertir el PDF a imágenes
    imagenes = convert_from_path("reporte_tablas_de_cuatro.pdf")
    
    # Seleccionar la primera página
    imagen = imagenes[0]
    
    # Redimensionar la imagen
    imagen_renderizada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    
    # Convertir la imagen para usarla en tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_renderizada)
    
    # Actualizar la imagen en el label
    label.config(image=imagen_tk)
    
    # Mantener una referencia a la imagen para evitar que se elimine por el recolector de basura
    label.image = imagen_tk

# Convertir el PDF inicial a imágenes
imagenes = convert_from_path("reporte_tablas_de_seis.pdf")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visualizar PDF")

# Seleccionar la primera página del PDF
imagen = imagenes[0]

# Definir el tamaño de la imagen
ancho = 300
alto = 400

# Redimensionar la imagen
imagen_renderizada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

# Convertir la imagen para usarla en tkinter
imagen_tk = ImageTk.PhotoImage(imagen_renderizada)

# Crear un label para mostrar la imagen
label = tk.Label(ventana, image=imagen_tk)
label.pack()

# Crear un botón que cambia la imagen al presionarlo
boton = tk.Button(ventana, text="Empezar", command=cambiar_pdf)
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
