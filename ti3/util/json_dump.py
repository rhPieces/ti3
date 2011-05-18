from pymongo.connection import Connection
from pymongo.son_manipulator import AutoReference, NamespaceInjector
import json

con = Connection()
db = con.ti3
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

hexes = [hex for hex in db.hexes.find()]

outf = open('data/hexes.dat', 'w')

for x, hex in enumerate(hexes):
    hex['_id'] = x
    json.dump(hex, outf)
    outf.write('\n')
