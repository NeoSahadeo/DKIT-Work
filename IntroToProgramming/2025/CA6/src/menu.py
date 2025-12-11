import copy

# \033 is the ESC button
# [..m are delimeters
# and the numbers in between are the
# ansi codes
# eg: \033[32m which is green


SEPERATOR = '-'  # Stores what the seperator should look like
MENU_OPTIONS = [  # Store the menu options, able to change the list dynamically
    "Deposit the Monies",
    "Withdraw the Monies",
    "Check the Monies Balance",
    "Exit"
]
# Get the largest length in the menu to calculate the correct size to draw the box
# Copy the value so that I can keep the original order of the list
menu_sorted = copy.deepcopy(MENU_OPTIONS)
menu_sorted.sort()
MENU_LEN = len(menu_sorted[0]) + 10

# DEFAULT COLOR
DEFAULT_COLORS = "\033[1;30;47m"


# Take in a string, ansi, and if there should be a new line
# i did provide default values to save myself time
def log(string, ansi="", new_line=True):
    """
    Create a 'log' function that takes the place of print
    so I can include the end ANSI without typing it in
    every-time
    """

    if new_line:
        # Pad the string with spaces to avoid missing blocks
        string = f"{string: <{MENU_LEN}}"
        print(ansi + string + "\033[0m")
    else:
        print(ansi + string + "\033[0m", end='')


def print_border():
    """
    Small function to do this repeated task of print the border
    """
    log(SEPERATOR * MENU_LEN, "\033[40m")  # Print the board with black


def print_menu():
    """
    Print out the user_interface menu in a ~pulchritudinous~ way!

    https://duckduckgo.com/?t=ffab&q=pulchritudinous&ia=web
    """
    # Print statemtns for the menu
    print_border()
    log("Bank of Neo", DEFAULT_COLORS)
    log("We put the i in interest!", "\033[3;30;47m")

    print_border()
    log("Menu: ", DEFAULT_COLORS)
    for index, value in enumerate(MENU_OPTIONS):  # Using enumerate so I get the index value back
        log(f"{index + 1}) " + value, "\x1b[30;47m")  # I add 1 to the index so that the menu starts at 1

    print_border()
