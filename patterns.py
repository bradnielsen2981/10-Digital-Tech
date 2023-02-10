import turtle

turtle.bgcolor("black")
t = turtle.Turtle() #t is a turtle object
t.penup()
t.goto(0,0)

colourlist = ["red","blue","yellow","green","purple","orange"]

t.pendown()
for i in range(24):
    for num in range(4): 
        t.pencolor(colourlist[num]) #0, 1, 2
        t.forward(100)
        t.right(90)
    t.right(15)
t.penup()
input()
turtle.clear()

t.pendown()
for colour in colourlist:
    t.pencolor(colour)
    t.forward(200)
    t.right(60)
t.penup()

input()