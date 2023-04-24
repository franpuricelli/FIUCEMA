# !/bin/python3

#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
import os

def leerimprimir(n):
    with open('texto.txt', 'r') as archivo:
        lineas = archivo.readlines()
        ultimas_lineas = lineas[-n:]
        for linea in ultimas_lineas:
            print(linea)


if __name__ == "__main__":
    leerimprimir(2)

