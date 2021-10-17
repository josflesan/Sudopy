import pygame

from model.colors import Colors
from model.constants import Constants

class Cell:
    """
    Cell class modelling each of the sudoku cells

    Attributes
    ----------
    num : int
        the number held by the cell
    row : int
        the row position of the cell (1-9)
    col : int
        the column position of the cell (1-9)
    bWidth : int
        the width of the Sudoku board
    bHeight : int
        the height of the Sudoku board
    tempNum : int
        the temporary number added as a note to the cell
    selected : bool
        whether or not the cell is selected

    Methods
    -------
    draw(window):
        Draws the cell's contents to the pygame window
    """

    ROWS, COLS = 9, 9

    def __init__(self, num, row, col, boardWidth, boardHeight):
        """
        Constructs necessary attributes for Cell object

            Parameters:
                    num (int): The number to be assigned to the cell
                    row (int): The row (1-9) position of the cell
                    col (int): The col (1-9) position of the cell
                    boardWidth (int): The width of the board object
                    boardHeight (int): The height of the board object
        """
        self.__row = row
        self.__col = col
        self.__bWidth = boardWidth
        self.__bHeight = boardHeight
        self._num = num
        self._tempNum = 0
        self._selected = False

    # GETTERS

    @property
    def num(self):
        return self._num

    @property
    def tempNum(self):
        return self._tempNum

    @property
    def selected(self):
        return self._selected

    # SETTERS

    @num.setter
    def num(self, val):
        self._num = val

    @tempNum.setter
    def tempNum(self, val):
        self._tempNum = val

    @selected.setter
    def selected(self, val):
        self._selected = val


    def draw(self, window):
        """
        Function that draws the cell onto the screen, as well as its number

            Parameter:
                    window (pygame.display Object): The pygame window
        """
        fnt = pygame.font.SysFont(Constants.FONT, Constants.FONT_SIZE)

        padding = self.__bWidth / 9  # The cell padding will be board width div by 9
        x = self.__col * padding 
        y = self.__row * padding

        # If it is a temporary number, show it in grey and left aligned
        if self.tempNum != 0 and self.num == 0:
            text = fnt.render(str(self.tempNum), 1, Colors.GREY)
            window.blit(text, (x+5, y+5))
        # If it is a permanent number, show it in black and centered
        elif not(self.num == 0):
            text = fnt.render(str(self.num), 1, Colors.BLACK)
            window.blit(text, (x + (padding/2 - text.get_width()/2), y + (padding/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(window, Colors.RED, (x, y, padding, padding), 4)
