import frontend
from blessed import Terminal
from colors import Color

# TODO: handling invalid inputs without scrolling down
# TODO: function that locks size of terminal

dog = '''
     |\_/|                     
     | o o   Hi there!         
     |   <>              _     
     |  _/\------____ ((| |))  
     |               `--' |    
 ____|_       ___|   |___.'    
/_/_____/____/_______|         
'''


def get_main_menu_input():

    term = Terminal()

    # then centralizes input by adding half the length of terminal using blank spaces
    term_width = term.width

    blank = ""
    for _ in range(int(term_width/2)):
        blank = blank + " "

    input_choice = ""

    input_condition = False
    while not input_condition:
        print()
        print(term.center("                   What do you want to do?                  "))
        print(blank, end="")
        input_choice = input().strip().capitalize()

        if input_choice in ["C", "D", "Q"]:
            input_condition = True
        else: 
            print(term.center(Color.RED + "                 Error. Input Valid Choice.                 " + Color.END))

    return input_choice


def show_menu():
    term = Terminal()
    print()
    frontend.center_multiline_string(dog)
    print()
    print("\n")
    print(term.center("                         Main Menu                          \n"))
    print(term.center("                   > Classic Mode   [C] <                   "))
    print(term.center("                   > Diagonal Mode  [D] <                   "))
    print(term.center("                   > Quit Game      [Q] <                   \n\n"))


def open_menu_page():
    term = Terminal()

    frontend.show_title("Sudoku")
    frontend.show_divider_line()
    show_menu()
    frontend.show_divider_line()
    user_input = get_main_menu_input()

    return user_input
