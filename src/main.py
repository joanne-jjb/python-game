'''
Created on Oct 14, 2017

@author: buenavej

Final Project
'''

#Imports
import random
import turtle

#Constants
screen = None
maxApple = 10
score = 0
applesConsumed = 0

snakeSegments = []
appleLocations = []
currentlyFacing = "s"
currentPosition = []
endGameOutput = ""
foundApples = []

#Modules
def displayGameRules():
    rulesString = """
    __________          __  .__                      ________                       
    \______   \___.__._/  |_|  |__   ____   ____    /  _____/_____    _____   ____  
    |     ___<   |  |\   __\  |  \ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \  
    |    |    \___  | |  | |   Y  (  <_> )   |  \ \    \_\  \/ __ \|  Y Y  \  ___/  
    |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /__|_|  /\___  > 
              \/                \/            \/          \/     \/      \/     \/
 
        Welcome to the Python Game!
        Have you ever played \"Snake\"? It's exactly like that.
    
        #####################################################################
        #                          Playing the Game                         #
        #####################################################################
        - Use the arrow keys to move your snake.
        - Your snake will always move forward.
        - Eating apples will increase your score, but also your snake length!
        - Apples are indicated by the \"@\" symbol.
    
        #####################################################################
        #                          Ending the Game                          #
        #####################################################################
        - Hitting the wall or yourself will end the game.
        - The following will be saved as a .txt file:
                 - Your Score
                 - Where you found apples
                 - Image of your final screen
    """
    return rulesString

#Segments sections of the game into small, testable chunks
def buildPlayArea():
    screen = turtle.getscreen()
    screen.bgcolor("light green")
    screen.screensize(400,400)
    cursor = turtle.getturtle()
    cursor.penup()
    cursor.hideturtle()
    cursor.goto(0,-200)


    cursor.write(displayGameRules(), True, align="center", font=("Courier", 18, "normal"))
    
    screen.listen()
    return screen

def initializeGame():
    userInput = ""
    while (userInput != "Y" and userInput != "N"):
        userInput = raw_input("Would you like to play the \"Python Game\"? Type \"Y\" for \"Yes\" and \"N\" for \"No\": ")
    if (userInput == "Y"):
        gameplay()
    if (userInput == "N"):
        endgame()

def gameplay():
    generateApples()

def generateApples():
    random.randint(0, 5)

def endgame():
    outputFile = open("GameResult.txt", "w+")
    outputFile.write("Your Score is: " + str(score))
    outputFile.close()

def main():
    screen = buildPlayArea()
    displayGameRules()
#    initializeGame()
    turtle.done()

main()