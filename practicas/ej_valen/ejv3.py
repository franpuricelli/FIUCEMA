"""
Buscar en la siguiente secuencia, todos los patrone que comiencen por & y acaben por %$
Secuencia: “vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvke ms;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$”
"""
import re

def reem(string):
    patron = r"[&](.*?)[@$]"
    resultado = re.findall(patron,string)
    return resultado

string = "vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvke ms;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$"
print(reem(string))
