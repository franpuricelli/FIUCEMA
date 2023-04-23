class Biblioteca:
    def __init__(self):
        self.libros = []
  
    def agregar_libro(self,libro):
        self.libros.append(libro)
#Definí el método libros_largos dentro de la clase Biblioteca que, utilizando listas por comprensión, nos diga cuáles son sus libros largos.
    def libros_largos(self):
        return [libro for libro in self.libro if libro.es_largo()]
class Libro(Biblioteca):
    def __init__(self,un_titulo,unas_paginas,un_genero):
        self.titulo = un_titulo
        self.paginas = unas_paginas
        self.genero = un_genero
  
    def es_largo(self):
        return self.paginas > 300

libro_1 = Libro("La insoportable levedad del ser", 330, "Drama")
libro_2 = Libro("Contacto", 400, "Ciencia ficción")
libro_3 = Libro("Historias de cronopios y de famas", 180, "Ficción")

