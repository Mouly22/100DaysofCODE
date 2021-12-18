import turtle 
scrn = turtle.Screen()
scrn.bgcolor("lavender")
#the object scrn has color property(which we write as bgcolor)
arin = turtle.Turtle()
arin.color("blue")
arin.pensize(3)
#the object arin has property/attribute - color,pensize
arin.forward(100)
arin.right(90)                    #name.right(90) goes downward
arin.forward(90)

arina = turtle.Turtle()
arina.color("hot pink")
arina.forward(100)
arina.left(90)                    #name.left(90) goes upward
arina.forward(90)

#name.right(value)/name.left(value) works for defining angles(degrees).

prity = turtle.Turtle()
prity.color("green")
prity.right(45)
prity.forward(60)
prity.left(90)
prity.forward(100)

zina = turtle.Turtle()
zina.color("red")
zina.left(180)                #notice this
zina.forward(150)

scrn.exitonclick()                # wait for a user click on the canvas
#we invoke its exitonclick method of scrn object, the program pauses execution 
#and waits for the user to click the mouse somewhere in the window

#import turtle defines the module turtle which will allow you to create a Turtle object and draw with it.
#turtle.Turtle; here"turtle" tells Python that we are referring to the turtle module, which is where the object "Turtle" is found
