import unittest
from src.board import Board

class PlayerTestCase(unittest.TestCase):
    def test_range(self):
        turn = self.player.play(Board())
        self.assertIsInstance(turn, Tuple)



