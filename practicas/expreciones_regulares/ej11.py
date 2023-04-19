# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P
# y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def listita(string):
    patron = "(P\w*)\s(P\w*)"
    for elemento in string:
        if re.match(patron, elemento) is not None:
            print(elemento)
    
print(listita(lista))