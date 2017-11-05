# tictactoe
The ultimate game for learning Python

## Most important: how to run tests
At the root of the working copy, type:
```
$ python -m unittest discover
```

## Program architecture
### Principle
A tictactoe game is a 3x3 board game for two players. Each player, one after the other, places a mark on the board. The first one that has successfully aligned either one row, one column or one diagonal is the winner of the game.

### What needs to be done
1. The Game class is missing! This means that two Players cannot fight each other in a Tournament
2. The only implemented Player is PlayerRandom, which is not the smarter. Once Game class is created, why not create a Player that you can set a Tournament with?

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

##### available_places()
Returns a list of tuples corresponding to the remaining playable turns on the board, each tuple representing:
- *Line* number at index 0
- *Column* number at index 1
```
>>> from src.board import Board
>>> b = Board("""
    201
    210
    122""")
>>> b.available_places()
[(0, 1), (1, 2)]
```

### Player classes
The Player classes are stored in the src/players directory. They inherit from the BasePlayer class located in src/.
A *Player* class is responsible for holding an AI player strategy.

```
>>> from src.players.player_random import PlayerRandom
>>> from src.board import Board
>>> p = PlayerRandom(1)
>>> p.play(Board())
(1, 0)
```

#### Player methods and attributes
##### Player(player_number)
A player must be instantiated with the number it plays the game

##### play(board)
Takes and instance of Board as an argument.
Returns a length 2 tuple indicating:
- at index 0 which *line* the player just played
- at index 1 which *column* the player just played

### Game class
A game is defined by two players (inheriting from the BasePlayer class). The game is responsible for creating an instance of a board, and updating it as the two players play turns. The game is characterized by its outcome, defining who is the winner.

#### Game methods and attributes
### Game(player_set)
The instantiation takes a table of 2 instances of objects inheriting from the BasePlayer class.

### outcome()
Returns a tuple of length 2, having at the following indexes:
0. Winner: integer value indicating if there is a winner, and who is it, according to the following code:
   - Integer 0 for "The game is tie / ex aequo"
   - Integer 1 for "Winner is player 1"
   - Integer 2 for "Winner is player 2"
1. Number of marks: integer value indicating the number of times a mark was made on the board (2 per turn)

### Tournament class
The point of a Tournament consist of measuring two players, with a given number of rounds, including reverting the order of the players to cancel the fact that first player has a significant advantage.
To launch a tournament between the PlayerRandom players, just type at the root of the working copy:
```
$ python -m src.tournament
```

#### Tournament methods and attributes
### Tournament(players_class_table, number_of_games_per_round=1000, alternate_start=True)
Init function takes the following arguments:
- **players_class_table**: a list of *classes* (not instances!) of the Tournament players. For example
```
[PlayerRandom, PlayerRandom]
```
- **number_of_games_per_round** (default value: 1000): integer value representing the number of games that will be played in one round. Note: if alternate_start is set to True, the Tournament total number of games will be doubled, in order to switch the first player.

- **alternate_start** (default value: True): indicates whether the Tournament will exchange the first and second player to take into account the fact that the first player has a significant advantage. If set to False, there will be only one round, and index 0 of the players_class_table argument will always play first. If set to True, there will be two rounds were the index 0 of the players_class_table will play first, and a second round were it will play second.

### outcome()
Returns a tuple of length 2, having at the following indexes:
0. Victories: Tuple of length 3 indicating at the following indexes:
   0. Number of "The game is tie / ex aequo" games
   1. Number of "Winner is index 0 of players_class_table" games
   2. Number of "Winner is index 1 of players_class_table" games
1. Total number of marks: integer value indicating the tournament total number of times a mark was made on the board (2 per turn)
