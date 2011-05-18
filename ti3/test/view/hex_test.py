import unittest

import pygame

import ti3.view.hex as hex

class HexTest(unittest.TestCase):

    def setUp(self):
        self.hex = hex.Hex((200,175))

    def test_init(self):
        self.assertIsInstance(self.hex, pygame.Surface)

if __name__ == '__main__':
    unittest.main()
