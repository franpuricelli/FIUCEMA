
class Estudiante:
    def __init__(self,energia):
        self.energia = energia
        self.animo = "no feliz"

    def dormir(self,horas):
        self.energia += 12.5 * horas

    def comer(self):
        self.energia += 10

    def ejercicio(self,minutos):
        self.energia -= minutos * 0.8333

    def estudiar(self,horas):
        self.energia -= 20 * horas

    def aprobar(self):
        self.animo = "feelizz"
        return self.animo

estudiante = Estudiante(100)
estudiante.ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia)