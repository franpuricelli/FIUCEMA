#!/bin/python3

# Escribí un programa que lea un archivo e imprima las primeras n líneas.

import os
def leerimprimir(lineas):
    with open("texto.txt","r") as arch:
        for linea in range(lineas):
            lineas = arch.readline()
            print(lineas)
print(leerimprimir(5))



