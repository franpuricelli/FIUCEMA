#Buscar en una cadena los siguiente caracteres “&*@” y reemplzarlos por “|”.
import re

def reemplazar(string):
    patron = r"[&@]"
    string = re.sub(patron, "|", string)
    return string

stri = "djf@jf@jsdjgjsgj&fg@g@&"
stri = reemplazar(stri)
print(stri)
