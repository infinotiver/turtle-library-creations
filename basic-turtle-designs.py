# -*- coding: utf-8 -*-


import turle
#basic geometrical shapes
# 3.Pentagon
bob = turtle.Turtle()

bob.pensize(10)
bob.color('black', 'red')

bob.begin_fill()

for i in range(5):
    bob.forward(100)
    bob.left(72)
    
bob.end_fill()

# 4.Hexagon
bob = turtle.Turtle()

bob.color('red', 'yellow')

for i in range(6):
    bob.forward(100)
    bob.left(60)

turtle.done()

# 5.Septagon
bob = turtle.Turtle()

bob.pensize(10)
bob.color('black', 'red')

bob.begin_fill()

for i in range(7):
    bob.forward(100)
    bob.left(51.42)
    
bob.end_fill()

turtle.done()

# 6.Octagon
bob = turtle.Turtle()

bob.color('black', 'red')
bob.pensize(5)
bob.begin_fill()

for i in range(8):
    bob.forward(100)
    bob.left(45)
    
bob.end_fill()

turtle.done()

# 7.Nonagon
bob = turtle.Turtle()

bob.pensize(10)
bob.color('black', 'red')

bob.begin_fill()

for i in range(9):
    bob.forward(100)
    bob.left(40)
    
bob.end_fill()

turtle.done()

# 8.Decagon
bob = turtle.Turtle()

bob.pensize(10)
bob.color('black', 'red')

bob.begin_fill()

for i in range(10):
    bob.forward(100)
    bob.left(36)
    
bob.end_fill()

turtle.done()

# 9. Circle 
#Circle do not need loops it do not has sides so turtle have a different command for it.
bob = turtle.Turtle()

bob.pensize(10)
bob.color('black', 'red')

bob.begin_fill()
bob.circle(100)
bob.end_fill()

turtle.done()

# 10.Star
bob = turtle.Turtle()
bob.color('black', 'red')
bob.pensize(10)
    
bob.begin_fill()
for i in range(5):
    bob.forward(150)
    bob.right(144)
bob.end_fill()

turtle.done()

"""## We now know how to make circles. Let's experiment and try to draw the Olympic rings."""
#olympic rings
bob = turtle.Turtle()
bob.pensize(6) #Set the thickness of the pen to 6

firstRowColors = ["blue", "black", "red"] #firstRowColors is a list of colors that are present in the first row of logo

for i in range(3):
    bob.penup()
    bob.pencolor(firstRowColors[i])
    bob.goto(i*110, 0)
    bob.pendown()
    bob.circle(50)
 

secondRowColors = ["", "yellow","" ,  "green"]
for i in range(1, 4, 2):
    bob.penup()
    bob.pencolor(secondRowColors[i])
    bob.goto(i*55, -50)
    bob.pendown()
    bob.circle(50)
    
bob.hideturtle()
turtle.done()

"""## Spider web"""

t = turtle.Turtle()
t.speed(0)
 
#Code for building radical thread
for i in range(6):
    t.forward(150)
    t.backward(150)
    t.right(60)
    
 
 #Code for building spiral thread
side = 150
for i in range(15):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)
    for i in range(6):
        t.forward(side)
        t.right(60)
        side = side - 10

"""## Let us see some tally marks"""

tallymarks = turtle.Turtle()

number = int(input("Enter a number: ")) #Asking user to enter a number

tallymarks.right(90)
x = 0

for i in range(1,number+1):
    if(i%5 == 0): #For every fifth number, it will draw diagonal line
        tallymarks.right(135)
        tallymarks.forward(30*math.sqrt(2))
        tallymarks.right(225)
    else: #For other numbers, it will draw vertical line
        tallymarks.penup()
        tallymarks.goto(x*10,0)
        tallymarks.pendown()
        tallymarks.forward(30)
        x = x + 1

"""## Now, What about drawing a spiral square?"""

t = turtle.Turtle()
t.speed(10)

side = 200
for i in range(100):
    t.forward(side)
    t.right(90) #Exterior angle of a square is 90 degree
    side = side - 2
    
t.hideturtle()

"""## Now, let's start with a cool design!"""

bob = turtle.Turtle()
bob.color("red", "yellow")

bob.speed(10)

bob.begin_fill()
for i in range(50):
    bob.forward(300)
    bob.left(170)
bob.end_fill()

turtle.done()

import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Terry,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)

"""#### You could just experiment and play around with this thing and make cool designs"""

# Like see how I'm doing it!
bob = turtle.Turtle()
bob.color("red", "yellow")

bob.speed(10)

bob.begin_fill()
for i in range(50):
    bob.forward(math.sqrt(i))
    bob.left(170)
bob.end_fill()

turtle.done()

"""#### Did you observed You could just experiment and explore what happens"""

bob = turtle.Turtle()
bob.color("red", "yellow")

bob.speed(10)

bob.begin_fill()
for i in range(50):
    bob.forward(math.sqrt(i)*10)
    bob.left(170)
bob.end_fill()

turtle.done()

"""#### You see it It is just fun!! Just experiment and explore around with the maths library and the numbers and EXPLORE! What if I do something more"""

bob = turtle.Turtle()
bob.color("red", "yellow")

bob.speed(10)

bob.begin_fill()
for i in range(50):
    bob.forward(math.sqrt(i)*10)
    bob.left(i%90)
bob.end_fill()

turtle.done()

"""Let's continue"""

bob = turtle.Turtle()
bob.color("red")

bob.speed(10)

for i in range(100):
    bob.forward(20)
    bob.left(math.sin(i/10)*15)
    bob.left(20)

turtle.done()

bob = turtle.Turtle()
bob.color("red")

bob.speed(10)

for i in range(2000):
    bob.forward(10)
    bob.left(math.sin(i/10)*25)
    bob.left(20)

turtle.done()

"""See both the designs by changing some numbers, you can observee output seems to change!!
You could also do the same by using the random library!
"""

AISC = turtle.Turtle()

AISC.getscreen().bgcolor("#994444")

#for i in range(5):
#    AISC.forward(10)
#    AISC.left(216)

AISC.penup()
AISC.goto((-200, 50))
AISC.pendown()
AISC.speed(10)
AISC.pensize(3)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill
        
star(AISC, 300)
AISC.hideturtle()
turtle.done()

