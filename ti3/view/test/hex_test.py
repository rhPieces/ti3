import unittest

import pygame

import ti3.view.hex as hex_view
import ti3.model.hex as hex_model

class HexTest(unittest.TestCase):

    def setUp(self):
        self.hex = hex_view.Hex((200,175))
        self.hex.set_hex(
            hex_model.Hex({
                '_id': 1,
                'type':'Planet',
                'set':'',
                'entities':[]
            })
        )

    def test_init(self):
        self.assertIsInstance(self.hex, pygame.Surface)
        self.assertIsInstance(self.hex.hex, hex_model.Hex)

    def test_set_hex(self):
        self.hex.set_hex(1)
        self.assertEqual(1, self.hex.hex)

    @unittest.skip("Test a surface")
    def test_draw(self):
        pass

    def test_get_color(self):
        self.assertEqual((0, 250, 0), self.hex.get_color());
        
        self.hex.hex.type = 'Special'
        self.assertEqual((250, 0, 0), self.hex.get_color());
        self.hex.hex.type = 'Homeworld'
        self.assertEqual((0, 250, 250), self.hex.get_color());
        self.hex.hex.type = 'Empty'
        self.assertEqual((0, 0, 250), self.hex.get_color());

if __name__ == '__main__':
    unittest.main()
