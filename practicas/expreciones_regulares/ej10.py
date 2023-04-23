# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
import re

def subestrin(string):
    patron = "[@|&]+(.*?)[@|&]"
    return re.findall(patron,string)

print(subestrin("hola como estas @carlitos @@marquitos@ytyu&"))

