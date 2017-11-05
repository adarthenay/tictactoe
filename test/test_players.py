import unittest

from src.players.player_random import PlayerRandom

from .base_test_players import PlayerTestCase

class TestPlayerRandom(PlayerTestCase, unittest.TestCase):
    def setUp(self):
        self.player = PlayerRandom(1)

if __name__ == "__main__":
    unittest.main()
