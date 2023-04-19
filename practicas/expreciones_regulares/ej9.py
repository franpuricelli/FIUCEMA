# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

import re

def extraedor(string):
    patron = "-(.*?)-"
    return re.findall(patron,string) 

print(extraedor("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))