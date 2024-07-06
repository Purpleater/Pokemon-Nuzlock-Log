import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

signalToMenuIndex = {
    0: "Home",
    1: "Member Roster",
    2: "Edit Game Save",
    3: "Credits"
}


def loadPokemonData():
    with open('DataFolder/PokemonData.json', 'r') as file:
        pokemonData = json.load(file)["pokemonList"]
        return pokemonData

