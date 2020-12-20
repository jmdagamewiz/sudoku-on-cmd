import glob
import os
from colors import Color


def get_folder_file_list(folder_name):

    folder_location = folder_name + "/*.sud"
    file_list = glob.glob(folder_location)

    for index in range(len(file_list)):
        file_list[index] = os.path.basename(file_list[index])

    return file_list


def get_file_location(folder_location, file_name):
    return folder_location + "/" + file_name


def get_file_string(file_location):
    file_string = open(file_location, "r").read()

    final_string = ""

    for line in file_string:
        final_string = final_string + line.strip()

    return final_string


def get_puzzle_category_list(file_list):

    easy_list = []
    medium_list = []
    hard_list = []

    for file_name in file_list:
        if "easy" in file_name:
            easy_list.append(file_name)
        if "medium" in file_name:
            medium_list.append(file_name)
        elif "hard" in file_name:
            hard_list.append(file_name)

    return [easy_list, medium_list, hard_list]


def get_puzzle_answer_name(puzzle_name):
    return puzzle_name.replace(".sud", "") + "_answer.sud"


def get_grid(sudoku_string):
    grid = []

    j = 0
    row_string = ""

    for i in range(len(sudoku_string)):
        j = j + 1
        row_string = row_string + sudoku_string[i]

        if j == 9:
            row_list = list(row_string)

            for index in range(len(row_list)):
                if row_list[index] == ".":
                    row_list[index] = " "

            grid.append(row_list)
            row_string = ""
            j = 0

    return grid


def put_to_grid(value, position, grid):

    print(position)
    x = position[0]
    y = position[1]

    if value == "0":
        grid[y][x] = " "
    else:
        grid[y][x] = Color.GREEN + str(value) + Color.END

    return grid


def colorize_grid(grid, color):
    color_end = Color.END

    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] != " ":
                grid[y][x] = color + grid[y][x] + color_end

    return grid


def decolorize_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if Color.END in grid[y][x] or Color.UNDERLINE in grid[y][x]:
                grid[y][x] = grid[y][x].replace(Color.END, "")
                grid[y][x] = grid[y][x].replace(Color.UNDERLINE, "")

            if Color.CYAN in grid[y][x] or Color.GREEN in grid[y][x]:
                grid[y][x] = grid[y][x].replace(Color.CYAN, "")
                grid[y][x] = grid[y][x].replace(Color.GREEN, "")

            if Color.YELLOW in grid[y][x] or Color.RED in grid[y][x]:
                grid[y][x] = grid[y][x].replace(Color.YELLOW, "")
                grid[y][x] = grid[y][x].replace(Color.RED, "")

    return grid


# counts number of blanks in grid
def count_blank(grid):
    blanks = 0

    for grid_row in grid:
        for cell in grid_row:
            if cell == " ":
                blanks = blanks + 1

    return blanks


def get_checked_grid(puzzle_grid, answer_grid):

    puzzle_grid = decolorize_grid(puzzle_grid)
    answer_grid = decolorize_grid(answer_grid)

    for y in range(len(puzzle_grid)):
        for x in range(len(puzzle_grid[y])):

            if puzzle_grid[y][x] != answer_grid[y][x]:

                if puzzle_grid[y][x] == " ":
                    puzzle_grid[y][x] = "_"

                puzzle_grid[y][x] = Color.RED + puzzle_grid[y][x] + Color.END

            else:
                if puzzle_grid[y][x] == answer_grid[y][x]:
                    puzzle_grid[y][x] = Color.CYAN + puzzle_grid[y][x] + Color.END

    return puzzle_grid


def count_mistakes(checked_grid):

    mistakes = 0

    for y in range(len(checked_grid)):
        for x in range(len(checked_grid[y])):

            if Color.RED in checked_grid[y][x]:
                mistakes = mistakes + 1

    return mistakes


def fill_grid(puzzle_name, puzzle_grid):
    # USE puzzle_grid backend.fill_grid(puzzle_name, puzzle_grid) TO ACCESS FUNCTION

    answer_grid_name = get_puzzle_answer_name(puzzle_name)
    answer_location = get_file_location("puzzles_answers", answer_grid_name)
    answer_string = get_file_string(answer_location)
    answer_grid = get_grid(answer_string)

    for y in range(len(puzzle_grid)):
        for x in range(len(puzzle_grid)):
            puzzle_grid[y][x] = answer_grid[y][x]

    return answer_grid
