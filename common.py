import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

signalToMenuIndex = {
    0: "Home",
    1: "Member Roster",
    2: "Edit Game Save",
    3: "Credits"
}

gameStatsFileNameIndex = {
    "Pokemon Mystery Dungeon Red/Blue Rescue Team": "PMD-RT",
    "Pokemon Mystery Dungeon Explorers of Sky": "PMD-EoS"
}


def loadJson(fileString):
    with open(f"{fileString}.json", 'r') as file:
        data = json.load(file)
        return data


def loadGeneralPokemonData():
    with open('DataFolder/PokemonData.json', 'r') as file:
        pokemonData = json.load(file)["pokemonList"]
        return pokemonData


def loadGameStats(gameName):
    with open(f'DataFolder/GameStatistics/{gameStatsFileNameIndex[gameName]}.json', 'r') as file:
        gameInformation = json.load(file)
        return gameInformation


def getPokemonByID(id):
    pokemonList = loadGeneralPokemonData()
    result = next((pokemon for pokemon in pokemonList if pokemon["id"] == id), None)
    return result



def getLocationByID_PMD(gameName, locationID):
    dungeonList = loadGameStats(gameName)["dungeonList"]
    selectedDungeon = next((dungeon for dungeon in dungeonList if dungeon["dungeonID"] == locationID), None)
    return selectedDungeon
