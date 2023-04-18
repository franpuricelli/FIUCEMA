"""Creá un programa que verifique las siguientes condiciones:

A) si un string dado tiene una h seguida de ninguna o más e.
B) si un string dado tiene una h seguida de una o más e.
c) si un string dado tiene una h seguida de cero o una e.   
D) si un string dado tiene una h seguida de dos o tres e.
"""
import re

texto= "heee"

def he(t):
    patron = "he*"
    if re.search(patron,t) is not None:
        print("Se encontro el patron")
    else:
        print("no se encontro el patron")

def he2(t):
    patron = "he{2;3}"
    if re.search(patron,t) is not None:
        print("Se encontro el patron")
    else:
        print("no se encontro el patron")

print(he2(texto))

