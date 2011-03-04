"""
Functions and classes for drawing the board
"""

import pygame
from pygame.locals import *
from hex import gHex

class gBoard(pygame.Surface):

    def set_board(self, board):
        self.board = board
        self.grid = []
        for row in range(0, len(board.grid)):
            for col in range(0, len(board.grid[0])):
                if col == 0:
                    self.grid.append([])
                self.grid[row].append(gHex((200, 175)))
                self.grid[row][col].set_hex(self.board.get_hex(row, col))

    def draw(self):
        self.set_colorkey((250, 250, 250))
        self.fill((250, 250, 250))
        initialx = 100
        initialy = 100
        xinc = 150
        yinc = 175
        for row, hexes in enumerate(self.grid):
            for col, hex in enumerate(hexes):
                hex.draw()
                hex.convert()

                rect = hex.get_rect()
                offset = 0
                if not col % 2:
                    offset = 87

                rect.centerx = initialx + (col * xinc)
                rect.centery = initialy + (row * yinc) + offset
                self.blit(hex, rect)

