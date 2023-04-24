# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re

def verificar(string):
    return not bool(re.search(r"[^a-zA-Z0-9]", string))
    
print(verificar("abce"))
print(verificar("abc@e"))