"""
Definir una función que tenga como parámetros una lista de números por un lado y un número por otro y 
devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso ([2,4,6,8], 2), 
debería retornar [1,2,3,4]. Tomar las precauciones necesarias.
"""

def division_numeros(a,b):
    try:
        lista = []
        for i in a:
            lista.append(i/2)    
        print(lista)
    except TypeError:
        return "en la lista hay elementos no numericos"

print(division_numeros([2,4,6,8], 2))