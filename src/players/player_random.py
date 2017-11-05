import random

from src.base_player import BasePlayer

class PlayerRandom(BasePlayer):
    def play(self, board):
        possible_turns = board.available_places()
        return random.choice(possible_turns)
