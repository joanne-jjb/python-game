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
gameSpeed = 50
appleValue = 1
appleBonus = 10
screensize = 400

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
    cursor.write(displayGameRules(), True, align="center", font=("Courier", 12, "normal"))
    screen.onkey(initGame, "Return")
    screen.onkey(closegame, "Escape")
    screen.listen()

def initGame():
    global screen
    global player
    global totalScore
    global gameOver
    global apples
    global applesToSpawn

    apples = []
    applesToSpawn = maxApples
    gameOver = False

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
    totalScore = score()

    gameloop()
    
def gameplay():
    generateApples()

def gameloop():
    global player
    global gameOver

    player.move()
    if (player.collide(player.getx(), player.gety()) or wallCollision(player.getx(), player.gety())):
        gameOver = True
    checkForApples()
    generateApples()
    if not gameOver:
        screen.ontimer(gameloop, gameSpeed)
    else:
        endgame()

def wallCollision(x, y):
    wallRange = range(-screensize, screensize)
    if (x not in wallRange or y not in wallRange):
        return True
    return False

def checkForApples():
    global apples
    global player
    global totalScore
    global applesToSpawn

    for apple in apples:
        if(apple.collide(player.getx(), player.gety())):
            totalScore.increase(appleValue)
            apples.remove(apple)
            apple.destroy()
            player.grow()

    if(len(apples) == 0):
        totalScore.increase(appleBonus)
        applesToSpawn = maxApples

def generateApples():
    global apples
    global applesToSpawn

    if(applesToSpawn > 0):
        apples.append(apple())
        applesToSpawn -= 1

def endgame():
    global screen
    global totalScore
    
    outputString = """
      ________                        ________                      
     /  _____/_____    _____   ____   \_____  \___  __ ___________  
    /   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ 
    \    \_\  \/ __ \|  | |  \  ___/  /    |    \   /\  ___/|  | \/ 
     \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    
            \/     \/      \/     \/          \/          \/      
    Your Final Score is: """
    
    outputString += str(totalScore)

    outputString += """
    A summary of your game has been saved to file "GameResult.txt"
    
    Press "Enter" to begin the game or "Esc" to Exit
    """

    screen.clear()
    screen.bgcolor(screenColor)
    screen.screensize(400,400)
    cursor = turtle.Turtle()
    cursor.penup()
    cursor.hideturtle()
    cursor.goto(0, 0)
    cursor.write(outputString, True, align="center", font=("Courier", 12, "normal"))
    outputFile = open("GameResult.txt", "w+")
    outputFile.write("Your Final Score was: " + str(totalScore))
    outputFile.close()
    screen.onkey(initGame, "Return")
    screen.onkey(closegame, "Escape")
    screen.listen()

def closegame():
    screen.bye()

def main():
    buildPlayArea()
    turtle.done()

main()