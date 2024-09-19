import random
import os

SIZE = 4  # Board size
NEW_TILE = [2, 4]  # Possible new tile values

def init_board():
    board = [[0]*SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = random.choice(NEW_TILE)

def print_board(board):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in board:
        print("\t".join([str(num) if num != 0 else '.' for num in row]))
    print("\n")

def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]
