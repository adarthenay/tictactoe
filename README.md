# tictactoe
The ultimate game for learning Python

## Most important: how to run tests
At the root of the working copy, type:
```
$ python -m unittest discover
```

## Program architecture
### Principle
A tictactoe game is a 3x3 board game for two players. Each player, one after the other, place a mark on the board. The first one that has successfully aligned either one row, one column or one diagonal is the winner of the game.

### Board
The *Board* class is in charge of keeping and delivering board information as well as undertanding whether there is a winner or not. The information is stored as the following:
- Integer 0 for "Empty place in the board"
- Integer 1 for "Player 1"
- Integer 2 for "Player 2"

```
>>> from src.board import Board
>>> b = Board()               # creates a new instance of board
>>> b.grid
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> b.is_empty()
True
>>> b.winner()
0
```

#### Board methods and attributes
##### grid
Attribute, return a list of *lines*, each line being a list of slots of the board.
This attribute is read/write.

##### is_empty()
Returns True if the board is empty, False otherwise.

##### winner()
Returns an integer value indicating if there is a winner, and who is it, according to the following code:
- Integer 0 for "No winner"
- Integer 1 for "Player 1"
- Integer 2 for "Player 2"

### Player classes
The Player classes are stored in the src/players directory. They inherit from the BasePlayer class located in src/.
A *Player* class is responsible for holding an AI player strategy.

```
>>> from src.players.random import PlayerRandom
>>> from src.board import Board
>>> p = PlayerRandom()
>>> p.play(Board())
(1, 0)
```

#### Player methods and attributes
##### play(board)
Takes and instance of Board as an argument.
Returns a length 2 tuple indicating:
- at index 0 which *line* the player just played
- at index 1 which *column* the player just played
 




