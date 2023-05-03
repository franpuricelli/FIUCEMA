#!/bin/python3

import os,glob,sys

def primeras_lineas():
    
    primer_linea = []
    camino = "datos/marzo"
    camino2 = "../../"

    os.chdir(camino)
    archs = glob.glob("*.txt")

    for arch in archs:
        with open(arch,"r") as file:
            primer_linea.append(file.readline())
    os.chdir(camino2)
    os.mkdir("resultados")
    os.chdir("resultados")
   
    with open("resultados","a") as file:
        for i in primer_linea:
            file.write(i)

if __name__ == "__main__":
    primeras_lineas()



