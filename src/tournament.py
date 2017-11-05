from .game import Game

class Tournament(object):
    def __init__(self, players_class_table, number_of_games_per_round=1000, alternate_start=True):
        self.players_class_table = players_class_table
        self.number_of_games_per_round = number_of_games_per_round
        self.alternate_start = alternate_start

    def outcome(self):
        player_sets = [(self.players_class_table[0](1), self.players_class_table[1](2))]
        victories = [0, 0, 0]
        total_number_of_marks = 0
        if self.alternate_start:
            player_sets.append((self.players_class_table[1](1), self.players_class_table[0](2)))
        for player_set_index, player_set in enumerate(player_sets):
            for round in range(self.number_of_games_per_round):
                winner, number_of_marks = Game(player_set).outcome()
                total_number_of_marks += number_of_marks
                if winner == 0:
                    victories[0] += 1
                else:
                    if player_set_index == 0:
                        victories[winner] += 1
                    else:
                        victories[3 - winner] += 1
        return (victories, total_number_of_marks)

if __name__=='__main__':
    from src.players.player_random import PlayerRandom
    print Tournament([PlayerRandom, PlayerRandom]).outcome()
