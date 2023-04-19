#!/usr/bin/env python3
#Escribir un script en el cual debemos movernos a la carpeta Informes y obtener los archivos *.txt que hayan allí. Por cada archivo hay que obtener, por un lado, cuántas veces aparece la palabra "estado" y por otro lado la cantidad de líneas. Por último, hay que crear una carpeta que se llame Apellidos, donde hay que crear un archivo llamado Lista.txt que contenga en cada línea la primer línea de cada archivo .txt obtenidos anteriormente.

import os, glob, sys

def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, "r") as file:
            file_completa = file.read()
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_estado.append(file_completa.count("\n"))

    os.mkdir("Apellido")
    with open("Apellido/Lista.txt", "w") as salida: #Le tengo que decir donde quiero que cree la lista
        for archivo in txt:
            with open(archivo,"r") as file:
                primera_linea = file.readline()
                salida.write(file.readline())
    return cantidad_estado, cantidad_lineas








# crear la carpeta Prácticas en el directorio actual:
#os.mkdir("Prácticas")

# crear la carpeta Teorías en el directorio superior:
#os.mkdir("../Teorías")

# movernos a la carpeta Prácticas:
#os.chdir("Prácticas")

# movernos desde Prácticas a Teorías
###os.chdir("../../../clase2")
#os.listdir()
#glob.glob(".txt")  #("*") signfica todo 
