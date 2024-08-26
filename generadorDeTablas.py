from datetime import datetime as dt
import numpy as np
""" Creacion del generador de Bingo
este archivo contiene la generacion de un array numpy de 2 dimenciones con el reducir la velocidad de creacion
de los numeros de las tablas
"""

class Bingo():
    def __init__(self):
        self.listanB =[]
        self.listanI =[]
        self.listanN =[]
        self.listanG =[]
        self.listanO =[]

    def createTabla(self):
        # Generación de números aleatorios para cada columna sin repetición
        columnaB = np.random.choice(np.arange(1, 16), 5, replace=False)
        columnaI = np.random.choice(np.arange(17, 31), 5, replace=False)
        columnaN = np.random.choice(np.arange(32, 46), 5, replace=False)
        columnaG = np.random.choice(np.arange(47, 61), 5, replace=False)
        columnaO = np.random.choice(np.arange(62, 76), 5, replace=False)
        
        # Crear una matriz con las columnas
        return np.array([columnaB, columnaI, columnaN, columnaG, columnaO]).T.astype(object)  # Convertir a object para permitir None
