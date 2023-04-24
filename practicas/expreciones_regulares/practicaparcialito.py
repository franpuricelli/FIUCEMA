#!/bin/python3

import re,os


archivo_origen = "gmails.txt"
archivo_destino = "gmails_nuevos.txt"
patron = r"([a-zA-Z0-9.*]+)@(yahoo|hotmail).com\b"
reemplazo = r"\1@gmail.com"

with open(archivo_origen, "r") as archivo:
    texto = archivo.read()

nuevo_contenido = re.sub(patron,reemplazo,texto)

with open(archivo_destino, "w") as reemplazo:
    reemplazo.write(nuevo_contenido)




