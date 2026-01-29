# game_logic.py

BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = -1

def create_board():
    board = []
    for i in range(BOARD_SIZE):
        board.append([EMPTY] * BOARD_SIZE)

    board[4][4] = WHITE
    board[4][5] = BLACK
    board[5][4] = BLACK
    board[5][5] = WHITE
    return board

