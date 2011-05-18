from __future__ import print_function
import source.model.board as bm
import source.model.hex as hm

hexes = hm.load()
mc = hexes[21]

b = bm.Board(11, 11)
b.set_hex(mc, *b.center)

b.set_hex(hexes[0], *b.adjacent_coords(*b.center)['n'])
b.set_hex(hexes[1], *b.adjacent_coords(*b.center)['ne'])
b.set_hex(hexes[2], *b.adjacent_coords(*b.center)['se'])
b.set_hex(hexes[3], *b.adjacent_coords(*b.center)['s'])
b.set_hex(hexes[4], *b.adjacent_coords(*b.center)['sw'])
b.set_hex(hexes[5], *b.adjacent_coords(*b.center)['nw'])

for i, row in enumerate(b.grid):
    if not i % 2:
        print('   ', end = '')
    for h in row:
        sym = '*' if h is None else 'P'
        print('{0}     '.format(sym), end = '')
    print()
