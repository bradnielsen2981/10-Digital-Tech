import turtle
turtle.bgcolor = "white"
turtleobject = turtle.Turtle()

#function will draw a coloured square, begin fill endfill
#arguments of the function are the colour ("red", side)
def coloursquare(colour, side):
    turtleobject.fillcolor(colour)
    turtleobject.begin_fill()
    for i in range(4):
        turtleobject.forward(side)
        turtleobject.right(90)
    turtleobject.end_fill()
    return

coloursquare("red",100)
input()


#create a row of 8 squares with RANDOM colours (red, yellow, blue)
#for loop 
