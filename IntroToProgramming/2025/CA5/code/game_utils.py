import turtle
from draw_pieces import draw_rook, draw_king, draw_queen, draw_bishop, draw_knight, draw_pawn
from draw_utils import draw_square
from utils import get_tile_size, get_screen, conv_spos
from state import get_state, update_state

color = ["#779556", "white"]  # Colours of the board, colours from Chess.com

t_h = get_tile_size()  # Get the tile height
prev_loc = (8.5, 3.502)  # the default location for preview


def move_piece(pos):
    """
    Places a piece at specificed position

    :param (int, int) (x, y): game-space coords
    """
    x, y = pos  # unpack pos into x and y

    loc, hand, current, board = get_state()  # Get state data from main loop
    if not hand:  # If there is nothing in the hand
        hand = board[y][x][0]  # Set the hand to the piece thats located there
        loc = (x, y)  # Set the position of this piece

        remove_piece(loc)  # remove the piece from the board -- visual

    elif hand:  # If a piece is in the hand
        p, q = loc  # unpack loc / prev loc into p and q
        same_color = board[q][p][1] == board[y][x][1]  # check if its the same colour
        same_pos = (p, q) == (x, y)  # Check if the previous location is the same as the current mouse click

        if not same_color:
            remove_piece((x, y))  # Remove the piece at its new location

            place_piece(hand, pos, board[q][p][1])  # Put the piece down

            # Swap the current player colour
            # if current == "white":
            #     current = "black"
            # else:
            #     current = "white"

            #### Update the board
            board[y][x] = board[q][p]  # put the current piece in the previous position to the new position
            board[q][p] = ("", "")  # 0 out the previous position
            ####

            hand = ""  # Reset the hand after placing a piece
            remove_piece(loc)  # Remove the previous piece

        elif same_pos:
            # Must be checked before colour
            # because there are multiple pieces that are the same colour
            # but only 1 with the same position

            #### Logic to put the piece down if its the same position
            place_piece(hand, loc, board[q][p][1])  # Put the piece down
            hand = ""  # reset the hand
            ####

        elif same_color:
            #### Logic to swap the piece if its the same colour
            place_piece(hand, loc, board[q][p][1])  # Put the piece down

            hand = board[y][x][0]  # Set the hand to the piece thats located there
            loc = (x, y)  # Set the position of this piece
            remove_piece(loc)  # remove the piece from the board -- visual
            ####

    preview(hand, board[y][x][1])  # update the preview square

    # Update the state of the game with all the changed values
    update_state(loc, hand, current, board)


def remove_piece(pos):
    """
    Removes the piece at the location
    :param (int, int) (x, y): game coords
    """
    x, y = pos  # unpack pos into x and y

    # 0.01 is to account for the boarder
    draw_square(x, y - 0.01, t_h, color[(y + x) % 2])  # Draw a square at that location with the correct colour


def preview(piece, _color):
    """
    Adds a preview to the current piece in the hand

    :param str piece:
    :param str color:
    """
    draw_square(prev_loc[0], prev_loc[1], t_h, "#A4A4A4")  # Clear the position
    if piece:
        # Add 0.1 because of the border
        place_piece(piece, (prev_loc[0], prev_loc[1] + 0.1), _color)  # Call the place piece function
    else:
        draw_square(prev_loc[0], prev_loc[1], t_h, "#A4A4A4")  # Clear the position


def place_piece(piece, pos, _color):
    # Place a piece with a switch statement

    match piece:  # A match case to switch between different pieces

        # Draw the piece at the location and use the correct colour
        case "rook":
            draw_rook(pos, _color)
        case "knight":
            draw_knight(pos, _color)
        case "queen":
            draw_queen(pos, _color)
        case "bishop":
            draw_bishop(pos, _color)
        case "king":
            draw_king(pos, _color)
        case "pawn":
            draw_pawn(pos, _color)


def render_board():
    """
    Render the board
    """
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing

    # This is the preview area, it should be on the right hand side of the board
    draw_square(prev_loc[0], prev_loc[1], t_h, "#A4A4A4")  # Clear the position
    #### Add some font to the hand
    t = turtle.Turtle()
    t.hideturtle()  # Hide the turtle cursor
    x, y = conv_spos((prev_loc[0], prev_loc[1] + 1))  # Convert game space co-ordinate to screen space
    t.penup()  # Lift pen up
    t.setx(x)  # Set x position of cursor
    t.sety(y)  # Set y position of cursor
    t.color("green")  # make the pen colour green
    t.write("Hand", font=("Times New Roman", 12, "normal"))  # Write 'hand' to screen
    ####

    _, height = get_screen()  # Get screen size
    border_s = 4  # Border size in 'px'
    # 200 comes from 2 * 100, half the border size converted to a percentage
    draw_square(-(border_s / 200), -(border_s / 200), height + border_s, "black")  # Draw a border around the board

    _, _, _, board = get_state()  # Get the game state

    # 8x8 matrix for loop, uses game space co-ordinates
    for x in range(0, 8):  # This will iterate over all columns
        for y in range(0, 8):  # This will iterate over all rows
            # (y + x) % 2 swaps between 0 and 1, which are the 2 colours of the baord
            draw_square(x, y, t_h, color[(y + x) % 2])  # draw the square and swap colours
            piece = board[y][x][0]  # get the piece that should be there
            _color = board[y][x][1]  # Get the colour that the piece should be
            place_piece(piece, (x, y), _color)  # place_piece at that position and with the correct colour
