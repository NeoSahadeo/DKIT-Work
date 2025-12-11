# Write a Python function that uses the Turtle library to draw a square.
# Write a python program that calls the square function. The size of the square should be input by the user.

import turtle

t = turtle.Turtle()


def draw_square(size):
    t.pendown() # put the pen down
    for x in range(4): # Draw the sqaure
        t.forward(size) # move forward
        t.left(90) # turn left


if __name__ == "__main__":  # File name is called __main__
    square_size = int(turtle.textinput("Square", "Size of square"))
    draw_square(square_size)



    turtle.exitonclick()  # Pauses program till you click the window

# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#
#     def speak(self):
#         print(f"{self.name} says {self.sound}")
#
#
# dog = Animal("Shibu", "Barks")
# cat = Animal("Cat", "Meow")
# cow = Animal("Dairy Cow", "Moooo")
#
# cow.speak()
