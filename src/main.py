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
    snakeGame = game(screen)
    snakeGame.playgame()
    turtle.done()

main()