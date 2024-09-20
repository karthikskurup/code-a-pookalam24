import turtle
from turtle import *
import math
from tkinter import *

speed(10000)

# Turtle pen configuration
tur = turtle.Turtle()
tur.penup()
tur.speed("fastest")
tur.pensize(1)
tur.hideturtle()

#circle
def circ(len,clr):
    penup()
    home()
    goto(0, -(len+50))
    pendown()
    color(clr)
    begin_fill()
    circle(len)
    end_fill()

#outer circle
circ(300,"black")

#triangular pattern
home()
goto(0, -50)
def tripatt(len,clr):
    color(clr)
    for i in range(36):
        begin_fill()
        forward(len / math.tan(math.pi / 3.6))
        left(130)
        forward(len / math.sin(math.pi / 3.6))
        left(100)
        forward(len / math.sin(math.pi / 3.6))
        left(130)
        forward(len / math.tan(math.pi / 3.6))
        end_fill()
        left(10)
    left(5)

#outer patterns
tripatt(300,"red")
tripatt(271, "orange")
tripatt(246,"#fcd349")
tripatt(223,"#ffeeb5")


#middle circle
circ(200,"#014504")

#square pattern
def sqpatt(len,clr):
    penup()
    home()
    goto(0,-50)
    left(45)
    pendown()
    color(clr)
    for i in range(18):
        begin_fill()
        for i in range(4):
            forward(len * math.sqrt(2))
            left(90)
        end_fill()
        penup()
        left(20)
        pendown()

#inner patterns
sqpatt(100,"white")
sqpatt(82,"#3d0706")
sqpatt(70,"purple")

#line patterns
home()
goto(0,-50)
pensize(10)
color("purple")
for i in range(18):
    forward(196)
    backward(196)
    left(20)

#inner circle
circ(110,"orangered")
sqpatt(50,"green")

# Flower Petals
tur.goto(0,-90)
tur.pendown()
for i in range(16):
    tur.color(["red","goldenrod","crimson","violet"][i%4])
    tur.begin_fill()
    tur.right(90)
    tur.circle(50, 90)
    tur.left(90)
    tur.circle(50, 90)
    tur.right(180)
    tur.end_fill()
    tur.circle(40, 24)
tur.color("black")
tur.penup()
turtle.left(144)
turtle.Screen().exitonclick()


    

    
    
    
