import turtle
scrn = turtle.Screen()
scrn.bgcolor("lavender")
rin = turtle.Turtle()
rin.color("hotpink")
rin.pensize(5)
rin.forward(100)
rin.left(120)
rin.forward(100)
rin.left(120)
rin.forward(100)

rini = turtle.Turtle()
rini.color("pink")
rini.pensize(5)
rini.forward(100)
rini.left(90)
rini.forward(100)
rini.left(90)
rini.forward(100)
rini.left(90)
rini.forward(100)

scrn.exitonclick()

#Just like we can have many different integers in a program, we can have many turtles. 
#Each of the turtle is an independent object and we call each one an instance of the Turtle type (class)
#Each instance has its own attributes and methods 
#Geometry conventions have 0 degrees facing East and that is the case here too
#Each instance can have attributes, sometimes called instance variables
#alex.forward(50) alex is an instance of the class Turtle.forward is a method.