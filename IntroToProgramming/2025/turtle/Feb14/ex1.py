import turtle

t = turtle.Turle()
colors = ["Red","Green","Blue",]

for x in range(100):
    t.fillcolor([ x % len(colors)])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.forward()
