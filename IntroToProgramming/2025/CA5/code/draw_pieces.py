import turtle
from utils import get_tile_size
from draw_utils import draw_poly

t_h = get_tile_size()  # Get the tile size so pieces can scale

#### Piece Scale
SCALE = 0.7  # 0.7 looks nice. This allows relative scaling
####


#### Sizes for different parts of the chess pieces
BASE_M = 0.15
WIDTH_M = 0.75
####

#### DO NOT MANUALLY CHANGE THIS
BASE = t_h * BASE_M  # Calculate the base width
WIDTH = t_h * WIDTH_M  # Calculate the body width
####


def draw_rook(pos, main_c):
    """
    Draws the Rook

    :param (int, int) (x, y): Game coords
    :param string main_c: The colour of the pieces
    """
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE) * 0.5, y, WIDTH * SCALE, (t_h - t_h * 0.2) * SCALE, main_c)  # Draw the body; trim of 20 percent

    #### Draw the battlements
    head = 0.2 * t_h * SCALE
    draw_poly(x + (1 - WIDTH_M * SCALE) * 0.5, y + 0.8 * SCALE, head, head, main_c)
    draw_poly(x + 1 - (1 - WIDTH_M * SCALE) * 0.5 - 0.2 * SCALE, y + 0.8 * SCALE, head, head, main_c)
    draw_poly(x + 0.5 - (0.2 * 0.5 * SCALE), y + 0.74 * SCALE, head, head, main_c)
    ####

    turtle.update()  # Update the screen


def draw_bishop(pos, main_c):
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE) * 0.5, y + 0.1 * SCALE, WIDTH * SCALE, BASE * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.7) * 0.5, y, WIDTH * SCALE * 0.7, (t_h - t_h * 0.3) * SCALE, main_c)  # Draw the body; trim of 30 percent
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.9) * 0.5, y + 0.65 * SCALE, WIDTH * SCALE * 0.9, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.3) * 0.5, y + 0.89 * SCALE, WIDTH * SCALE * 0.3, (t_h * 0.1) * SCALE, main_c)

    turtle.update()  # Update the screen


def draw_king(pos, main_c):
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.7) * 0.5, y, WIDTH * SCALE * 0.7, (t_h - t_h * 0.3) * SCALE, main_c)  # Draw the body; trim of 30 percent
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.9) * 0.5, y, WIDTH * SCALE * 0.9, (t_h * 0.31) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.9) * 0.5, y + 0.5 * SCALE, WIDTH * SCALE * 0.9, (t_h * 0.15) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.55) * 0.5, y + 0.70 * SCALE, WIDTH * SCALE * 0.55, (t_h * 0.05) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.2) * 0.5, y + 0.74 * SCALE, WIDTH * SCALE * 0.2, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.4) * 0.5, y + 0.82 * SCALE, WIDTH * SCALE * 0.4, (t_h * 0.10) * SCALE, main_c)

    turtle.update()  # Update the screen


def draw_queen(pos, main_c):
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.5) * 0.5, y, WIDTH * SCALE * 0.5, (t_h - t_h * 0.3) * SCALE, main_c)  # Draw the body; trim of 30 percent
    draw_poly(x + (1 - WIDTH_M * SCALE * 1.1) * 0.5, y, WIDTH * SCALE * 1.1, (t_h * 0.31) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.8) * 0.5, y + 0.55 * SCALE, WIDTH * SCALE * 0.8, (t_h * 0.25) * SCALE, main_c)

    #### Draw the battlements
    head = 0.15 * t_h * SCALE
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.8) * 0.5, y + 0.75 * SCALE, head, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + 1 - (1 - WIDTH_M * SCALE * 0.8) * 0.5 - 0.15 * SCALE, y + 0.75 * SCALE, head, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.2) * 0.5, y + 0.75 * SCALE, WIDTH * SCALE * 0.2, (t_h * 0.16) * SCALE, main_c)
    ####

    turtle.update()  # Update the screen


def draw_knight(pos, main_c):
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.85) * 0.5, y, WIDTH * SCALE * 0.85, (t_h - t_h * 0.4) * SCALE, main_c)  # Draw the body;
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.85) * 0.5, y + 0.60 * SCALE, WIDTH * SCALE * 0.55, (t_h * 0.39) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.3) * 0.5, y + 0.60 * SCALE, WIDTH * SCALE * 0.73, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.4) * 0.5, y + 0.85 * SCALE, WIDTH * SCALE * 0.55, (t_h * 0.08) * SCALE, main_c)

    turtle.update()  # Update the screen


def draw_pawn(pos, main_c):
    turtle.tracer(0, 0)  # Turn screen drawing off -> Speeds up drawing
    x, y = pos  # Unpack the co-ordinates

    draw_poly(x + 0.5 - SCALE * 0.5, y, t_h * SCALE, BASE * SCALE, main_c)  # Draw the base
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.35) * 0.5, y, WIDTH * SCALE * 0.35, (t_h - t_h * 0.3) * SCALE, main_c)  # Draw the body;
    draw_poly(x + (1 - WIDTH_M * SCALE * 1.1) * 0.5, y, WIDTH * SCALE * 1.1, (t_h * 0.25) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.7) * 0.5, y + 0.6 * SCALE, WIDTH * SCALE * 0.7, (t_h * 0.1) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.9) * 0.5, y + 0.7 * SCALE, WIDTH * SCALE * 0.9, (t_h * 0.1) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.7) * 0.5, y + 0.8 * SCALE, WIDTH * SCALE * 0.7, (t_h * 0.1) * SCALE, main_c)
    draw_poly(x + (1 - WIDTH_M * SCALE * 0.4) * 0.5, y + 0.89 * SCALE, WIDTH * SCALE * 0.4, (t_h * 0.1) * SCALE, main_c)

    turtle.update()  # Update the screen


if __name__ == "__main__":

    turtle.done()
