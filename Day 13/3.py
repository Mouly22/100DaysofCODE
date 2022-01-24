import turtle
scrn = turtle.Screen()
mini = turtle.Turtle()
mini.color("yellow")
mini.shape("turtle")
mini.penup()                     #picks the pen up so the turtle does not draw a line as it moves.
for i in range(10):
    mini.forward(50)
    mini.stamp()
    mini.forward(-50)
    mini.right(36)

    
scrn.exitonclick()