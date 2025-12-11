# Write a function called draw_star that accepts the size of the star and draws a star with the given size.
# Your main program should call the function to draw the star

import turtle

t = turtle.Turtle()  # Instantiates the turtle class

def draw_star(size):
    star = 5
    for x in range(star):  # Draws the star; repeats 5 times
        t.forward(size)  # Moves forward by 100
        t.left(144) # Turns left by 144

if __name__ == "__main__":
    star_size = int(turtle.textinput("Star", "Star size"))  # Take in size
    draw_star(star_size) # Call the function

    turtle.exitonclick()  # Exit when windows is clicked