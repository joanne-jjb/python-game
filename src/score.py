'''
Created on Oct 14, 2017

@author: buenavej
'''

import turtle

class score:
    #constants to define where the score is on the game screen
    x = 210
    y = 300

    #creates itself on the screen on init
    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)
        self._turtle.penup()
        self._value = 0
        self.__writeScore()

    #returns itself for printing
    def __str__(self):
        return str(self._value)

    #maintains itself based on points passed as parameters
    def increase(self, points):
        self._value += points
        self.__writeScore()

    def __writeScore(self):
        self._turtle.clear()
        self._turtle.setposition(self.x, self.y)
        displayString = "Your Current Score Is: "
        self._turtle.write(displayString + str(self), True, align="center", font=("Courier", 20, "normal"))
