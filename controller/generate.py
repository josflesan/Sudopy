# Helper functions used to generate a random sudoku board

from controller.solver import check_valid, solve_backtrack
from copy import deepcopy
from random import randint as r

def generate_board():
    """
    Function that generates a random, partially filled board

        Returns:
                (list[int][int]): 2D array representing the model being used by the Board object
    """

    prob_filled = 2  # Increase this number to increase difficulty (TODO: Make this feature?)

    # While the sudoku board is not solvable...
    while True:

        # Initialise a new board
        new_board = [[0 for i in range(9)] for j in range(9)]

        for y in range(9):
            for x in range(9):
                
                # Each sudoku cell has a 80% chance of getting a number (see above)
                if r(1, 10) >= prob_filled:
                    new_board[y][x] = r(1, 9)  # Fill cell with random number 1 - 9
                    if check_valid(new_board, new_board[y][x], (y, x)):
                        continue  # If it is a valid move, then accept it
                    else:
                        new_board[y][x] = 0  # Otherwise, delete this move

        result_board = deepcopy(new_board)
        # If the board is solvable, return it
        if solve_backtrack(new_board):
            return result_board
