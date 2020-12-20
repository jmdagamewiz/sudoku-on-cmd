import os
from colors import Color
from blessed import Terminal


def center_multiline_string(multiline_string):

    # need to split into multiple lines first
    for string in multiline_string.splitlines():
        print(Terminal().center(string))


def clear_screen():
    os.system("cls")


def show_divider_line():

    print(Terminal().center("============================================================"))


def show_title(string):

    # from ASCII text generator @ https://ascii.co.uk/text
    # ASCII font named Doom

    title = ""
    if string == "Sudoku":
        title = '''
 _____           _       _          
/  ___|         | |     | |         
\ `--. _   _  __| | ___ | | ___   _ 
 `--. \ | | |/ _` |/ _ \| |/ / | | |
/\__/ / |_| | (_| | (_) |   <| |_| |
\____/ \__,_|\__,_|\___/|_|\_\\\\__,_|
        '''
    elif string == "Classic Mode":
        title = '''
 _____ _               _       ___  ___          _      
/  __ \ |             (_)      |  \/  |         | |     
| /  \/ | __ _ ___ ___ _  ___  | .  . | ___   __| | ___ 
| |   | |/ _` / __/ __| |/ __| | |\/| |/ _ \ / _` |/ _ \\
| \__/\ | (_| \__ \__ \ | (__  | |  | | (_) | (_| |  __/
 \____/_|\__,_|___/___/_|\___| \_|  |_/\___/ \__,_|\___|
        '''
    elif string == "Diagonal Mode":
        title = '''
______                                 _  ___  ___          _      
|  _  (_)                             | | |  \/  |         | |     
| | | |_  __ _  __ _  ___  _ __   __ _| | | .  . | ___   __| | ___ 
| | | | |/ _` |/ _` |/ _ \| '_ \ / _` | | | |\/| |/ _ \ / _` |/ _ \\
| |/ /| | (_| | (_| | (_) | | | | (_| | | | |  | | (_) | (_| |  __/
|___/ |_|\__,_|\__, |\___/|_| |_|\__,_|_| \_|  |_/\___/ \__,_|\___|
                __/ |                                              
               |___/                                               
        '''
    else:
        raise ValueError("Passed argument must be valid.")

    center_multiline_string(title)


def show_start_message(puzzles_list):

    print("this is a sudoku game.\n")
    print("here are all the levels you can play:\n")

    print("Easy")
    for file in puzzles_list[0]:
        print("\t" + file)

    print("Medium")
    for file in puzzles_list[1]:
        print("\t" + file)

    print("Hard")
    for file in puzzles_list[2]:
        print("\t" + file)


def get_puzzle_name_input(puzzles_list):

    input_condition = False

    # default puzzle choice
    puzzle_name = "easy01.sud"

    while not input_condition:
        puzzle_name = input("\ninput filename: ")

        if puzzle_name in puzzles_list:
            input_condition = True
        else:
            print(Color.RED + "error. available file only." + Color.END)

    return puzzle_name


def get_value_input():

    input_num = None
    input_condition = False
    while not input_condition:
        try:
            print("input 0 to erase.")
            input_num = int(input("what would you like to input? "))

            if 1 <= input_num <= 9:
                input_condition = True
            elif input_num == 0:
                print(Color.UNDERLINE + "erasing an input.\n" + Color.END)
                input_condition = True
            else:
                print(Color.RED + "error. integers from 1 to 9 only.\n" + Color.END)

        except ValueError:
            print(Color.RED + "error. integer input only.\n" + Color.END)

    return str(input_num)


def get_position_input(grid):
    column = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    row = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    input_condition = False
    while not input_condition:
        position = input("where would you like to put this? ").strip()

        if len(position) == 2:

            x = position[0]
            y = position[1]

            # checking if given position format is correct
            if x in column and y.lower() in row:

                x = int(x) - 1
                y = row.index(y.lower())

                if Color.CYAN not in grid[y][x]:
                    return [x, y]
                else:
                    print(Color.RED + "Error. Position has given.\n" + Color.END)

            else:
                print(Color.RED + "Error. Input in form [digit from 1 to 9][letter from a to h] only.\n" + Color.END)
        else:
            print(Color.RED + "Error. 2 character input only.\n" + Color.END)


def show_puzzle_name(puzzle_name):
    print("\n\tlevel: {}\n".format(puzzle_name))


