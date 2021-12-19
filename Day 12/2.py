import turtle
scrn = turtle.Screen()
scrn.bgcolor("Gray")
mim = turtle.Turtle()
mim.color("pink")
mim.pensize(3)
distance = 10
for i in range(20):
    mim.forward(distance)
    mim.right(90)
    distance = distance + 10

scrn.exitonclick()


