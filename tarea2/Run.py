from Boards import *
import matplotlib.pyplot as plt

board = Board()
winf = []
wins = []

j = 0
print "Learning..."
while j != 50:
    board.play("X","O")
    board.play("O","X")
    j +=1

## Se jugaran 2 juegos con la red neuronal jugando primero, y luego con la red jugando segundo

board.learn("O", 20, board.networkfirst)
board.learn("X", 20, board.networksecond)
perfwin = board.playNeuralFirst("O", "X", 2)
perswin = board.playNeuralSecond("O", "X", 2)

