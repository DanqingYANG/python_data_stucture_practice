import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

myTurtle.color("red")
myTurtle.fillcolor("pink")
myTurtle.begin_fill()
myTurtle.circle(50)
myTurtle.end_fill()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(120)
        #myTurtle.circle(60)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()