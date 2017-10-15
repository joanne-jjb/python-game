'''
Created on Oct 14, 2017

@author: buenavej
'''

import turtle
import random

class apple:
    appleBounds = 25

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)
        self._turtle.shape("apple.gif")
        self._turtle.penup()
        x = int(random.randint(-250, 250) / 10 ) * 10
        y = int(random.randint(-250, 250) / 10) * 10
        self._turtle.setposition(x,y)
        self._turtle.showturtle()

    def getx(self):
        return int(self._turtle.xcor())

    def gety(self):
        return int(self._turtle.ycor())

    def collide(self, x, y):
        rangex = range((self.getx() - self.appleBounds), (self.getx() + self.appleBounds))
        rangey = range((self.gety() - self.appleBounds), (self.gety() + self.appleBounds))
        
        if ((x in rangex) and (y in rangey)):
            return True
        
        return False

    def destroy(self):
        self._turtle.hideturtle()
        self._turtle.clear()
        del self._turtle