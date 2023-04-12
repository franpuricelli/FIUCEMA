import re 

def entre_guiones(string):
    patron = "-(.*?)-"
    return re.findall(patron,string)

string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))



