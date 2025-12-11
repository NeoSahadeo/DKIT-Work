import turtle
from ex3 import draw_times

if __name__ == "__main__":
    shape_type = input("Select shape (square, circle): ").strip().lower()
    shapes = int(input("Numbers of shapes: "))
    draw_times(shape_type, shapes)

    turtle.exitonclick()
