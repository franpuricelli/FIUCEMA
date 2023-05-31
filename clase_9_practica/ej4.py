import requests

pokemones = requests.get("https://pokeapi.co/api/v2/pokemon/abilities")
print(pokemones)


