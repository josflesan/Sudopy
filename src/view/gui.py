# GUI that displays the sudoku board

from model.board import Board
from model.button import Button
from model.colors import Colors
from controller.solver import *
from controller.generate import generate_board
import pygame
import time

from model.constants import Constants

class GUI:
    """
    Class modelling the GUI for the app

    Methods
    -------
    auto_solve(window, board, time, strikes):
        visualizer function that animates the backtracking algorithm
    redraw_window(window, board, time, strikes):
        function that updates the display in each frame
    format_time(secs):
        helper function to format the time as provided by time module
    main():
        main function that initialises pygame and handles events
    """

    RUN = True

    def auto_solve(self, window: pygame.display, board: Board, time: time.time, strikes: int, buttons: Tuple[Button]) -> None:
        """
        Visualizer function that animates the backtracking algorithm

            Parameters:
                    window (pygame.display): the pygame window
                    board (Board): the board object
                    time (time.time): the play time
                    strike (int): number of strikes the user has
            
            Returns:
                    (bool): flag indicating whether or not a particular moves yields a potential solution
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GUI.RUN = False
                return True  # Exit this loop (solution is to end program)
        
        empty_cell = find_empty(board.model)
        if not empty_cell:
            return True  # Stop backtracking, sudoku board solved
        else:
            row, col = empty_cell

        for i in range(1, 10):
            if check_valid(board.model, i, (row, col)):
                board.cells[row][col].num = i
                board.model[row][col] = i
                board.cells[row][col].incorrect = False
                board.cells[row][col].correct = True
                pygame.time.delay(50)
                self.redraw_window(window, board, time, strikes, buttons)

                if self.auto_solve(window, board, time, strikes, buttons):
                    return True

                board.cells[row][col].incorrect = True
                board.cells[row][col].correct = False
                self.redraw_window(window, board, time, strikes, buttons)
                pygame.time.delay(50)
                board.cells[row][col].num = 0
                board.model[row][col] = 0


    def redraw_window(self, window: pygame.display, board: Board, time: time.time, strikes: int, buttons: Tuple[Button]) -> None:
        """
        Function that redraws the window with all the updated information after interaction

            Parameters:
                    window (pygame.display): The window object as supplied by pygame
                    board (Board): The board object
                    time (time.time): The current time as provided by time
                    strikes (int): The number of strikes the user has
        """
        window.fill(Colors.WHITE)  # Clear screen
        # Draw time
        fnt = pygame.font.SysFont(Constants.FONT, Constants.FONT_SIZE)
        text = fnt.render("Time: " + self.format_time(time), 1, Colors.BLACK)
        window.blit(text, (Constants.WIN_WIDTH-270, Constants.WIN_HEIGHT - 40))
        # Draw strikes
        text = fnt.render("X " * strikes, 1, Colors.RED)
        window.blit(text, (20, Constants.WIN_HEIGHT - 40))
        # Draw grid and board
        board.draw(window)
        # Draw buttons
        for button in buttons:
            button.draw(window)
        pygame.display.update()

    def format_time(self, secs: int) -> str:
        """
        Helper function that formats the time received by time module

            Parameters:
                    secs (int): The time in seconds as supplied by time module
                
            Returns:
                    (str): Formatted string representation of time elapsed
        """
        sec = secs%60
        minute = secs//60
        hour = minute//60

        mat = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2)
        return mat

    def main(self) -> None:
        """Main GUI function that initialises and handles all of the pygame logic"""
        pygame.font.init()
        window = pygame.display.set_mode(Constants.WIN_DIMENS)  # Create the window
        pygame.display.set_caption(Constants.APP_TITLE)  # Set the window title
        board = Board(9, 9, 540, 540)
        key = None  # The key pressed
        start = time.time()  # The starting time upon opening the app
        strikes = 0  # The number of strikes the user has

        # Instantiate both buttons
        generateSudokuBtn = Button("GENERATE SUDOKU\nBOARD", (20, 50), (230, 75), Constants.FONT, Colors.BOARD_BUTTON_BG, Colors.BOARD_BUTTON_HOVER)
        autoSolveSudokuBtn = Button("AUTO SOLVE\nBOARD", (Constants.WIN_WIDTH - 250, 50), (230, 75), Constants.FONT, Colors.SOLVE_BUTTON_BG, Colors.SOLVE_BUTTON_HOVER)

        while GUI.RUN:

            play_time = round(time.time() - start)  # The time elapsed since the game started, recalculated every frame

            # Keyboard event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GUI.RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    # Clearing cell logic
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        board.clear()
                        key = None
                    # Running visualization logic
                    if event.key == pygame.K_SPACE:
                        self.auto_solve(window, board, play_time, strikes, [generateSudokuBtn, autoSolveSudokuBtn])
                    # Committing number to cell logic
                    if event.key == pygame.K_RETURN:
                        i, j = board.selected
                        if board.cells[i][j].tempNum != 0:
                            if board.insert_num(board.cells[i][j].tempNum):
                                print("Success")  # Debug success message
                            else:
                                print("Wrong")  # Debug wrong message
                                strikes += 1
                            key = None
                            
                            # Logic to handle end of the game
                            if board.is_finished():
                                print("Game Over")
                                GUI.RUN = False
                
                # Mouse Click Event Logic
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Check if the buttons were clicked
                    for button in [generateSudokuBtn, autoSolveSudokuBtn]:
                        if button.click():  # If the buttons have been clicked

                            if button == generateSudokuBtn:
                                new_board = generate_board()  # Create a new board
                                board.model = new_board  # Update the model being used by the board
                                board.update_board()
                                self.redraw_window(window, board, play_time, strikes, (generateSudokuBtn, autoSolveSudokuBtn))
                                pygame.display.update()              
                                
                            elif button == autoSolveSudokuBtn:
                                self.auto_solve(window, board, play_time, strikes, [generateSudokuBtn, autoSolveSudokuBtn])

                    clicked = board.click(pos)
                    if clicked:
                        board.select(clicked[0], clicked[1])
                        key = None


            # If the cell is selected and key has been pressed, add a note
            if board.selected and key != None:
                board.add_note(key)

            # If the user has made 3 mistakes, end the game
            if strikes == 3:
                print("Game Over")
                GUI.RUN = False

            # Redraw the window in each frame and update the pygame display
            self.redraw_window(window, board, play_time, strikes, (generateSudokuBtn, autoSolveSudokuBtn))
            pygame.display.update()               
                    