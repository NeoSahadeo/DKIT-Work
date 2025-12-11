from draw_utils import draw_poly, draw_text
from game_utils import move_piece
from utils import conv_spos, conv_gpos

button_events = []  # A list of all registered button events


def button(x, y, t_x, t_y, width, height, text, color, type, size, func):
    """
    Create a button

    :param int x: poly pos-x
    :param int y: poly pos-y
    :param int t_x: text pos-y
    :param int t_y: text pos-y
    :param int width: poly width
    :param int height: poly height
    :param str text:
    :param str color:
    :param str type:
    :param int size:
    :param function func: Callback function
    """
    draw_poly(x, y, width, height, color)  # Draw a bounding box
    draw_text(t_x, t_y, text, size, type)  # Add text to the bounding box

    p, q = conv_spos((x, y))  # Convert the x and y game-space positions to screen-space to avoid rounding errors
    button_events.append((p, width + p, q, height + q, func))  # Append this event to the list. Include a callback function for it to do something
    # width + p and height + q will be the bounding box of the polygon
    # this allows me to figure out if that button was clicked or not.


def handle_click(x, y):
    """
    INTERNAL USE ONLY
    Binds mouse position clicks to a function call

    :param int x:
    :param int y:
    """
    for minx, maxx, miny, maxy, func in button_events:  # Iterate over the button event list and unpack the values
        if (maxx >= x and x >= minx) and (maxy >= y and y >= miny):  # Check if the click was within the bounds of the element
            func()  # Execute the callback function if its true
            return  # Return to exit function so it doesnt execute any other code

    p, q = conv_gpos((x, y))  # Convert click to game space coords

    if p >= 0 and p <= 7 and q <= 7 and q >= 0:  # Place the pieces only in the board
        move_piece((p, q))  # Call the place piece function
        return  # Return to exit function so it doesnt execute any other code
