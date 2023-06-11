"""
Creá una carpeta llamada “CarpetaParcial” en la que existan 2 archivos .txt que contengan la siguiente información 
(los archivo .txt, también tenés que crearlos vos bro):

Contenido del archivo 1: 643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw iromvvwrwrvervwr43v4*3

Contenido del archivo2: 64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tv 
ew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3

Deberás extraer los números de teléfono de CABA (+54911########) y guardarlos en un archivo nuevo, en una carpeta llamada”
Telefonos”, creada dentro de la CarpetaParcial.

+5491142342353
"""
import os, re

def telefonos():
    os.mkdir("CarpetaParcial")
    os.chdir("CarpetaParcial")
    patron = r"\+54911\d{8}"
    with open("arch1.txt","a") as file:
        file.write("643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw iromvvwrwrvervwr43v4*3")
    with open("arch2.txt","a") as file:
        file.write("64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tvew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3")
    
    with open("arch1.txt","r") as file:
        contenido1 = file.read()
    with open("arch2.txt","r") as file:
        contenido2 = file.read()

    larch = re.findall(patron,contenido1)
    larch2 = re.findall(patron,contenido2)
    larch3 = larch + larch2
    print(larch3)

    with open("numeros.txt","a+") as file:
        for num in larch3:
            file.write(num + "\n")

if __name__ == "__main__":
    telefonos()
    



