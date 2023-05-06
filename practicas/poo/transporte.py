"""
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, 
y de estos dos medios de transporte sabemos que:

comienzan con una cantidad que podemos establecer de combustible

los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de 
combustible por cada kilómetro recorrido

las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al 
máximo que pueden llevar.

Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.
"""

class MedioDeTransporte:
    
    def cargar_combustible(self,litros):
        self.combustible += litros

class Moto(MedioDeTransporte):
    
    def __init__(self,combustible, acompanantes):
        self.combustible = combustible
        self.acompanantes = self.personas(acompanantes)

    def recorrer(self,kms):
        self.combustible -= kms

    def personas(self,acompanantes):
        if acompanantes > self.maximo():
            raise Exception("La cantidad maxima de acompañantes son 5")
        else: self.acompanantes = acompanantes

    def maximo(self):
        return 2

class Auto(MedioDeTransporte):
    
    def __init__(self,combustible, acompanantes):
        self.combustible = combustible
        self.acompanantes = self.personas(acompanantes)

    def recorrer(self,kms):
        self.combustible -= kms/2

    def personas(self,acompanantes):
        if acompanantes > self.maximo():
            raise Exception("La cantidad maxima de acompañantes son 5")
        else: self.acompanantes = acompanantes

    def maximo(self):
        return 5
    
fitito = Auto(100,4)

fitito.recorrer(100)
print(fitito.combustible)