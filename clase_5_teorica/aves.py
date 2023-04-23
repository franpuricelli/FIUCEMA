class AnimalAlado:
 
  def esta_feliz(self):
      return self.energia > 500
  
class AvesNoVoladoras:
  def __init__(self,energia):
    self.energia = energia

  def correr_en_circulos(self):
    self.energia -= 25

class Golondrina(AnimalAlado):
  def __init__(self, energia): #constructor, energia es atributo #self --> referencia a la instania en particular
    self.energia = energia 

  def esta_debil(self):
    return self.energia < 10

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self,vueltas): #diferencia entre metodo y funcion --> los metodos se encuentran dentro de una clase
    self.volar(vueltas)

#diferencia entre metodo y procedimiento --> metodo siempre dentro de una clase
#diferencia entre funcion y procedimiento --> procedimiento no retorna nada

  def volar(self, kms):
    self.energia -= 10 + kms
  
  def comer(self,cantidades):
    self.comer_alpiste(cantidades)
  
  def volar_sin_parar(self):
    self.energia -= 10 

  # def esta_feliz(self):
  #   return self.energia > 50
     
# para que un objeto sea polimorfico con otro, debe haber un 3er objeto que sea 



class Dragon(AnimalAlado):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def esta_debil(self):
    return self.energia < 50

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def comer(self,cantidades):
    self.comer_peces(cantidades)
  
  def volar_en_circulos(self,vueltas):
    self.energia -= vueltas

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def volar_sin_parar(self):
    self.energia -= 1




# Hace a hipo, entrenador de dragones: sabe aceptar a dragones y luego 
# hacerlos entrenar, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)

class EntrenadorDeDragones:
  def __init__(self,discipulos):
    self.discipulos = discipulos
  
  def entrenar_equipo(self,discipulos):
    for discipulo in discipulos:
      discipulo.volar_en_circulos(20)
      discipulo.comer(3)
  
# Definí el método entrenamiento_intensivo, que hace dar vueltas en circulos a sus entrenados hasta que estén débiles.
  def entrenamiento_intensivo(self,discipulos):
    for discipulo in discipulos:
      while discipulo.esta_debil() is False:
        discipulo.volar_sin_parar()
      
    

      
  

    
  

# def entrenamiento_intensivo(self,animal):
#   while animal.energia


# lista de objetos --> lista = [roberta,]
pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = EntrenadorDeDragones([])
