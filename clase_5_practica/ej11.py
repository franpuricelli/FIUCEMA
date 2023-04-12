import re 
def dos_p(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\s(P\w*)",elemento)
        if resultado is not None:
            print(resultado.group())

lista =  ["Práctica Python", "Práctica C++", "Práctica Fortran"]
print(dos_p(lista))
