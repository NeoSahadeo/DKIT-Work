# Create the following pattern with different colours for the large (outer) circle and smaller (inner) circle. The user
# should be asked how many circles they want in their rosette. The program will then draw the rosette with that
# number of inner and outer circles.

import turtle
t = turtle.Turtle()  # Instantiates the class turtle

turtle.bgcolor("black")


def draw_circle(size, amount_of_turns):  # Function to draw a circle and turn the turtle around
    t.circle(size)
    t.left(360 / amount_of_turns)


def draw_rosette(amount_of_turns):
    t.pencolor("pink")
    t.pensize(3)
    for x in range(amount_of_turns):  # Loop for outer circles
        draw_circle(60, amount_of_turns)

    t.pencolor("orange")
    for x in range(amount_of_turns):  # Loop for inner circles
        draw_circle(30, amount_of_turns)


t.speed(0)

if __name__ == "__main__":
    circles = int(turtle.textinput("Draw Rosette", "How many circles"))  # Get the amount of circles
    draw_rosette(circles)  # call the draw_rosette function passing in circles

    turtle.exitonclick()