def show_puzzle(grid):

    term = Terminal()

    print(term.center("         1   2   3    4   5   6    7   8   9       "))
    print(term.center("       +-------------------------------------+     "))
    print(term.center("    a  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[0][0], grid[0][1], grid[0][2], grid[0][3],
                                                                         grid[0][4], grid[0][5], grid[0][6], grid[0][7],
                                                                         grid[0][8])))
    print(term.center("    b  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[1][0], grid[1][1], grid[1][2], grid[1][3],
                                                                         grid[1][4], grid[1][5], grid[1][6], grid[1][7],
                                                                         grid[1][8])))
    print(term.center("    c  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[2][0], grid[2][1], grid[2][2], grid[2][3],
                                                                         grid[2][4], grid[2][5], grid[2][6], grid[2][7],
                                                                         grid[2][8])))
    print(term.center("       +-------------------------------------+     "))
    print(term.center("    d  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[3][0], grid[3][1], grid[3][2], grid[3][3],
                                                                         grid[3][4], grid[3][5], grid[3][6], grid[3][7],
                                                                         grid[3][8])))

    print(term.center("    e  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[4][0], grid[4][1], grid[4][2], grid[4][3],
                                                                         grid[4][4], grid[4][5], grid[4][6], grid[4][7],
                                                                         grid[4][8])))
    print(term.center("    f  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[5][0], grid[5][1], grid[5][2], grid[5][3],
                                                                         grid[5][4], grid[5][5], grid[5][6], grid[5][7],
                                                                         grid[5][8])))
    print(term.center("       +-------------------------------------+     "))
    print(term.center("    g  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[6][0], grid[6][1], grid[6][2], grid[6][3],
                                                                         grid[6][4], grid[6][5], grid[6][6], grid[6][7],
                                                                         grid[6][8])))
    print(term.center("    h  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[7][0], grid[7][1], grid[7][2], grid[7][3],
                                                                         grid[7][4], grid[7][5], grid[7][6], grid[7][7],
                                                                         grid[7][8])))
    print(term.center("    i  | {} | {} | {} || {} | {} | {} || {} | {} | {} |     ".format(grid[8][0], grid[8][1], grid[8][2], grid[8][3],
                                                                         grid[8][4], grid[8][5], grid[8][6], grid[8][7],
                                                                         grid[8][8])))
    print(term.center("       +-------------------------------------+     "))


def show_checking_message():

    term = Terminal()

    print()
    print(term.center("                        Checking....                        \n"))
    print()


def show_greetings(greeting):

    greeting_ascii = ""

    if greeting == "Congratulations":

        # from ASCII text generator @ https://ascii.co.uk/text
        # ASCII font named Doom

        greeting_ascii = '''
 _____                             _         _       _   _                 
/  __ \                           | |       | |     | | (_)                
| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \\
 \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                    __/ |                                                  
                   |___/                                                   
        '''

    elif greeting == "Try Again":

        # from ASCII text generator @ https://ascii.co.uk/text
        # ASCII font named Doom

        greeting_ascii = '''
 _____             ___              _       
|_   _|           / _ \            (_)      
  | |_ __ _   _  / /_\ \ __ _  __ _ _ _ __  
  | | '__| | | | |  _  |/ _` |/ _` | | '_ \ 
  | | |  | |_| | | | | | (_| | (_| | | | | |
  \_/_|   \__, | \_| |_/\__, |\__,_|_|_| |_|
           __/ |         __/ |              
          |___/         |___/               
        '''

    center_multiline_string(greeting_ascii)
    print()


def show_mistakes_message(mistakes):

    if mistakes == 0:
        show_greetings("Congratulations")

    else:
        show_greetings("Try Again")


def get_user_play_decision():

    term = Terminal()
    term_width = term.width

    blank = ""
    for _ in range(int(term_width / 2) - 2):
        blank = blank + " "

    input_condition = False

    while not input_condition:
        print()
        print(term.center("                 Go to Main Menu? [yes/no]                  "))
        print(blank, end="")
        player_input = input().strip()

        if player_input == "yes":
            input_condition = True
            return True
        elif player_input == "no":
            input_condition = True
            return False
        else:
            print(term.center(Color.RED + "                 Error. Input valid choice.                 " + Color.END))


def show_end_message():
    term = Terminal()

    term_width = term.width

    blank = ""
    for _ in range(int(term_width / 2) - 2):
        blank = blank + " "

    thank_you = '''
 _____ _                 _     __   __          
|_   _| |               | |    \ \ / /          
  | | | |__   __ _ _ __ | | __  \ V /___  _   _ 
  | | | '_ \ / _` | '_ \| |/ /   \ // _ \| | | |
  | | | | | | (_| | | | |   <    | | (_) | |_| |
  \_/ |_| |_|\__,_|_| |_|_|\_\   \_/\___/ \__,_|
    '''
    center_multiline_string(thank_you)
    print()
    print(term.center("              Thank you for playing the game!               "))
    print(term.center("                      Game closing...                       "))
