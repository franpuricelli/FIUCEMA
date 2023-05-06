class MedioDeTransporte:
    
    def __init__(self,combustible):
        self.combustible = combustible

    def cargar_combustible(self,litros):
        self.combustible += litros

    def entran_personas(self,personas):
        return self.maximo() > personas

class Moto(MedioDeTransporte):

    def recorrer(self,kms):
        self.combustible -= kms

    def maximo(self):
        return 2

class Auto(MedioDeTransporte):

    def recorrer(self,kms):
        self.combustible -= kms/2

    def maximo(self):
        return 5
    
fitito = Auto(100)

fitito.recorrer(100)
print(fitito.combustible)