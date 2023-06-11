"""
Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la 
lista solo si el número es positivo. 
De lo contrario debería generar un error indicando que el número no es positivo.
"""

def positivos(a):
    lista_positivos = []
    for i in a:
        if i<0:
            raise Exception (f"{i} no es positivo")
        if i>=0:
            lista_positivos.append(i)

print(positivos([-1,2,1]))