"""
Functions and classes for drawing a hex
"""

import pygame
from pygame.locals import *

class Hex(pygame.Surface):

    def __init__(self, size):
        pygame.Surface.__init__(self, size)
        self.hex = None

    def set_hex(self, hex):
        self.hex = hex

    def draw(self):
        self.set_colorkey((250, 250, 0))
        self.fill((250, 250, 0))
        if self.hex is not None:
            pygame.draw.polygon(self, self.get_color(), ((49, 0), (149, 0), (199, 87), (149, 174), (49, 174), (0, 87)), 0)
            pygame.draw.polygon(self, (250, 250, 250), ((49, 0), (149, 0), (199, 87), (149, 174), (49, 174), (0, 87)), 2)

    def get_color(self):
        color = (0, 0, 0)
        if self.hex is not None:
            if self.hex.type == 'Planet':
                color = (0, 250, 0)
            elif self.hex.type == 'Special':
                color = (250, 0, 0)
            elif self.hex.type == 'Homeworld':
                color = (0, 250, 250)
            elif self.hex.type == 'Empty':
                color = (0, 0, 250)

        return color


