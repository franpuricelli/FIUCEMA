# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios)
import re

def he(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Valor encontrado"
    else: return "patron no encontrado"

print(he("hol_aaaaputo"))
"""
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Valor encontrado"
    else: return "patron no encontrado"
"""
