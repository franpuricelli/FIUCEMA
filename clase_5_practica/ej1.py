import re 

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]",string))  #si el string no tiene caracteres de A a la Z minuscula y mayuscula y del 0 al 9, retornara falso ya que el string no tiene caractere spermitidos
print(caracteres_permitidos("@"))

