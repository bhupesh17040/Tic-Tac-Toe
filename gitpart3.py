# HOMEWORK ASSIGNMENT 2
#Game Tic-tac-toe

# Strategising Tic-Tac-Toe Gameplay

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 
tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______
A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.
We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

from random import randint
# There are 2 players: player1 and player2
player1 = 1
player2 = 2

 
#  There are 9 tiles numbered tile0 to tile9
#  0 value of a tile indicates that tile has not been ticked
#  1 value indicates that the tile is ticked by player-1
#  2 value indicates that the tile is ticked by player-2