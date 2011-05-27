"""
Functions and Classes dealing with the game board
"""

class Board:
    def __init__(self, max_rows, max_cols):
        self.grid = []
        self.max_rows = max_rows
        self.max_cols = max_cols
        self.center = (max_rows / 2, max_cols / 2)
        for row in range(0, max_rows):
            self.grid.append([None for col in range(0, max_cols)])

    def set_hex(self, hex, row, col):
        self.grid[row][col] = hex

    def get_hex(self, row, col):
        if row is None or col is None:
            return None
        return self.grid[row][col]

    def adjacent_hexes(self, row, col):
        return dict((dir, self.get_hex(*coord))
                for dir, coord in self.adjacent_coords(row, col).iteritems()
                    if coord is not None)

    def adjacent_coords(self, row, col):
        none = (None, None)
        return {
            'n': (row - 1, col) if row >= 1 else none,
            'ne': (row - 1, col + 1) if row >= 1 and col <= self.max_cols - 1 else none,
            'se': (row, col + 1) if  col <= self.max_cols - 1 else none,
            's': (row + 1, col) if row <= self.max_rows - 1 else none,
            'sw': (row, col - 1) if  col >= 1 else none,
            'nw': (row - 1, col - 1) if row >= 1 and col >= 1 else none,
        }

