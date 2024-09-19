import random
import os

SIZE = 4  # Board size
NEW_TILE = [2, 4]  # Possible new tile values

def init_board():
# <<<<<<<<<<<<<<  ✨ Codeium Command ⭐  >>>>>>>>>>>>>>>>
    """
    Initializes a new game board with two random tiles.
    
    Returns a 2D list of size SIZE x SIZE, where each element is an integer.
    The board will contain two random tiles, each being a 2 or a 4.
    """
# <<<<<<<  9569ce85-220f-4259-870b-f5d60c2a803d  >>>>>>>
    board = [[0]*SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
# <<<<<<<<<<<<<<  ✨ Codeium Command ⭐  >>>>>>>>>>>>>>>>
    """
    Adds a new tile to a random empty position on the board.
    
    A random empty position is chosen from the board, and one of the values
    in NEW_TILE is chosen at random and placed in that position.
    
    :param board: The 2D list representing the board.
    :type board: List of lists of int
    """
# <<<<<<<  ffd04def-e949-495a-8128-29ef61314e8f  >>>>>>>
    empty_tiles = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = random.choice(NEW_TILE)

def print_board(board):
# <<<<<<<<<<<<<<  ✨ Codeium Command ⭐  >>>>>>>>>>>>>>>>
    """
    Prints the current state of the board to the console.
    
    :param board: The 2D list representing the board.
    :type board: List of lists of int
    """
# <<<<<<<  9102cc71-e806-4f00-bbcc-123798d14fc4  >>>>>>>
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
# <<<<<<<<<<<<<<  ✨ Codeium Command ⭐  >>>>>>>>>>>>>>>>
    """
    Starts a new game of 2048.
    
    This function will continually print the current state of the board and
    ask the user for a move until the game is over. The game is over when
    there are no more valid moves left.
    
    The user is asked to enter a move (W=Up, S=Down, A=Left, D=Right) and
    the board is updated accordingly. If the user enters an invalid move, a
    message is printed and the user is asked again.
    
    When the game is over, the final state of the board is printed and a
    message is printed to indicate that the game is over.
    """
# <<<<<<<  0b745cd7-da88-4dfb-bb7a-1efe41e1fd1a  >>>>>>>
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
