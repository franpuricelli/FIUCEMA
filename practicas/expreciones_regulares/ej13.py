# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re

def reem(string):
    patron = "[\W]{2,}"
    return re.sub(patron,"_",string)

print(reem("$$hola 2 $"))
