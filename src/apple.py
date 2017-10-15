'''
Created on Oct 14, 2017

@author: buenavej
'''

import turtle
import random

class apple:
    #constant to define apple perimeter for scoring validation
    appleBounds = 25

    #determine bounds of where apples can spawn
    appleLoc = 600 / 2
    appleInc = 10

    #apples randomly place themselves
    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)
        self._turtle.shape("apple.gif")
        self._turtle.penup()
        x = int(random.randint(-self.appleLoc, self.appleLoc ) / self.appleInc ) * self.appleInc
        y = int(random.randint(-self.appleLoc, self.appleLoc ) / self.appleInc) * self.appleInc
        self._turtle.setposition(x,y)
        self._turtle.showturtle()

    #helper methods to return coordinates as int
    def getx(self):
        return int(self._turtle.xcor())

    def gety(self):
        return int(self._turtle.ycor())

    #APPLE MODULES

    #determines if the snake ran into the apple
    def collide(self, x, y):
        applex = self.getx()
        appley = self.gety()
        rangex = range((applex - self.appleBounds), (applex + self.appleBounds))
        rangey = range((appley - self.appleBounds), (appley + self.appleBounds))
        if ((x in rangex) and (y in rangey)):
            return True
        return False

    #apple removes itself from the game
    def destroy(self):
        self._turtle.hideturtle()
        self._turtle.clear()
        del self._turtle