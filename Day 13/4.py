import turtle
scrn = turtle.Screen()
mini = turtle.Turtle()
mini.shape("turtle")
mini.color("pink")
mini.penup()                  #picks the pen up so the turtle does not draw a line as it moves.               
for i in range(10):
    mini.forward(50)
    mini.stamp()
    mini.right(36)
    mini.forward(-50)
   
    
scrn.exitonclick()
    
