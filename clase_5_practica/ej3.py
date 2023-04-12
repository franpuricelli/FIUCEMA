import re
#3
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else: "no se encontro el patron"


print (encontrar_patron("he"))
print (encontrar_patron("hheeeeeey"))
"""
print (encontrar_patron("a"))
print (encontrar_patron("he"))
print (encontrar_patron("heee"))
print (encontrar_patron("heeeeee"))

#2
def encontrar_patron2(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else: "no se encontro el patron"

print (encontrar_patron2("a"))
print (encontrar_patron2("he"))
print (encontrar_patron2("heee"))
print (encontrar_patron2("heeeeee"))

#1
def encontrar_patron1(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else: "no se encontro el patron"

print (encontrar_patron1("a"))
print (encontrar_patron1("he"))
print (encontrar_patron1("heee"))
print (encontrar_patron1("heeeeee"))
"""
#4
#1
def encontrar_patron4(string):
    patron = "he{2;4}"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else: "no se encontro el patron"

print (encontrar_patron4("a"))
print (encontrar_patron4("he"))
print (encontrar_patron4("heee"))
print (encontrar_patron4("heeeeee"))


