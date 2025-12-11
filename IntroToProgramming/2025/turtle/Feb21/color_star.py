import turtle

t = turtle.Turtle()

star = 5
t.fillcolor("red")  # makes the colour red
t.begin_fill() # starts the fill
for x in range(star):
    t.forward(100)
    t.left(144)
t.end_fill()  # ends the fill
