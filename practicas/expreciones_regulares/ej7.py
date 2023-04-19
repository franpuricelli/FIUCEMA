# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

import re

def strinn(string):
    patron = "(?!\s)(\W)"
    if re.search(patron,string) is not None:
        return "Valores NO permitidos"
    else: return "Valores permitidos"

print(strinn("hola che como # va de10"))