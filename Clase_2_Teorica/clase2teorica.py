#!/bin/python3
import os,sys
#usuario=sys.argv[1]

#def saludador(nombre):
#    return "Hola "+nombre
#if __name__=="__main__":
#    print(saludador(usuario))

with open("mi_nombre.txt", "a") as miarch:
    miarch.write("Franco")
