# Class with all of the app constants

from dataclasses import dataclass

@dataclass
class Constants:
    """
    Data Class containing all of the app constants

    Attributes
    ----------
    APP_TITLE : str
        the title of the app
    FONT : str
        the name of the font used by the app
    WIN_DIMENS : tuple[int]
        the x and y dimensions of the window
    WIN_WIDTH : int
        the x dimension of the window
    WIN_HEIGHT : int
        the y dimension of the window
    FONT_SIZE : int
        the font size used by the app
    BTN_FONT_SIZE : int
        the font size used for button text
    Y_OFFSET : int
        the amount (in px) the board is displaced down
    """

    APP_TITLE = "SudoPy"
    FONT = "ubuntumono"

    WIN_DIMENS = (540, 770)
    WIN_WIDTH = WIN_DIMENS[0]
    WIN_HEIGHT = WIN_DIMENS[1]
    FONT_SIZE = 30
    BTN_FONT_SIZE = 20
    Y_OFFSET = 150  # The y position at which the board is drawn