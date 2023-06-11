

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except TypeError:
    print("no puedo agregar arroz")