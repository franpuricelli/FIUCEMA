# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada. --> preguntar

import re

lista = ["hola","amigo","mio","sanlorenzoo"]

def he(string):
    patron = "hola"
    if re.match(patron,string) is not None:
        return "Valor encontrado"
    else: return "no se encontro el patron"
print(he(lista))