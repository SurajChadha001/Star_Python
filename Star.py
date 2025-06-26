# import turtle
# a = turtle.Turtle()
# a.getscreen().bgcolor("black")

# a.penup()
# a.goto(-200,100)
# a.pendown()
# a.color("yellow")

# a.speed(25)
# def star(turtle, size):
#     if size >= 10:
#         return
#     else:
#         turtle.begin_fill()
#         for i in range(5):
#             turtle.forward(size)
#             star(turtle, size/3)
#             turtle.left(216)
#             turtle.end_fill()
# star(a,360)
# turtle.done()

import turtle

# Set up the turtle
a = turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-200, 100)
a.pendown()
a.color("yellow")
a.speed(0)  # Fastest speed for better visualization

def star(turtle, size, level):
    if level == 0 or size < 10:  # Base case: stop when level is 0 or size is too small
        return
    else:
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            if level > 1:  # Recursive call for inner stars
                star(turtle, size / 3, level - 1)
            turtle.left(216)
        turtle.end_fill()

# Draw the main star with 3 levels of recursion
star(a, 360, 3)
turtle.done()