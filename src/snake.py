'''
Created on Oct 14, 2017

@author: buenavej
'''
import turtle

class snake:
    def __init__(self, screen):
        self._length = 1
        self._screen = screen
        self._turtle = turtle.Turtle()
        self._turtle.penup()
        
    def getx(self):
        return int(self._turtle.xcor())
    
    def gety(self):
        return int(self._turtle.ycor())
    
    def move(self):
        self._turtle.forward(10)
    
    def right(self):
        self._turtle.setheading(0)
    
    def left(self):
        self._turtle.setheading(180)

    def up(self):
        self._turtle.setheading(90)

    def down(self):
        self._turtle.setheading(270)

    def grow(self):
        print("Grow")
    