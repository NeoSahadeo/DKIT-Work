import turtle
from ex2 import draw_shape

def draw_times(shape_type, shapes):
    for x in range(0, shapes):
        draw_shape(shape_type, 100)



if __name__ == "__main__":
    shape_type = input("Select shape (square, circle): ").strip().lower()
    shapes = int(input("Numbers of shapes: "))
    draw_times(shape_type, shapes)

    turtle.exitonclick()
