from game import Game
from board import Board

import ctypes

user32 = ctypes.windll.user32

size = (16,16)
prob = 0.15
board = Board(size, prob)
# screenSize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
screenSize = (1000, 1000)
game = Game(board, screenSize)
game.run()
