# Class with colors for the GUI app

from dataclasses import dataclass
from pygame import Color

@dataclass
class Colors:
    """
    Data Class with all of the app colors

    Attributes
    ----------
    BLACK : tuple[int]
        black rgb color used for permanent numbers and grid
    GREY : tuple[int]
        grey rgb color used for temporary numbers
    WHITE : tuple[int]
        white rgb color used for window background
    RED : tuple[int]
        red rgb color used to select cells and mark them as wrong in visualizer
    GREEN : tuple[int]
        green rgb color used to mark cells as correct in visualizer
    """
    BLACK: tuple = (0, 0, 0)
    GREY: tuple = (128, 128, 128)
    WHITE: tuple = (255, 255, 255)
    RED: tuple = (217, 37, 13)
    GREEN: tuple = (151, 230, 65)
    