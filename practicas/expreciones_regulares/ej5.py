# Escribí un programa que diga si un string empieza con un número específico.
import re

def strinn(string):
    patron = "^9"
    if re.search(patron,string) is not None:
        return "Valor encontrado"
    else: return "patron no encontrado"

print(strinn(" papa"))