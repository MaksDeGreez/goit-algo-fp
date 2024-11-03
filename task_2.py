import turtle
import math

def draw_pythagoras_tree(t, length, angle, depth):
    if depth == 0:
        return

    t.forward(length)

    start_pos = t.position()
    start_heading = t.heading()

    # First branch (left angle)
    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, depth - 1)

    t.penup()
    t.setposition(start_pos)
    t.setheading(start_heading)
    t.pendown()

    # Second branch (right angle)
    t.right(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, depth - 1)

    t.penup()
    t.setposition(start_pos)
    t.setheading(start_heading)
    t.pendown()
    t.backward(length)

def main():
    depth = int(input("Enter recursion depth: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90) # Point the turtle up

    length = 100
    angle = 45

    draw_pythagoras_tree(t, length, angle, depth)

    turtle.done()

if __name__ == "__main__":
    main()
