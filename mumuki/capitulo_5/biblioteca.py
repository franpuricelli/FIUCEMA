class Biblioteca:
    def __init__(self):
        self.libros = []
  
    def agregar_libro(self,libro):
        return self.libros.append(libro)

    def libros_largos(self):
  	    return [libro for libro in self.libros if libro.es_largo()]
""" 
    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]
"""
class Libro(Biblioteca):
    def __init__(self,titulo,paginas,genero):
        self.titulo = titulo
        self.paginas = paginas
        self.genero = genero
  
    def es_largo(self):
        return self.paginas > 300





libro_1 = Libro("La insoportable levedad del ser", 330, "Drama")
libro_2 = Libro("Contacto", 400, "Ciencia ficción")
libro_3 = Libro("Historias de cronopios y de famas", 180, "Ficción")


