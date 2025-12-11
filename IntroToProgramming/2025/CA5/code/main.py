import turtle
import copy
from draw_utils import draw_text, draw_square, draw_poly
from game_utils import render_board
from utils import get_tile_size, conv_spos
from events import handle_click, button
from state import COLORS, PIECE_SCORE, get_state, base_board, update_state

t_h = get_tile_size()  # Get the tile size, t_h stands for tile height


def main():
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing

    # Add exit button
    button(7, 8.5, 7.3, 8.55, 100, 35, "Exit", "orange", "bold", 12, turtle.bye)

    #### Draw some text
    draw_text(0, 8.5, "Chess by Neo", 12, "bold")  # Add a small chess logo
    draw_text(0, 8.3, "Made with turtle", 8, "bold")  # Add an attribution
    ####

    #### Draws Board -> Initial
    render_board()  # Draw the board

    turtle.update()  # Update the screen


def restart():
    """
    Restart / start the function
    """
    loc, hand, current, _ = get_state()  # get the current state excluding the board

    # I use a deep copy to copy all sub structures in the list to a new memory location
    # because lists are pass-by-ref
    update_state(loc, hand, current, copy.deepcopy(base_board))  # Resets the board to initial position

    main()  # Update the board again
    turtle.onscreenclick(handle_click)  # Bind click events to the hand_click event handler

    turtle.ontimer(game_loop)  # Start a game loop


def game_loop():
    m, n = 0, 0  # set the values to 0
    for x in get_state()[-1]:  # loop through the board
        for y in x:
            if y[0]:  # check if the value is not empty
                if y[1] == COLORS[0]:  # sort color by score
                    m += PIECE_SCORE[y[0]]  # Calculate piece score p2
                else:
                    n += PIECE_SCORE[y[0]]  # Calculate piece score p1

    #### Draw the scores
    draw_square(8.4, 2, t_h, "white")  # Draw a white square over print location
    draw_square(8.4, 5, t_h, "white")  # Draw a white square over print location
    draw_text(8.5, 2.6, f"Player 1 score\n{n}", 10, "bold")  # print p1 score
    draw_text(8.5, 5, f"Player 2 score\n{m}", 10, "bold")  # print p2 score
    ####

    # If its either this means that the game should end because the king is dead
    if m < 0 or n < 0:  # Check if the score is a negative or 0

        #### Creates a reset button to restart the game
        draw_poly(2.5, 3.5, 300, 100, "green")  # Background for the win screen
        button(3.1, 3, 3.6, 3.1, 150, 50, "reset", "#31DE88", "bold", 12, restart)  # Create reset button
        ####

        t = turtle.Turtle()  # Create turtle instance
        t.hideturtle()  # Hide the turtle cursor
        x, y = conv_spos((3, 3.8))  # Convert game space co-ordinate to screen space coordinates
        t.penup()  # Lift pen up
        t.setx(x)  # Set x position of cursor
        t.sety(y)  # Set y position of cursor
        t.color("white")  # Set the pen color

        player = 1  # player win variable that stores who won the game
        # by default white wins

        # If m is less than or equal to 0 that means black won
        if m < 0:
            player = 2

        # Write the winnner dialogue to screen
        t.write(f"Player {player} wins!", font=("Times New Roman", 20, "italic"))  # Write font to screen

    else:
        turtle.ontimer(game_loop, 500)  # Continue the game loop after 500ms


if __name__ == "__main__":
    restart()  # Call the restart function when the program is run directly. This will bootstrap it and start the game
    turtle.done()  # Stop turtle from closing
