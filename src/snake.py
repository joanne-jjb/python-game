'''
Created on Oct 14, 2017

@author: buenavej
'''
import turtle

class snake:
    snakeBounds = 10

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.shapesize(2,2)
        self._turtle.penup()
        self._bodyLength = 10
        self._body = []

    def getx(self):
        return int(self._turtle.xcor())
    
    def gety(self):
        return int(self._turtle.ycor())

    def move(self):
        self._turtle.stamp()
        self._body.insert(0, self._turtle.position())
        if (len(self._body) > self._bodyLength): 
            self._turtle.clearstamps(1)
            self._body.pop()
        self._turtle.forward(20)

    def right(self):
        if(self._turtle.heading() != 180):
            self._turtle.setheading(0)
    
    def left(self):
        if(self._turtle.heading() != 0):
            self._turtle.setheading(180)

    def up(self):
        if(self._turtle.heading() != 270):
            self._turtle.setheading(90)

    def down(self):
        if(self._turtle.heading() != 90):
            self._turtle.setheading(270)

    def grow(self):
        self._bodyLength += 1

    def collide(self, x, y):
        for location in self._body:
            rangex = range((int(location[0]) - self.snakeBounds), (int(location[0]) + self.snakeBounds))
            rangey = range((int(location[1]) - self.snakeBounds), (int(location[1]) + self.snakeBounds))
            if ((x in rangex) and (y in rangey)):
                return True
        return False

