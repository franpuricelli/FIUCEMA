#!/bin/python3

"""
shiban, decirle a la computadora con que tiene que ejecutar el script

"""
import os,glob

def recoger():
    os.chdir("informes")
    txt =glob.glob("*.txt")
    cant_estado = []
    cant_lineas = []

    for arch in txt:
        with open(arch,"r") as file:
            file_completa = file.read()
            cant_estado.append(file_completa.count("estado"))
            cant_lineas.append(file_completa.count("\n"))
            #cant_lineas.append(file_completa.readlines())
    
    os.mkdir("apellido")
    with open("apellido/lista.txt","w") as salida:
        for arch in txt:
            with open(arch,"r") as file:
                #primer_linea = file.readline()
                salida.write(file.readline())
    return cant_estado,cant_lineas

if __name__=="__main__":
    print(recoger())


