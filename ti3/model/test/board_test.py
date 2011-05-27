import unittest
import ti3.model.board as board_model

class HexTest(unittest.TestCase):

    def setUp(self):
        self.board = board_model.Board(3, 3)

    def test_init(self):
        board = board_model.Board(3, 3)
        self.assertEqual(board.center, (1, 1))
        self.assertIsNone(board.get_hex(0, 0))
        self.assertIsNone(board.get_hex(2, 2))

    def test_get_set_hex(self):
        self.board.set_hex('test', 0, 0)
        self.assertEqual('test', self.board.get_hex(0, 0))

    def test_adjacent_hexes(self):
        self.board.set_hex('se', 0, 1);
        self.board.set_hex('s', 1, 0);
        result = self.board.adjacent_hexes(0, 0)
        self.assertIsNone(result['n'])
        self.assertIsNone(result['nw'])
        self.assertIsNone(result['sw'])
        self.assertEqual('s', result['s'])
        self.assertEqual('se', result['se'])


if __name__ == '__main__':
    unittest.main()
