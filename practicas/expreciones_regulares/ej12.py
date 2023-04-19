# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|)
import re

def reemplazador(string):
    patron = "[\s_:]"
    return re.sub(patron,"|",string)
print(reemplazador("hola_si estas leyendo est___o,: espero no te vuelvas loc@"))