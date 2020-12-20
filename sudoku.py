import time
import os

import frontend
import backend

import menu_page
import classic_menu_page
import classic_game_page
import diagonal_menu_page
import diagonal_game_page


# when packaging this .py file to .exe file,
# include --hidden-import: jinxed.terminfo.vtwin10


def main():

    play = True
    while play:

        frontend.clear_screen()
        user_choice = menu_page.open_menu_page()

        # defaults
        puzzle_name = "easy01.sud"
        puzzle_location = backend.get_file_location("classic_puzzles", puzzle_name)

        # goes to classic game menu page
        if user_choice == "C":

            frontend.clear_screen()
            puzzle_name = classic_menu_page.open_classic_page()

        # goes to diagonal game menu page
        elif user_choice == "D":

            frontend.clear_screen()
            puzzle_name = diagonal_menu_page.open_diagonal_page()

        # quits game
        elif user_choice == "Q":
            break

        # plays a game of classic or diagonal sudoku

        if user_choice == "C":
            classic_game_page.play_classic_game(puzzle_name)

        elif user_choice == "D":
            diagonal_game_page.play_diagonal_game(puzzle_name)

        play = frontend.get_user_play_decision()

    frontend.clear_screen()
    frontend.show_end_message()
    time.sleep(1.5)


if __name__ == "__main__":
    os.system("mode con cols=100 lines=40")
    main()
