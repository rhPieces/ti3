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

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Twilight Imperium')

    img = pygame.image.load('data/images/tiles/sardakk_norr.png')
    img = img.convert_alpha()
    img_rect = img.get_rect()
    img = pygame.transform.scale(img, (img_rect.width/3, img_rect.height/3))
    img_rect = img.get_rect()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to Twilight Imperium", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    img_rect.centerx = background.get_rect().centerx
    img_rect.centery = background.get_rect().centery + 50
    background.blit(text, textpos)
    background.blit(img, img_rect)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
