import turtle
turtle.bgcolor("black")
turtle.colormode(255)
t = turtle.Turtle() #t is a turtle object
t.penup()
t.speed(0)
t.goto(0,0)
colourlist = ["red","blue","yellow","green","purple","orange","aqua","pink"]
t.pendown()
for i in range(24):
    t.fillcolor((255-i*10,i*10,255))
    t.begin_fill()
    for num in range(8): 
        t.pencolor(colourlist[num]) #0, 1, 2
        t.forward(100)
        t.right(45)
    t.end_fill()
    t.right(15)
t.penup()
input()
turtle.clear()

t.pendown()
for i in range(24):
    for colour in colourlist:
        t.pencolor(colour)
        t.forward(200)
        t.right(60)
    t.right(15)
t.penup()
input()