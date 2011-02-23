"""
Functions and Classes dealing with hexes on the board
"""
from pymongo.connection import Connection
from pymongo.son_manipulator import AutoReference, NamespaceInjector

def load(**kwargs):
    con = Connection()
    db = con.ti3
    db.add_son_manipulator(NamespaceInjector())
    db.add_son_manipulator(AutoReference(db))

    return [Hex(hex) for hex in db.hexes.find(kwargs)]

class Hex:

    def __init__(self, hex):
        self.type = hex['type']
        self.set = hex['set']
        self.entities = hex['entities']

