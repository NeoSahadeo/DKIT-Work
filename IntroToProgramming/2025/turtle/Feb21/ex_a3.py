# Create a function draw_filled_circle that accepts two parameter the radius and the colour. Your function should
# draw a filled circle with the given radius and color.

# The main program should prompt the user for the radius and color and then call the function.

import turtle

t = turtle.Turtle()  # Instantiates the turtle class

def draw_filled_circle(radius, color):
    t.fillcolor(color)  # Fill color
    t.begin_fill()  # Start the fill
    t.circle(radius)  # Draw the circle
    t.end_fill()  # End the fill


if __name__ == "__main__":
    circle_radius = int(turtle.textinput("Circle", "Enter radius"))  # Ask the user for a radius then convert the string to a integer
    circle_color = turtle.textinput("Circle", "Enter color")  # Ask the user for a colour

    draw_filled_circle(circle_radius, circle_color)  # Call the function and pass in the values


    turtle.exitonclick() # Wait for user to click the window; close when clicked