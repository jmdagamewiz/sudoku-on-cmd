import frontend
import backend
import time
from blessed import Terminal
from colors import Color


def get_value_input():

    term = Terminal()

    input_num = None
    input_condition = False

    term_width = term.width

    blank = ""
    for _ in range(int(term_width / 2)):
        blank = blank + " "

    while not input_condition:
        try:
            print(term.center("                     Input 0 to erase.                     "))
            print(term.center("               What would you like to input?               "))
            print(blank, end="")
            input_num = int(input())

            if 1 <= input_num <= 9:
                input_condition = True
            elif input_num == 0:
                print(term.center(Color.UNDERLINE + "                     Erasing an input.                     \n" + Color.END))
                input_condition = True
            else:
                print(term.center(Color.RED + "             Error. integers from 1 to 9 only.              \n" + Color.END))

        except ValueError:
            print(term.center(Color.RED + "                 Error. integer input only.                 \n" + Color.END))

    return str(input_num)


def get_position_input(grid):
    column = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    row = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    term = Terminal()

    term_width = term.width

    blank = ""
    for _ in range(int(term_width / 2)):
        blank = blank + " "

    input_condition = False
    while not input_condition:

        print(term.center("             Where would you like to put this?              "))
        print(blank, end="")
        position = input().strip()

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
                    print(term.center(Color.RED + "                 Error. position has given.                 \n" + Color.END))

            else:
                print(term.center(Color.RED + "        Error. input in form [1 to 9][a to h] only.         \n" + Color.END))
        else:
            print(term.center(Color.RED + "               Error. 2 character input only.               \n" + Color.END))


def show_diagonal_game(puzzle_name, puzzle_grid):
    term = Terminal()

    blanks = backend.count_blank(puzzle_grid)

    while blanks > 0:

        frontend.clear_screen()

        frontend.show_title("Diagonal Mode")
        frontend.show_divider_line()

        print()
        print(term.center("Level: " + puzzle_name))
        print()

        frontend.show_puzzle(puzzle_grid)

        print()
        frontend.show_divider_line()
        print()

        value_input = get_value_input()
        position_input = get_position_input(puzzle_grid)
        puzzle_grid = backend.put_to_grid(value_input, position_input, puzzle_grid)

        blanks = backend.count_blank(puzzle_grid)

    frontend.clear_screen()

    frontend.show_puzzle(puzzle_grid)

    puzzle_grid = backend.decolorize_grid(puzzle_grid)

    frontend.show_checking_message()
    time.sleep(1)
    frontend.clear_screen()

    answer_grid_name = backend.get_puzzle_answer_name(puzzle_name)
    answer_location = backend.get_file_location("diagonal_puzzles_answers", answer_grid_name)
    answer_string = backend.get_file_string(answer_location)
    answer_grid = backend.get_grid(answer_string)

    checked_grid = backend.get_checked_grid(puzzle_grid, answer_grid)
    mistakes = backend.count_mistakes(checked_grid)

    frontend.clear_screen()

    frontend.show_mistakes_message(mistakes)
    frontend.show_puzzle(checked_grid)


def play_diagonal_game(puzzle_name):

    # gets puzzle and puts into grid (2d list)
    puzzle_location = backend.get_file_location("diagonal_puzzles", puzzle_name)
    puzzle_string = backend.get_file_string(puzzle_location)

    puzzle_grid = backend.get_grid(puzzle_string)
    puzzle_grid = backend.colorize_grid(puzzle_grid, Color.CYAN)

    show_diagonal_game(puzzle_name, puzzle_grid)
