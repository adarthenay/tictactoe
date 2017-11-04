from test.base_test_players import PlayerTestCase
from src.players.player_random import PlayerRandom

class TestPlayerRandom(PlayerTestCase):
    def setUp(self):
        self.player = PlayerRandom()
