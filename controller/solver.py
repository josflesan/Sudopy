# Solver file containing helper methods

from typing import List, Tuple


def solve_backtrack(b: List[int]) -> bool:
    '''
    Function that solves a partially complete sudoku board using backtracking.
    The algorithm recursively finds an empty cell, and for each possible
    number (1-9) checks if the move is valid, otherwise it moves back and reverses
    its moves.

        Parameters:
                b (list[int][int]): 2D Array representing the incomplete sudoku board
        
        Returns:
                True/False (boolean): A value to stop the backtracking
    '''
    empty_cell = find_empty(b)
    if not empty_cell:
        return True  # Stop backtracking, sudoku board solved
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if check_valid(b, i, (row, col)):
            b[row][col] = i

            if solve_backtrack(b):
                return True

            b[row][col] = 0

    return False


def check_valid(b: List[int], num: int, pos: int) -> bool:
    '''
    Function that checks whether or not a particular move is valid.

        Parameter:
                b (list[int][int]): 2D array representing the sudoku board
                num (int):          The number to be inserted into the cell
                pos (tuple[int]):   The tuple representing the position of the cell (row, col)

        Returns:
                True/False (bool):  Whether or not the move is valid
    '''

    # Check Row
    for col in range(len(b[0])):
        # pos[0]: row position of move
        if b[pos[0]][col] == num and pos[1] != col:
            return False

    # Check Column
    for row in range(len(b)):
        if b[row][pos[1]] == num and pos[0] != row:
            return False

    # Check Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y*3, box_y*3 + 3):
        for col in range(box_x*3, box_x*3 + 3):
            if b[row][col] == num and (row, col) != pos:
                return False

    return True  # If no rules broken, valid move


def find_empty(b: List[int]) -> Tuple[int]:
    '''
    Function that finds an empty cell in the sudoku board

        Parameters:
                b (list[int][int]): the 2d array representing the sudoku board

        Returns:
                (row, col) (tuple[int]): Tuple representing the row and column for the empty cell
    '''
    for row in range(len(b)):
        for col in range(len(b[0])):
            if b[row][col] == 0:  # 0 Represents an empty cell in our model
                return (row, col)  

    return None