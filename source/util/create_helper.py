import os
from pymongo.connection import Connection
from pymongo.son_manipulator import AutoReference, NamespaceInjector

con = Connection()
db = con.ti3
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

sets = {
    'v' : 'Vanilla',
    'se': 'Shattered Empire',
    'sa': 'Shattered Ascension',
}

types = {
    'e': 'Empty',
    'p': 'Planet',
    'h': 'Homeworld',
    's': 'Special',
    'm': 'Mecatol Rex',
    'w': 'Wormwhole Nexus',
}

specialties = {
    'r': 'Red',
    'g': 'Green',
    'b': 'Blue',
    'y': 'Yellow',
    'g': 'Ground Force',
    's': 'Shock Troop',
    'f': 'Fighter',
    't': 'Trade Good',
}

entities = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'n': 'Nebula',
    'af': 'Asteroid Field',
    'i': 'Ion Storm',
    's': 'Supernova',
}

def add_hex():
    new_hex = {}
    new_hex['set'] = get_from_dict('Set', sets)
    new_hex['type'] = get_from_dict('Type', types)
    new_hex['entities'] = get_entities()
    #db.hexes.save(new_hex)
    print(new_hex)

def add_planet():
    planet = {}
    planet['name'] = raw_input('Planet Name: ')
    planet['res'] = raw_input('Resource Value: ')
    planet['inf'] = raw_input('Influence Value: ')
    planet['specialty'] = get_from_dict('Specialty', specialties)

    #db.planets.save(planet)
    return planet

def get_entities():
    to_add = []
    while raw_input('Add Entity? y/N ') == 'y':
        if (raw_input('Planet? y/N ') == 'y'):
            to_add.append(add_planet())
        else:
            to_add.append(get_from_dict('Entity', entities))

    return to_add

def get_from_dict(name, ops):
    os.system(['clear','cls'][os.name == 'nt'])
    for l in ['{0:>4} {1:<30}'.format(k, ops[k]) for k in ops]:
        print(l)
    val = raw_input(name + ': ')
    while val and val not in ops:
        val = raw_input(name + ': ')

    if val:
        return ops[val]
    return None

if __name__ == '__main__':
    while raw_input('Continue? ') == 'y':
        os.system(['clear','cls'][os.name == 'nt'])
        add_hex()
