#tarea: hacer un metodo para saber si las golondrinas y los dragones estan felices (golondrias si tienen mas de 50 d energia y 
#dragones si tienen mas de 500 d energia)
#cap 1,2 y 3 mumuki

from aves import pepita, anastasia, roberta, hipo,maria,chimuelo


print("energia de maria antes de entrenar: ",maria.energia)
print("energia de chimuelo antes de entrenar: ",chimuelo.energia)

# print(hipo.entrenar_equipo([chimuelo,maria]))
print(hipo.entrenamiento_intensivo([maria,chimuelo]))

print("energia de maria despus de entrenar: ",maria.energia)
print("energia de chimuelo despues de entrenar: ",chimuelo.energia)



"""
Ahora hacé las modificaciones en las clases Golondrina y Dragones para que un Entrenador pueda entrenar tanto a aves como dragones.
Creá una clase de AvesNoVoladoras, que come_alpiste y como su nombre indica no puede volar_en_circulos pero si correr_en_circulos disminuyendo su energía en 25.
¿Las AvesNoVoladoras son polimórficas con las aves Golondrinas desde el punto de vista del Entrenedor?¿Cómo podemos solucionar este inconveniente?

"""