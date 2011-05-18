import unittest
import view.hex as hex

class HexTest(unittest.TestCase):

    def setUp(self):
        self.hex = hex.Hex()

    def test_init(self):
        self.assertType('pygame.Surface', self.hex)

if __name__ == '__main__':
    unittest.main()
