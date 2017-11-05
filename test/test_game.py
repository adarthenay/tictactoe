import unittest

from src.game import Game
from src.players.player_random import PlayerRandom

class TestGame(unittest.TestCase):
    def test_outcome(self):
        outcome = Game([PlayerRandom(1), PlayerRandom(2)]).outcome()
        self.assertIsInstance(outcome, tuple)
        self.assertEqual(len(outcome), 2)

        winner, number_of_marks = outcome
        self.assertIn(winner, range(3))
        self.assertIn(number_of_marks, range(5, 10))
