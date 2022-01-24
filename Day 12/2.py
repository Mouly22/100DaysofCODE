 #If we want to make a repetitive pattern in our drawings, then we can use loops.

import turtle
scrn = turtle.Screen()
scrn.bgcolor("gray")
mim = turtle.Turtle()
mim.color("pink")
mim.pensize(3)
distance = 10
for i in range(20):
    mim.forward(distance)
    mim.right(90)
    distance = distance + 10

nim = turtle.Turtle()
nim.color("yellow")
nim.pensize(2)
distance = 9
angle = 90
for we in range(15):
    nim.forward(distance)
    nim.right(angle)
    distance = distance + 10
    angle = angle - 3


scrn.exitonclick()


