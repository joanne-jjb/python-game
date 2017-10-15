'''
Created on Oct 14, 2017

@author: buenavej
'''
import turtle

class snake:
    #Constant to define the perimeter of each snake segment for collison validation
    snakeBounds = 10

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.shapesize(2,2)
        self._turtle.penup()
        self._bodyLength = 10
        self._body = []

    #helper getter methods to return coordinates as int
    def getx(self):
        return int(self._turtle.xcor())

    def gety(self):
        return int(self._turtle.ycor())

    #registers arrow keys and validates snake can't go backwards
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

    #SNAKE MODULES

    #creates the image of the snake moving throughout the game
    #stamps the head, pops the last segment
    def move(self):
        self._turtle.stamp()
        self._body.insert(0, self._turtle.position())
        if (len(self._body) > self._bodyLength): 
            self._turtle.clearstamps(1)
            self._body.pop()
        self._turtle.forward(20)

    #manages how "long" the snake can be, otherwise snake will grow forever
    def grow(self):
        self._bodyLength += 1

    #manages if the snake ran into itself
    def collide(self, x, y):
        for location in self._body:
            segmentx = int(location[0])
            segmenty = int(location[1])
            rangex = range((segmentx - self.snakeBounds), (segmentx + self.snakeBounds))
            rangey = range((segmenty - self.snakeBounds), (segmenty + self.snakeBounds))
            if ((x in rangex) and (y in rangey)):
                return True
        return False

