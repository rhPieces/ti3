# GameState
#   Stores the stage of a game.
# Author - Reece Heinlein

class GameState:
    """Class to contain the state of a game"""
    def __init__(self):
        self.players = None
        self.board = None
        self.objective_deck = None
        self.action_deck = None
        self.political_deck = None
        self.point_limit = 0
        self.strategies = None
