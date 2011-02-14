from pymongo.connection import Connection
from pymongo.son_manipulator import AutoReference, NamespaceInjector

con = Connection()
db = con.ti3
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

def add_hex():
    new_hex = {}

    se = raw_input('Shattered Empire? ')
    if se == 'y':
        new_hex['shattered_empires'] = 1

    hw = raw_input('Home World? ')
    if hw == 'y':
        new_hex['home_world'] = 1

    wh = raw_input('Worm Holes: ').split(' ')
    if len(wh) > 0:
        new_hex['worm_holes'] = wh

    planets = add_planets()
    new_hex['planets'] = planets

    db.hexes.save(new_hex)

def add_planets():
    planets = []
    name = raw_input('Planet Name: ')
    while name != '':
        res = raw_input('Resource Value: ')
        inf = raw_input('Influence Value: ')
        specialty = raw_input('Specialy: ')
        planet = {
            'name': name,
            'influence': inf,
            'resources': res
        }
        if specialty != '':
            planet['specialty'] = specialty

        db.planets.save(planet)
        planets.append(planet)

        name = raw_input('Planet Name: ')

    return planets

if __name__ == '__main__':
    while raw_input('Continue? ') == 'y':
        add_hex()
