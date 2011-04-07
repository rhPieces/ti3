import pygame
from pygame.locals import *

class gInfoPanel(pygame.Surface):
    PTSIZE = 18 
    BACKGROUND = (0, 0, 0)
    COLOR = (250, 250, 250)

    def __init__(self, size):
        pygame.Surface.__init__(self, size)
        self.font = pygame.font.Font(None, self.PTSIZE)
        self.line_height = self.font.get_height()
        self.line_count = 0
        self.text = []

    def write(self, text):
        for line in text.split('\n'):
            self.text.append(line)   

    def clear(self):
        self.line_count = 0
        self.fill(self.BACKGROUND)
    
    def draw(self):
        for line in self.text:
            s = self.font.render(line, True, self.COLOR, self.BACKGROUND)
            rect = s.get_rect()
            rect.top = self.line_count * self.line_height
            rect.left = 0
            self.blit(s, rect)
            self.line_count += 1
        self.text = []
            
