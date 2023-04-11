#!/bin/python3

# Realizá un programa que lea un archivo e
# imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
import os, sys, glob


contador = 0
with open("C:/Users/simon/OneDrive/Escritorio/Informatica/FundamentosIUCEMA/practicas/manipulacion_de_archivos/texto.txt", "r") as archivo:
    texto = archivo.read().split()

with open(texto,"r") as file:
    for line in file:
        if not file.startswith(texto[0]):
          contador+=1
print(contador)




