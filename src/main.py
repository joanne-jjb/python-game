'''
Created on Oct 14, 2017

@author: buenavej

Final Project
'''

#Imports
import turtle
from snake import snake
from apple import apple
from score import score

#Constants
screenColor = "light green"
maxApples = 2
gameSpeed = 100
appleValue = 1
appleBonus = 10
apples = []
applesToSpawn = maxApples

#Modules
def displayGameRules():
    rulesString = """
    __________          __  .__                      ________                       
    \______   \___.__._/  |_|  |__   ____   ____    /  _____/_____    _____   ____  
    |     ___<   |  |\   __\     \ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \  
    |    |    \___  | |  | |   |  (  <_> )   |  \ \    \_\  \/ __ \|  | |  \  ___/  
    |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /__|_|  /\___  > 
              \/                \/            \/          \/     \/      \/     \/
 
        Welcome to the Python Game!
        Have you ever played \"snake\"? It's exactly like that.
    
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
    
    
    
    
                Press "Enter" to begin the game or "Esc" to Exit
    """
    return rulesString

#Segments sections of the game into small, testable chunks
def buildPlayArea():
    global screen
    screen = turtle.Screen()
    screen.bgcolor(screenColor)
    screen.screensize(400,400)
    cursor = turtle.Turtle()
    cursor.penup()
    cursor.hideturtle()
    cursor.goto(0,-200)
    cursor.write(displayGameRules(), True, align="center", font=("Courier", 18, "normal"))
    screen.onkey(initGame, "Return")
    screen.onkey(endgame, "Escape")
    screen.listen()

def initGame():
    global screen
    global player
    global score

    screen.clear()
    screen.bgcolor(screenColor)
    screen.register_shape("apple.gif")
    screen.onkey(endgame, "Escape")
    player = snake(screen)
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    screen.onkey(player.left, "Left")
    screen.onkey(player.right, "Right")
    generateApples()
    score = score()

    gameloop()
    
def gameplay():
    generateApples()

def gameloop():
    global player
    player.move()
    checkForApples()
    generateApples()
    screen.ontimer(gameloop, gameSpeed)

def checkForApples():
    global apples
    global player
    global score
    global applesToSpawn

    for apple in apples:
        if(apple.collide(player.getx(), player.gety())):
            score.increase(appleValue)
            apples.remove(apple)
            apple.destroy()

    if(len(apples) == 0):
        score.increase(appleBonus)
        applesToSpawn = maxApples

def generateApples():
    global apples
    global applesToSpawn

    if(applesToSpawn > 0):
        apples.append(apple())
        applesToSpawn -= 1

def endgame():
    global screen
    global score

    print("Anything")
    outputFile = open("GameResult.txt", "w+")
    outputFile.write("Your Score is: " + str(score))
    outputFile.close()
    screen.bye()

def main():
    buildPlayArea()
    turtle.done()

main()