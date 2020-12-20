import frontend
from blessed import Terminal
from colors import Color
import backend

cat = '''
      |\      _,,,---,,_      
ZZZzz /,`.-'`'    -.  ;-;;,_  
     |,4-  ) )-,_. ,\ (  `'-' 
    '---''(_/--'  `-'\_)      
'''


def get_diagonal_menu_input():

    term = Terminal()

    # then centralizes input by adding half the length of terminal using blank spaces
    term_width = term.width

    blank = ""
    for _ in range(int(term_width/2) - 5):
        blank = blank + " "

    puzzles_list = backend.get_folder_file_list("diagonal_puzzles")

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


def show_diagonal_menu():
    term = Terminal()

    print()
    print()
    frontend.center_multiline_string(cat)
    print()
    print()
    print(term.center("                        Diagonal Mode                       \n"))
    print()
    print(term.center("                       diagonal01.sud                       "))
    print(term.center("                       diagonal02.sud                       "))
    print(term.center("                       diagonal03.sud                       "))
    print(term.center("                       diagonal04.sud                       "))
    print(term.center("                       diagonal05.sud                       \n"))


def open_diagonal_page():
    frontend.show_title("Sudoku")
    frontend.show_divider_line()
    show_diagonal_menu()
    frontend.show_divider_line()
    user_input = get_diagonal_menu_input()

    return user_input
