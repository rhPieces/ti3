#!/opt/local/bin/python
#
# Twilight Imperium
#    Electronic version of Fantasy Flight's Twilight Imperium, 3rd Edition
#
# Author - Reece Heinlein
# Released under the GNU General Public License

try:
    import sys
    import pygame
    from pygame.locals import *
except ImportError, e:
    print("Could not load module. {0}".format(e))
    sys.exit(2)

def main():
    pygame.init()
    clk = pygame.time.Clock()

    screen = pygame.display.set_mode((1440, 900), FULLSCREEN)
    pygame.display.set_caption('Twilight Imperium')


    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    hex = get_hex()
    rect = hex.get_rect()
    initialx = 100
    initialy = 100
    xinc = 150
    yinc = 175
    for row in range(0, 4):
        for col in range (0, 9):
            offset = 0
            if col % 2:
                offset = 87
            rect.centerx = initialx + (col * xinc)
            rect.centery = initialy + (row * yinc) + offset
            background.blit(hex, rect)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return

        clk.tick(60)
        screen.blit(background, (0, 0))
        pygame.display.flip()

def get_hex():
    hex = pygame.Surface((200, 175))
    hex.set_colorkey((0, 250, 0))
    hex.convert()
    hex.fill((0, 250, 0))
    pygame.draw.polygon(hex, (0, 0, 250), ((49, 0), (149, 0), (199, 87), (149, 174), (49, 174), (0, 87)), 2)

    return hex

if __name__ == '__main__':
    main()
