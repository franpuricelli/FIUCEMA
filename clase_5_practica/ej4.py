import re

def palabras_unidas(string):
    patron = "^0[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Valor encontrado"
    else: return "patron no encontrado"








