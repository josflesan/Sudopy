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
    """

    APP_TITLE = "SudoPy"
    FONT = "ubuntumono"

    WIN_DIMENS = (540, 600)
    WIN_WIDTH = WIN_DIMENS[0]
    WIN_HEIGHT = WIN_DIMENS[1]
    FONT_SIZE = 30