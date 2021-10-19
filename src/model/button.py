from typing import Tuple
from model.colors import Colors
from model.constants import Constants
import pygame

class Button:
    """
    Button reusable class used to implement the 2 GUI buttons in the app

    Attributes
    ----------
    text : str
        the text displayed on the button
    pos : tuple[int]
        the x and y position of the button
    size : tuple[int]
        the x and y dimensions of the button
    font : str
        the string name of the font being used
    bg : tuple[int]
        the rgb color of the default background color for button
    hovered_bg : tuple[int]
        the rgb color of the hovered button

    Methods
    -------
    draw(window):
        the draw method to display the button object on screen (called on every frame)
    click():
        the method that checks whether the button has been pressed (called on every frame)
    """

    def __init__(self, text: str, pos: Tuple[int], size: Tuple[int], font: str, bg: Tuple[int], hovered_bg: Tuple[int]) -> None:
        """
        Constructor function that initialises all the parameters needed by a Button object

            Parameters:
                    text (str): the text shown on the button
                    pos (tuple[int]): the tuple containing the x and y positions of the button
                    size (tuple[int]): the tuple containing the x and y dimensions of the button
                    font (str): the string name of the font being used
                    bg (tuple[int]): the rgb color of the normal button background
                    hovered_bg (tuple[int]): the rgb color of the hovered button background
        """
        self._x, self._y = pos 
        self._font = pygame.font.SysFont(font, Constants.BTN_FONT_SIZE)
        self._font.bold = True  # Set the font to bold by default
        self._text = text
        self._size = size
        self._surface = pygame.Surface(size)
        self._bgcolor = bg  # Button color
        self._hoveredColor = hovered_bg  # Button color for hover effect

    def draw(self, window: pygame.display):
        """
        Function that draws the button object to the pygame window

            Parameters:
                    window (pygame.display): the pygame window object
        """

        x, y = pygame.mouse.get_pos()
        
        if (x >= self._x and x <= self._x + self._size[0]) and \
            (y >= self._y and y <= self._y + self._size[1]):
            # The mouse is inside the button, so hover color
            self._surface.fill(self._hoveredColor)
        else:
            self._surface.fill(self._bgcolor)

        text_lines = self._text.splitlines()
        for i, l in enumerate(text_lines):
            font_text = self._font.render(l, 1, Colors.BLACK)
            self._surface.blit(font_text, (self._size[0]/2 - font_text.get_size()[0] / 2, 
                                           self._size[1]/2 - font_text.get_size()[1] + Constants.BTN_FONT_SIZE * i))

        window.blit(self._surface, (self._x, self._y))

    def click(self):
        """
        Function that checks whether the button has been clicked

            Returns:
                    (bool): whether or not the button has been clicked on
        """
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:

            if (x >= self._x and x <= self._x + self._size[0]) and \
               (y >= self._y and y <= self._y + self._size[1]):
               # The mouse is inside the button
               return True
        
        return False
