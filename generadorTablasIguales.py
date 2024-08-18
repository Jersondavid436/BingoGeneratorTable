from generadorDeTablas import Bingo
import copy

class tablasIguales(Bingo):
    def __init__(self):
        self.tabla1 = []
        self.tabla2 = []
        self.tabla3 = []
        self.tabla4 = []
        self.tabla5 = []
        self.tablaLlena = []
        self.tablaP = []

    def tabla_principal(self):
        self.tablaP = self.createTabla()
        self.tablaP[2, 2] = "Bingo"

    def primera_tabla(self):
        self.tabla1 = copy.deepcopy(self.tablaP)  # Crear una copia independiente
        self.tabla1[1, 1:4] = None
        self.tabla1[2, 4] = None
        self.tabla1[3, 1:4] = None

    def segunda_tabla(self):
        self.tabla2 = copy.deepcopy(self.tablaP)
        self.tabla2[1:4, 0:2] = None
        self.tabla2[1:4, 3:5] = None
        

    def tercera_tabla(self):
        self.tabla3 = copy.deepcopy(self.tablaP)
        self.tabla3[0, 1:4] = None
        self.tabla3[1, 2:4] = None
        self.tabla3[2, 1] = None
        self.tabla3[2, 3] = None
        self.tabla3[3, 1:3] = None
        self.tabla3[4, 1:4] = None

    def cuarta_tabla(self):
        self.tabla4 = copy.deepcopy(self.tablaP)
        self.tabla4[1, 1:5] = None
        self.tabla4[2, 1] = None
        self.tabla4[3, 1:4] = None

    def quinta_tabla(self):
        self.tabla5 = copy.deepcopy(self.tablaP)
        self.tabla5[1, 1:4] = None
        self.tabla5[2, 1:4] = None
        self.tabla5[2, 2] = "Bingo"
        self.tabla5[3, 1:4] = None

    def tabla_llena(self):
        self.tablaLlena = copy.deepcopy(self.tablaP)
