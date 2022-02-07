from turtle import *
from map_game import *
from pynput import keyboard

map1()

def _up():
    pu()
    setheading(90)
    forward(20)
    pd()

def _down():
    pu()
    setheading(-90)
    forward(20)
    pd()

def _right():
    pu()
    setheading(0)
    forward(20)
    pd()

def _left():
    pu()
    setheading(180)
    forward(20)
    pd()

while(True):
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('w'):
            _up()
        if event.key == keyboard.KeyCode.from_char('a'):
            _left()
        if event.key == keyboard.KeyCode.from_char('d'):
            _right()
        if event.key == keyboard.KeyCode.from_char('s'):
            _down()
        if event.key == keyboard.KeyCode.from_char('p'):
            break

print("good enough")

#asdw
