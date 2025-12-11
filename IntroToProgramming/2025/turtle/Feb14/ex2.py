import turtle

def draw_shape(shape_type, size):
    t = turtle.Turtle()
    if shape_type == "square":
        # t.fillcolor("red")
        # t.begin_fill()
        for x in range(4):
            t.pendown()
            t.forward(size)
            t.left(90)
        # t.end_fill()
    elif shape_type == "circle":
        # t.fillcolor("red")
        # t.begin_fill()
        t.circle(size)
        # t.end_fill()


if __name__ == "__main__":
    shape_type = input("Select shape (square, circle): ").strip().lower()
    size = int(input("Size of shape: "))

    draw_shape(shape_type, size)

    turtle.exitonclick()
