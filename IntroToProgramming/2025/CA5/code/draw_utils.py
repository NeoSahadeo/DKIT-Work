import turtle
from utils import conv_spos, get_screen, get_tile_size


def draw_poly(x, y, width, height, color):
    """
    Draw Poly function is able to draw a 4-sided
    polygon with sides n,m
    :param int x: X game-space co-ord
    :param int y: Y game-space co-ord
    :param int width:
    :param int height:
    :param int color:
    """
    t = turtle.Turtle()  # Create turtle instance
    t.hideturtle()  # Hide the cursor
    t.speed(0)  # Set turtle speed to 0
    t.penup()  # Lift pen up
    t.pencolor(color)  # Set the colour the same colour to hide the lines

    x, y = conv_spos((x, y))  # Convert game space co-ordinate to screen space
    t.setx(x)  # Set x position of cursor
    t.sety(y)  # Set y position of cursor

    swap = True  # Swap variable to switch between height and width
    t.pendown()  # Put the pen down
    t.fillcolor(color)  # Change the fill color
    t.begin_fill()  # Begin to fill
    for x in range(0, 4):  # For loop that draws the 4 sided shape
        # Swap between height and width
        if swap:
            t.forward(width)  # Use the forward method
        else:
            t.forward(height)  # Use the forward method
        swap = not swap  # Negate the swap value
        t.left(90)  # 90deg to the left
    t.end_fill()  # Fill in the color


def draw_square(x, y, size, color):
    """
    Draw Square function is able to draw a square
    :param int x: X game-space co-ord
    :param int y: Y game-space co-ord
    :param int size:
    :param int color:
    """
    # Call the draw_poly function
    # with the size for both width and height.
    # Since it is a square.
    draw_poly(x, y, size, size, color)


def draw_text(x, y, text, size, type):
    t = turtle.Turtle()  # Create turtle instance
    t.hideturtle()  # Hide the turtle cursor
    x, y = conv_spos((x, y))  # Convert game space co-ordinate to screen space
    t.penup()  # Lift pen up
    t.setx(x)  # Set x position of cursor
    t.sety(y)  # Set y position of cursor
    t.write(text, font=("Arial", size, type))  # Write font to screen


if __name__ == "__main__":
    ### Test the functions
    h = get_tile_size()  # get the tile size
    draw_square(0, 0, h, "black")  # call the draw sqaure function
    draw_square(1, 0, h, "red")  # call the draw square function next to this
    turtle.done()  # Call turtle done so the window doesnt close
    ####
