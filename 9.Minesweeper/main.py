import random

def create_board(rows, cols, bombs):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    bomb_positions = random.sample(range(rows * cols), bombs)
    for position in bomb_positions:
        row = position // cols
        col = position % cols
        board[row][col] = '*'
    return board

def reveal_cells(board, row, col):
    if board[row][col] == ' ':
        bombs_nearby = count_bombs(board, row, col)
        board[row][col] = str(bombs_nearby)
        if bombs_nearby == 0:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                        reveal_cells(board, i, j)

def count_bombs(board, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == '*':
                count += 1
    return count

def print_board(board):
    for row in board:
        print(' '.join(row))

def play_game():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    bombs = int(input("Enter the number of bombs: "))
    board = create_board(rows, cols, bombs)
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        
        if board[row][col] == '*':
            print("Game Over! You hit a bomb.")
            game_over = True
        else:
            reveal_cells(board, row, col)
            if all(all(cell != ' ' for cell in row) for row in board):
                print("Congratulations! You won!")
                game_over = True

play_game()
