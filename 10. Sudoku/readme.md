Sudoku Solver
This Python program is designed to solve Sudoku puzzles using a backtracking algorithm. Here's a breakdown of its features:

Features:
find_next_empty(puzzle): This function searches the puzzle for the next empty cell (denoted by -1) and returns its row and column indices.

is_valid(puzzle, guess, row, col): This function checks if a guess is valid for a given cell in the puzzle. It ensures that the guess does not violate Sudoku rules within the row, column, and 3x3 grid.

solve_sudoku(puzzle): This is the main function that solves the Sudoku puzzle recursively using backtracking. It finds the next empty cell, makes a valid guess, and continues solving until the puzzle is solved or determines that no solution exists.

print_board(board): This function prints the Sudoku board in a human-readable format.

Example Sudoku Board: An example Sudoku board is provided within the _main_ block. This board represents an unsolved Sudoku puzzle, where empty cells are denoted by -1.

Solution: If a solution exists, the program prints the solved Sudoku board. Otherwise, it informs the user that no solution exists.
