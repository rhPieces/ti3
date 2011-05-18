"""
Functions and Classes dealing with hexes on the board
"""
import json

def load(**kwargs):
    hex_file = open('data/hexes.dat', 'r')

    hexes = []
    for line in hex_file:
        hexes.append(Hex(json.loads(line)))

    return hexes

class Hex:

    def __init__(self, hex):
        self._id = hex['_id']
        self.type = hex['type']
        self.set = hex['set']
        self.entities = hex['entities']
        self.planets = [entity for entity in self.entities if entity['type'] == 'Planet']
        self.ships = []

