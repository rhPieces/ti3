#!/opt/local/bin/python
#
# Twilight Imperium
#    Electronic version of Fantasy Flight's Twilight Imperium, 3rd Edition
#
# Author - Reece Heinlein
# Released under the GNU General Public License

from __future__ import print_function
try:
    import sys
    import pygame
    from pygame.locals import *
    import board as bm
    import gui.board as gbm
    import hex as hm
    import config
except ImportError, e:
    print("Could not load module. {0}".format(e))
    sys.exit(2)

def setup_board():
    phexes = hm.load(type = 'Planet')
    shexes = hm.load(type = 'Special')
    mc = hm.load(entities = {'$elemMatch': {'name' : 'Mecatol Rex'}})[0]

    b = bm.Board(3, 3)
    b.set_hex(mc, *b.center)

    b.set_hex(phexes[0], *b.adjacent_coords(*b.center)['n'])
    b.set_hex(phexes[1], *b.adjacent_coords(*b.center)['ne'])
    b.set_hex(shexes[0], *b.adjacent_coords(*b.center)['se'])
    b.set_hex(phexes[3], *b.adjacent_coords(*b.center)['s'])
    b.set_hex(phexes[4], *b.adjacent_coords(*b.center)['sw'])
    b.set_hex(phexes[5], *b.adjacent_coords(*b.center)['nw'])
    for row in b.grid:
        for hex in row:
            if hex is not None:
                print(hex.type, sep = ' ', end = ' ')
            else:
                print('None', sep = ' ', end = ' ')
        print()
    return b

def main():
    pygame.init()
    clk = pygame.time.Clock()

    screen = pygame.display.set_mode((config.width, config.height))
    pygame.display.set_caption('Twilight Imperium')

    b = setup_board()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    gb = gbm.gBoard((900,900))
    gb.set_board(b)
    gb.draw()

    gbpos = gb.get_rect()
    gbpos.centerx = screen.get_rect().centerx
    gbpos.centery = screen.get_rect().centery

    background.blit(gb, gbpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        changed = False
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return

        clk.tick(60)
        if changed:
            screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
