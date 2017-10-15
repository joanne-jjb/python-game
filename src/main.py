'''
Created on Oct 14, 2017

@author: buenavej

Final Project: Python Game
'''

#Imports
import turtle
from game import game

#commands to start game
def main():
    screen = turtle.Screen()
    pythonGame = game(screen)
    pythonGame.playgame()
    turtle.done()

main()