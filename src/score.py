'''
Created on Oct 14, 2017

@author: buenavej
'''

import turtle

class score:
    x = 130
    y = 270

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)
        self._turtle.penup()
        self._value = 0
        self.__writeScore()

    def __str__(self):
        return str(self._value)

    def increase(self, points):
        self._value += points
        self.__writeScore()
    
    def __writeScore(self):
        self._turtle.clear()
        self._turtle.setposition(self.x, self.y)
        displayString = "Your Current Score Is: "
        self._turtle.write(displayString + str(self._value), True, align="center", font=("Courier", 20, "normal"))
