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

    import ti3.model.board as bm
    import ti3.model.hex as hm
    import ti3.view.board as bv
    import ti3.view.infopanel as ipv
    import config
except ImportError as e:
    print("Could not load module. {0}".format(e))
    sys.exit(2)

def setup_board():
    hexes = hm.load()
    mc = hexes[27]

    board = bm.Board(3, 3)
    board.set_hex(mc, *board.center)

    board.set_hex(hexes[0], *board.adjacent_coords(*board.center)['n'])
    board.set_hex(hexes[1], *board.adjacent_coords(*board.center)['ne'])
    board.set_hex(hexes[2], *board.adjacent_coords(*board.center)['se'])
    board.set_hex(hexes[3], *board.adjacent_coords(*board.center)['s'])
    board.set_hex(hexes[4], *board.adjacent_coords(*board.center)['sw'])
    board.set_hex(hexes[5], *board.adjacent_coords(*board.center)['nw'])
    return board

def main():
    pygame.init()
    clk = pygame.time.Clock()

    screen = pygame.display.set_mode((config.width, config.height))
    pygame.display.set_caption('Twilight Imperium')

    board = setup_board()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    gb = bv.Board((round(config.width * .8), config.height))
    gb.set_board(board)
    gb.draw()
    gbpos = gb.get_rect()
    gbpos.top = 0
    gbpos.left = round(config.width * .2)

    ip = ipv.InfoPanel((round(config.width * .2), config.height))
    ip.write('Hello World\nThis is a test')
    ip.draw()
    ippos = ip.get_rect()
    ip.top = 0
    ip.left = 0


    background.blit(gb, gbpos)
    background.blit(ip, ippos)
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
