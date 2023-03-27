 #!/bin/python3

#armar un script que deba abrir un archivo txt y que cree otro (nuevo_archivo.txt) 
# con los 5 primeros caracteres del archivo que leyo

#otra manera
 
texto_leido=open("escritura_y_lectura.txt","r").read()

texto_p_escribir=texto_leido[0:6]

with open("nuevo_archivo.txt","a") as miarch:
    miarch.write(texto_p_escribir)
