# Python Sudoku Solver using Backtracking

from view.gui import GUI
import pygame

def main() -> None:
    """Client function that runs the program"""
    game = GUI()
    game.main()
    pygame.quit()

if __name__ == "__main__":
    main()