"""
Functions and classes for drawing a hex
"""
import math

import pygame
from pygame.locals import *

class Hex(pygame.Surface):

    def __init__(self, size, FILL = (250, 250, 0), WEIGHT = 6, OFFSET = 3):
        pygame.Surface.__init__(self, size)
        self.set_colorkey(FILL)
        self.fill(FILL)
        self.weight = WEIGHT
        self.offset = OFFSET

        self.hex = None

    def set_hex(self, hex):
        self.hex = hex

    def draw(self):
        if self.hex is not None:
            pygame.draw.polygon(
                self, self.get_color(), self._get_points(), self.weight
            )

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

    def _get_points(self):
        height = self.get_height() - self.offset
        width = self.get_width() - self.offset
        r = round(height / 2.0)
        s = round(1 / (math.cos(math.pi / 6) / r))
        h = round(math.sin(math.pi / 6) * s)
        return ((h, 0), (h + s, 0), (width, r),
                (h + s, height), (h, height), (0, r))
