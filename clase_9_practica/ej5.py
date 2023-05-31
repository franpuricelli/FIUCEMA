import requests, json

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")

with open("ficha_tecnica_pokemon.txt","wb") as file:
    file.write(pikachu.content+ b"\n" + sylveon.content)

