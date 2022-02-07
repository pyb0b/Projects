from turtle import *

def map1():
    
    speed(0)
    bgcolor("red")
    pu()
    setheading(90)
    
    fillcolor("blue")
    begin_fill()
    fd(400)
    right(90)
    fd(400)
    right(90)
    fd(50)
    right(90)
    fd(350)
    left(90)
    fd(350)
    right(90)
    fd(50)
    end_fill()

    backward(25)
    right(90)
    start=position()

    home()
    fillcolor("green")
    begin_fill()
    circle(25)
    end_fill()

    goto(start)
    left(90)



