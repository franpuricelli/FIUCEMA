#!/bin/python3

#ej 1

def revisar(lista):
    if "control" in lista:
        index = lista.index("control")
        lista.pop(index)
        lista.insert(index, "revisado")

#ej2

def eliminar_primer_elemento(lista):
    if len(lista) > 0:
        lista.pop(0)

#ej3

def encontrar_posicion(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return -1

#ej4

def mover_elemento_v1(lista_origen, lista_destino, elemento):
    if elemento in lista_origen:
        lista_origen.remove(elemento)
        lista_destino.append(elemento)

#ej5

def par_impar(lista):
    return [num % 2 == 0 for num in lista]

#ej6

def contar_caracteres(cadena):
    caracteres = {}
    for c in cadena:
        if c in caracteres:
            caracteres[c] += 1
        else:
            caracteres[c] = 1
    return caracteres

#ej7

def contar_caracteres(cadena):
    caracteres = {}
    for c in cadena:
        if c in caracteres:
            caracteres[c] += 1
        else:
            caracteres[c] = 1
    for c in range(ord('a'), ord('z')+1):
        if chr(c) not in caracteres:
            caracteres[chr(c)] = 0
    return caracteres

#ej8

def es_palindromo(palabra):
    return palabra == palabra[::-1]

#ej9

def productoria(lista):
    prod = 1
    for num in lista:
        prod *= num
    return prod

#ej10

socios = {
    1: {"nombre": "Florencia", "apellido": "Ocampo", "fecha_ingreso": "14092001", "cuota_al_dia": True},
    2: {"nombre": "David", "apellido": "Estévez", "fecha_ingreso": "14092001", "cuota_al_dia": True},
    3: {"nombre": "Sofía", "apellido": "Cáceres", "fecha_ingreso": "14092001", "cuota_al_dia": True}
}

def cargar_socio(numero, nombre, apellido, fecha_ingreso, cuota_al_dia):
    socios[numero] = {"nombre": nombre, "apellido": apellido, "fecha_ingreso": fecha_ingreso, "cuota_al_dia": cuota_al_dia}

def cantidad_socios():
    return len(socios)

def pagar_cuotas(numero_socio):
    if numero_socio in socios:
        socios[numero_socio]["cuota_al_dia"] = True
        print(f"Se han registrado como pagadas todas las cuotas del socio {numero_socio}")
    else:
        print("No se ha encontrado ningún socio con ese número")

def modificar_fecha(fecha_vieja, fecha_nueva):
    for numero_socio, datos_socio in socios.items():
        if datos_socio["fecha_ingreso"] == fecha_vieja:
            datos_socio["fecha_ingreso"] = fecha_nueva
    print("Se han modificado las fechas de ingreso correctamente")

def dar_baja(nombre, apellido):
    for numero_socio, datos_socio in socios.items():
        if datos_socio["nombre"] == nombre and datos_socio["apellido"] == apellido:
            del socios[numero_socio]
            print(f"El socio {numero_socio}, {nombre} {apellido}, ha sido dado de baja correctamente")
            return
    print("No se ha encontrado ningún socio con ese nombre y apellido")

def imprimir_socios():
    for numero_socio, datos_socio in socios.items():
        print(f"Socio número {numero_socio}: {datos_socio['nombre']} {datos_socio['apellido']}, ingresó el {datos_socio['fecha_ingreso']}, cuota al día: {datos_socio['cuota_al_dia']}")

cargar_socio(1, "Florencia", "Ocampo", "14092001", True)
cargar_socio(2, "David", "Estévez", "14092001", True)
cargar_socio(3, "Sofía", "Cáceres", "14092001", True)

print(f"El club tiene {cantidad_socios()} socios")
pagar_cuotas(2)
modificar_fecha("21102017", "22102017")
dar_baja("Sofía", "Cáceres")
imprimir_socios()


