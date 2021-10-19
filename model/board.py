from controller.solver import check_valid, solve_backtrack
from model.cell import Cell
from model.colors import Colors
from typing import List, Tuple
from copy import deepcopy
import pygame

class Board:
    """
    Class modelling the Sudoku Board

    Attributes
    ----------
    model : list[int][int]
        the 2D array modelling the state of the Sudoku board
    rows : int
        the number of rows in the Sudoku board (9)
    cols : int
        the number of columns in the Sudoku board (9)
    width : int
        the width of the Sudoku board
    height : int
        the height of the Sudoku board
    selected : tuple[int]
        the row and column position of the selected cell
    cells : list[Cell][Cell]
        the 2D array containing all of the cell objects in the Sudoku board

    Methods
    -------
    update_board():
        function that updates the internal 2D model of the Sudoku board
    insert_num(val):
        function that inserts a number into one of the cells in the Sudoku board
    add_note(val):
        function that adds a number as a note into the selected cell of the Sudoku board
    draw(window):
        function that draws the Sudoku board onto the pygame window
    select(row, col):
        function that selectes a particular cell in the Sudoku board
    clear():
        function that clears the Sudoku board
    click(pos):
        function that handles the logic of the user clicking on the Sudoku board
    is_finished():
        function that checks to see if the Sudoku board is full

    """

    BOARD = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows: int, cols: int, width: int, height: int) -> None:
        """
        Constructor function that initialises the necessary attributes for Board object

            Parameter:
                    rows (int): The number of rows in the sudoku board (9)
                    cols (int): The number of columnns in the sudoku board (9)
                    width (int): The width of the sudoku board
                    height (int): The height of the sudoku board
        """
        self._rows = rows
        self._cols = cols
        self._width = width
        self._height = height
        self._selected = None

        self.cells = [[Cell(self.BOARD[i][j], i, j, width, height) for j in range(cols)] 
                        for i in range(rows)]
        self.model = self.BOARD

    # GETTERS

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def selected(self) -> Tuple[int]:
        return self._selected

    # SETTERS

    @selected.setter
    def selected(self, pos: Tuple[int]) -> None:
        self._selected = pos

    # METHODS

    def update_board(self) -> None:
        """Function that updates the 2D array model for the sudoku board"""
        self.model = [[self.cells[i][j].num for j in range(self.cols)]
                        for i in range(self.rows)]

    def insert_num(self, val: int) -> bool:
        """
        Function that inserts a number into a cell in the Sudoku

            Parameters:
                    val (int): The value to be inserted into the selected cell in the Sudoku board
            
            Returns:
                    (bool): Whether or not the move was valid
        """
        row, col = self.selected  # Get the position of the selected cell
        # If the cell is currently empty
        if self.cells[row][col].num == 0:
            # Update the number of the cell and the model
            self.cells[row][col].num = val
            self.update_board()

            old_model = deepcopy(self.model)  # Save current state of the model

            # If the move is valid (check using the backtracking algorithm), move is ok
            if check_valid(self.model, val, (row, col)) and solve_backtrack(self.model):
                # Clear the model, then return (so visualization still works)
                self.model = old_model
                return True
            # If the move is not valid, bring cell back to default and update the model again
            else:
                self.cells[row][col].num = 0
                self.cells[row][col].tempNum = 0
                self.update_board()
                return False

    def add_note(self, val: int) -> None:
        """
        Function that assigns a temporary value to the selected cell

            Parameters:
                    val (int): The value to be added as a note to the cell
        """
        row, col = self.selected
        self.cells[row][col].tempNum = val

    def draw(self, window: pygame.display) -> None:
        """
        Function that draws the board in the pygame display

            Parameters:
                    window (pygame.display): The pygame window to be drawn to
        """

        # Draw grid lines
        gap = self.width / 9  # The size of the cells
        # For each of the rows in the sudoku board (1-9)...
        for i in range(self.rows + 1):
            # If it is one of the box rows, make the line thicker
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            # Draw a horizontal line and a vertical line at the corresponding position
            pygame.draw.line(window, Colors.BLACK, (0, i*gap), (self.width, i*gap), thickness)
            pygame.draw.line(window, Colors.BLACK, (i*gap, 0), (i*gap, self.height), thickness)

        # Draw each cell, for each cell in the board
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(window)

    def select(self, row: int, col: int) -> None:
        """
        Function that selects a cell in the board by setting the appropriate flag

            Parameters:
                    row (int): The row position of the cell
                    col (int): The column position of the cell
        """

        # Reset all other cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False

        # Set the current cell as selected and save its position
        self.cells[row][col].selected = True
        self.selected = (row, col)

    def clear(self) -> None:
        """Function that clears the selected cell"""
        row, col = self.selected  # Get the position of the selected cell
        if self.cells[row][col].num == 0:
            self.cells[row][col].tempNum = 0

    def click(self, pos: int) -> Tuple[int]:
        """
        Function to handle the logic of the user clicking on the board

            Parameters:
                    pos (int): The position of the click, as collected by pygame
            
            Returns:
                    (tuple[int]): The x and y position of the start of the cell that was clicked
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))

        else:
            return None
    
    def is_finished(self) -> bool:
        """
        Function that checks whether or not the Sudoku board is full and hence the game has finished

            Returns:
                    (bool): Whether or not the board is full/game has finished
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].num == 0:
                    return False
        return True
            