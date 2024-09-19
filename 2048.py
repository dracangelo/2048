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

def merge_left(row):
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False
    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])
    return merged_row + [0] * (SIZE - len(merged_row))

def move_left(board):
    new_board = []
    for row in board:
        new_board.append(merge_left(row))
    return new_board

def move(board, direction):
    if direction == 'UP':
        board = rotate_board(board)
        board = move_left(board)
        for _ in range(3):  # Rotate back to original position
            board = rotate_board(board)
    elif direction == 'DOWN':
        for _ in range(3):
            board = rotate_board(board)
        board = move_left(board)
        board = rotate_board(board)
    elif direction == 'LEFT':
        board = move_left(board)
    elif direction == 'RIGHT':
        for _ in range(2):
            board = rotate_board(board)
        board = move_left(board)
        for _ in range(2):
            board = rotate_board(board)
    return board

