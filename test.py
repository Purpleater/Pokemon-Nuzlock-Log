from common import *

gameInformation = loadGameStats('Pokemon Mystery Dungeon Explorers of Sky')

dungeonPokemonList = (getLocationByID_PMD("Pokemon Mystery Dungeon Explorers of Sky", 4))["dungeonPokemonList"]
for pokemon in dungeonPokemonList:
    print(getPokemonByID(pokemon))


print(getPokemonByID(900))