#Write code to draw a regular pentagon 
#(a five-sided figure with all sides the same length)
import turtle
scrn = turtle.Screen()
x = turtle.Turtle()
for i in range(5):
    x.left(75)
    x.forward(50)
scrn.exitonclick()