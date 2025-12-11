# Create the pattern show in the picture
# Write a function to create the picture
# Write a program to call the function

import turtle
t = turtle.Turtle()  # Instantiate the turtle class

def draw_circles():
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    for x in colors:  # 6 times because there are 6 circles in the picture shown
        t.pendown()  # put down before starting to draw
        t.fillcolor(x) # X is the color
        t.begin_fill()  # Start the fill
        t.circle(40)  # 40 is the radius
        t.end_fill()  # Fill in the circle
        t.penup()  # pick up before moving forward
        t.forward(40) # move forward the radius of the circle


if __name__ == "__main__":
    draw_circles()  # Calls the function
    turtle.exitonclick()  # Wait for user to click before closing window
