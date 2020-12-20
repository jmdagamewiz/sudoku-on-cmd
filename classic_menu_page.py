import frontend
from blessed import Terminal
from colors import Color
import backend


ducks = '''
  _          _          _          _         
>(')____,  >(')____,  >(')____,  >(')____,   
  (` =~~/    (` =~~/    (` =~~/    (` =~~/   
~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~^`---'~^~
'''


def get_classic_menu_input():

    term = Terminal()

    # then centralizes input by adding half the length of terminal using blank spaces
    term_width = term.width

    blank = ""
    for _ in range(int(term_width/2) - 5):
        blank = blank + " "

    puzzles_list = backend.get_folder_file_list("classic_puzzles")

    input_choice = ""

    input_condition = False
    while not input_condition:
        print()
        print(term.center("                 What do you want to play?                  "))
        print(blank, end="")
        input_choice = input().strip()

        if input_choice in puzzles_list:
            input_condition = True
        else:
            print(term.center(Color.RED + "                 Error. Input Valid Choice.                 " + Color.END))

    return input_choice


def show_classic_menu():
    term = Terminal()

    print()
    print()
    frontend.center_multiline_string(ducks)
    print()
    print()
    print(term.center("                        Classic Mode                        "))
    print()
    print(term.center("         Easy              Medium              Hard         "))
    print()
    print(term.center("      easy01.sud        medium01.sud        hard01.sud      "))
    print(term.center("      easy02.sud        medium02.sud        hard02.sud      "))
    print(term.center("      easy03.sud        medium03.sud        hard03.sud      "))
    print(term.center("      easy04.sud        medium04.sud        hard04.sud      "))
    print(term.center("      easy05.sud        medium05.sud        hard05.sud      \n"))


def open_classic_page():
    frontend.show_title("Sudoku")
    frontend.show_divider_line()
    show_classic_menu()
    frontend.show_divider_line()
    user_input = get_classic_menu_input()

    return user_input

