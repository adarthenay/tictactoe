from src.board import Board
 

class Game(object):
    def __init__(self, player_set):
        self.player_set=player_set
        
        
    def outcome(self):
        self.board=Board()
        turn=0
        while len(self.board.available_places())>0 and self.board.winner()==0:
            l,c=player_set[turn].play(self.board)
            self.board.grid[l][c]=turn+1
            turn=not turn 
        return (self.board.winner,0)
        