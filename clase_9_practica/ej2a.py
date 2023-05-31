import requests
import json

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
datos = respuesta.json()


status = respuesta.status_code
print(respuesta.headers)
content = respuesta.headers["Content-Type"]

print(datos["forms"])
print(content)

respuesta.json().keys() # rta de guille

lista_pokemones = []

pokemones = requests.get("https://pokeapi.co/api/v2/pokemon")
datos2 = pokemones.json()
print(datos2["count"]) #rta guille

resultados = datos2['results']

for pokemon in resultados:
    name = pokemon['name']
    lista_pokemones.append(name)
#print(lista_pokemones)
#print(len(lista_pokemones))
