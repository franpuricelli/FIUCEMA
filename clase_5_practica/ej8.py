import re

def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)

string = "texyudueufweiwefiqfiefiwef 10 ajajsjdajsd, 3 saosaso 12"

extraer_numeros(string)