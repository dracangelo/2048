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

def is_game_over(board):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return False
            if i < SIZE - 1 and board[i][j] == board[i + 1][j]:
                return False
            if j < SIZE - 1 and board[i][j] == board[i][j + 1]:
                return False
    return True

def play_game():
    board = init_board()
    while True:
        print_board(board)
        move_input = input("Enter move (W=Up, S=Down, A=Left, D=Right): ").upper()
        if move_input not in ['W', 'A', 'S', 'D']:
            print("Invalid move. Use W, A, S, D keys.")
            continue
        if move_input == 'W':
            direction = 'UP'
        elif move_input == 'A':
            direction = 'LEFT'
        elif move_input == 'S':
            direction = 'DOWN'
        elif move_input == 'D':
            direction = 'RIGHT'
        
        new_board = move(board, direction)
        if new_board != board:
            board = new_board
            add_new_tile(board)
        
        if is_game_over(board):
            print_board(board)
            print("Game Over!")
            break

if __name__ == "__main__":
    play_game()
