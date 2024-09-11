from common import *

gameInformation = loadGameStats('Pokemon Mystery Dungeon Explorers of Sky')

dungeonPokemonList = (getLocationByID_PMD("Pokemon Mystery Dungeon Explorers of Sky", 4))["dungeonPokemonList"]
for pokemon in dungeonPokemonList:
    print(getPokemonByID(pokemon))

newArray = []
'''
for pokemonName in array:
    pokemonList = loadGeneralPokemonData()
    result = next((pokemon for pokemon in pokemonList if pokemon["name"] == pokemonName), None)
    newArray.append((result["id"]))
'''
