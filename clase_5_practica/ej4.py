import re

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Valor encontrado"
    else: return "patron no encontrado"


print(palabras_unidas("hola_puto"))





