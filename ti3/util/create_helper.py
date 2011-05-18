import os
from pprint import pprint
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

hex_types = {
    'e': 'Empty',
    'p': 'Planet',
    'h': 'Homeworld',
    's': 'Special',
    'm': 'Mecatol Rex',
    'w': 'Wormwhole Nexus',
}

entity_types = {
    'p': 'Planet',
    'w': 'Wormhole',
    'a': 'Anomaly',
    't': 'Trade Station',
}

specialties = {
    'r': 'Red',
    'g': 'Green',
    'b': 'Blue',
    'y': 'Yellow',
    'gf': 'Ground Force',
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
    new_hex['type'] = get_from_dict('Type', hex_types)
    if new_hex['type'] == 'Homeworld':
        new_hex['race'] = raw_input('Race: ')
    new_hex['entities'] = get_entities()

    pprint(new_hex)
    if raw_input('Save? y/N ') == 'y':
        db.hexes.save(new_hex)

def add_planet():
    planet = {}
    planet['name'] = raw_input('Planet Name: ')
    try:
        planet['res'] = int(raw_input('Resource Value: '))
        planet['inf'] = int(raw_input('Influence Value: '))
    except ValueError, e:
        print('Caught a bad number for resource or influence')
        planet['res'] = planet['inf'] = 0
    planet['specialty'] = get_from_dict('Specialty', specialties)

    pprint(planet)
    return planet

def get_entities():
    to_add = []
    while raw_input('Add Entity? Y/n ') != 'n':
        new_entity = {}
        new_entity['type'] = get_from_dict('Type', entity_types)
        if new_entity['type'] in ('Planet', 'Trade Station'):
            new_entity.update(add_planet())
        else:
            new_entity['name'] = get_from_dict('Entity', entities)
        to_add.append(new_entity)

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
    while raw_input('Continue? Y/n ') != 'n':
        os.system(['clear','cls'][os.name == 'nt'])
        add_hex()
