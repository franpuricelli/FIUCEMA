# manejo de exepciones 

def eneavo(a):
    try:
        return 2/a 
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except TypeError:
        return "el numero es un string"

print(eneavo(0))
print(eneavo("9"))

