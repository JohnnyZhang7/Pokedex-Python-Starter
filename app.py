import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[0]) """

for poke in data:
    if poke['name']['english'] == 'Wooper':
        print(poke)
    if 'Ground' in poke['type']:
        print(poke['name']['english'])