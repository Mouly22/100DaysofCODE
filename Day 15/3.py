import turtle
scrn = turtle.Screen()
scrn.bgcolor("lavender")
x = turtle.Turtle()
x.shape("circle")
for i in range(20):
    x.color("pink")
    x.left(65)
    x.forward(30)
scrn.exitonclick()