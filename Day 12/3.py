import turtle
scrn = turtle.Screen()
scrn.bgcolor("lavender")
xen = turtle.Turtle()
xen.color("blue")
xen.shape("turtle")

x = 5
xen.up()                     #Pull the pen up -- no drawing when moving
for i in range(50):
    xen.stamp()              #Stamp a copy of the turtleshape onto the canvas and return its id
    xen.forward(x)
    xen.right(25)
    x += 2

scrn.exitonclick()
