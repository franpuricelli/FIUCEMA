# Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

import re
texto= "lorem ipsum, lala, blalbla"
patron = "[a-zA-Z0-9]"
if re.search(patron, texto) is not None:
    print("Se encontro el patron")#codig
else:
    #codigo
    print("no se encontro el patron")


