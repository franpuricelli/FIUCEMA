# Escribí un programa que separe y devuelva los caracteres númericos de un string.

import re

def strinn(string):
    lista = []
    patron = "\d"
    return re.findall(patron,string)

print(strinn("papa 5 3 2 ogsjdpogspodjg 4 4sdjosjfo43"))