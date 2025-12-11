import math
import turtle

# The General Convertion:
# Take in x and y (game-space)
# add an offset to move to bottom-left of screen (offset is ((width|height) / 2 ))
# Multiply the x and y by 8 because there are 8 tiles in a chess axis
# And vice-versa

#### Padding Size
PADDING_X = 0.1  # Width padding percent
PADDING_Y = 0.1  # Height padding percent
####


def get_screen():
    """
    Returns the screen size
    :return (int, int) width, height:
    """
    screen = turtle.Screen()  # Create instance of the screen Object.

    # Calls the width and height method to get those values
    width = screen.window_width()
    height = screen.window_height()
    ####

    # Subtract padding from screen size on both sides; thats why its multiplied by 2
    return (width - width * PADDING_X * 2, height - height * PADDING_Y * 2)  # Return the result as a tuple


def get_tile_size():
    """
    Returns the tile height based on the screen size
    :return int height:
    """
    _, height = get_screen()  # Unpack the tuple and discard the width

    # divide by 8 because that is how many tiles are in a chess axis
    # only return the height so the user can see the entire board without the
    # need to scroll
    return math.floor(height / 8)  # This should be an individual tile size


def conv_gpos(pos):
    """
    Convert screen space position to game space position.
    8x8 game space

    :param (int, int) pos: Tuple containing screen space co-ordinates
    :return (int, int): Tuple containing game space co-ordinates
    """
    width, height = get_screen()  # Tuple unpack height and width

    x, y = pos  # tuple unpack into x and y

    # Equation:
    # floor([x / (h)] * 8) = y

    # Added padding on both axis to account for the conversion
    # at each position so that the bottom-left starts are 0,0
    # instead of whatever the updated value is for the padding size
    return (math.floor(((PADDING_X * width + x + (width / 2)) / height) * 8), math.floor(((PADDING_Y * height + y + (height / 2)) / height) * 8))  # convertion equation


def conv_spos(pos):
    """
    Convert game space position to screen space position.

    :param (int, int) pos: Tuple containing game space co-ordinates
    :return (int, int): Tuple containing screen space co-ordinates
    """
    width, height = get_screen()  # Tuple unpack height and width

    x, y = pos  # tuple unpack into x and y

    # Convert a game space co-ordinate to a screen space co-ordinate
    return (-(width / 2) + ((height * x) / 8) - PADDING_X * width, -(height / 2) + ((height * y) / 8) - PADDING_Y * height)
    # Chose to scale the board of the height of the user's display
    # Also subtract of the padding to account for right side padding
