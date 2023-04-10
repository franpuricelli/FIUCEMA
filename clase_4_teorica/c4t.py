import re

#r"",texto --> expresiones regulares

#print(texto[22:26])
#findall devuelve siempre una lista


texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
p = "a[a-z]{3}"
"""
print(re.search(patron,texto),"re.search")
print(re.match(patron,texto),"match")
print(re.search(patron,texto).group())
print(re.findall(patron,texto),"findall")

patron2 = "ipsum(.*)sit"
print(re.search(patron2,texto))
print(re.search(patron2,texto), "\n")
print(re.search(patron2,texto).group())
print(re.search(patron2,texto).group(0),"0")
print(re.search(patron2,texto).group(1),"1")
"""
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
print(re.search(patron, texto).group())

print(re.search(patron, texto).group(0),"0") # es lo mismo q .group()
print(re.search(patron, texto).group(1),"1") # elimina las palabrasw de patron


