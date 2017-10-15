'''
Created on Oct 15, 2017

@author: buenavej
'''

import turtle
from snake import snake
from score import score
from apple import apple

class game:
    #Adjustment variables to customize the game
    screenColor = "light green"
    fontStyle = ("Courier","14")
    maxApples = 10
    screensize = 800
    appleValue = 1
    appleBonus = 10
    gameSpeed = 50

    def __init__(self, screen):
        self._screen = screen
        self._apples = []
        self._player = None
        self._totalScore = None
        self._applesToSpawn = 0

    #re-usable private methods used throughout the game
    def __buildCursor(self):
        cursor = turtle.Turtle()
        cursor.penup()
        cursor.hideturtle()
        return cursor

    def __resetScreen(self, screen):
        screen.clear()
        screen.bgcolor(self.screenColor)
        screen.setup(self.screensize, self.screensize)

    def __loadRules(self):
        rulesString = """
        __________          __  .__                      ________                       
        \______   \___.__._/  |_|  |__   ____   ____    /  _____/_____    _____   ____  
        |     ___<   |  |\   __\     \ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \  
        |    |    \___  | |  | |   |  (  <_> )   |  \ \    \_\  \/ __ \|  | |  \  ___/  
        |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /__|_|  /\___  > 
                  \/                \/            \/          \/     \/      \/     \/
     
            Welcome to the Python Game!
            Have you ever played \"snake\"? It's like that. Get the pun?

            #####################################################################
            #                          Playing the Game                         #
            #####################################################################
            - Your snake starts at length 10
            - Use the arrow keys to move your snake.
            - Your snake will always move forward.
            - Eating apples will increase your score, but also your snake length!

            #####################################################################
            #                              Scoring                              #
            #####################################################################
            - Each apple eaten will get you 1 point
            - Clearing the screen of apples will get you 10 bonus points

            #####################################################################
            #                          Ending the Game                          #
            #####################################################################
            - Hitting the wall or yourself will end the game.
            - The following will be saved as a .txt file:
                     - Your Score
        
        
        
                    Press "Enter" to begin the game or "Esc" to Exit
        """
        return rulesString

    def __closegame(self):
        self._screen.bye()

    ##game methods written sequentially, dictating game play
    def playgame(self):
        #set up screen to show rules
        self.__resetScreen(self._screen)
        cursor = self.__buildCursor()
        cursor.goto(0,-200)

        #write the rules
        cursor.write(self.__loadRules(), True, align="center", font=self.fontStyle)

        #register keys and listen for events
        self._screen.onkey(self.__initGame, "Return")
        self._screen.onkey(self.__closegame, "Escape")
        self._screen.listen()

    def __initGame(self):
        #initialize game variables (used for looping)
        self._apples = []
        self._applesToSpawn = self.maxApples

        #set-up screen
        self.__resetScreen(self._screen)
        self._screen.register_shape("apple.gif")
        self._screen.onkey(self.__endgame, "Escape")

        #register keystrokes
        self._player = snake()
        self._screen.onkey(self._player.up, "Up")
        self._screen.onkey(self._player.down, "Down")
        self._screen.onkey(self._player.left, "Left")
        self._screen.onkey(self._player.right, "Right")

        #generate apples and score tracking
        self.__generateApples()
        self._totalScore = score()

        #begin game
        self.__gameloop()

    def __gameloop(self):
        #body of the gameplay
        self._player.move()

        #check for collisions/check for lose conditions
        x = self._player.getx()
        y = self._player.gety()
        if(self._player.collide(x, y) or self.__wallCollision(x, y)):
            self.__endgame()
            return

        #check for scoring conditions or to add apples
        self.__checkForApples()
        self.__generateApples()

        self._screen.ontimer(self.__gameloop, self.gameSpeed)

    def __endgame(self):
        outputString = """
          ________                        ________                      
         /  _____/_____    _____   ____   \_____  \___  __ ___________  
        /   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ 
        \    \_\  \/ __ \|  | |  \  ___/  /    |    \   /\  ___/|  | \/ 
         \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    
                \/     \/      \/     \/          \/          \/      

        Your Final Score is: """

        outputString += str(self._totalScore)

        outputString += """
        A summary of your game has been saved to file "GameResult.txt"
        
        Press "Enter" to begin the game or "Esc" to Exit
        """

        #output summary file
        outputFile = open("GameResult.txt", "w+")
        outputFile.write("Your Final Score was: " + str(self._totalScore))
        outputFile.close()

        #clear screen for output text 
        self.__resetScreen(self._screen)
        cursor = self.__buildCursor()

        #write Game Over text on screen and listen for inputs
        cursor.goto(0, 0)
        cursor.write(outputString, True, align="center", font=self.fontStyle)
        self._screen.onkey(self.__initGame, "Return")
        self._screen.onkey(self.__closegame, "Escape")
        self._screen.listen()

    def __wallCollision(self, x, y):
        #check to see if the snake hit the wall
        wallRangey = range(((-self.screensize / 2) - 40), ((self.screensize / 2) - 40))
        wallRangex = range((-self.screensize / 2), (self.screensize / 2))
        if(x not in wallRangex or y not in wallRangey):
            return True
        return False

    def __checkForApples(self):
        #check to see if the snake ate an apple
        for apple in self._apples:
            #if the snake ate an apple, grow the snake and remove the apple
            if(apple.collide(self._player.getx(), self._player.gety())):
                self._totalScore.increase(self.appleValue)
                self._apples.remove(apple)
                apple.destroy()
                self._player.grow()

        #if all the apples were eaten, apply a bonus
        if(len(self._apples) == 0):
            self._totalScore.increase(self.appleBonus)
            self._applesToSpawn = self.maxApples

    def __generateApples(self):
        #checks to see if there are any apples are on the screen. If not, generates apples.
        #code also staggers apple generation so it doesn't happen quite so abruptly
        if(self._applesToSpawn > 0):
            self._apples.append(apple())
            self._applesToSpawn -= 1