import pygame
from sys import exit

class App:
    def startGame(self):
        while True:
            # events
            for event in pygame.event.get():
                # close game event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # click game events
                if event.type == pygame.MOUSEBUTTONDOWN and self.gameActive == True:
                    # restart button event
                    if self.restartButton.collidepoint(event.pos):
                        self.initialize()
                    # menu button event
                    if self.menuButton.collidepoint(event.pos):
                        self.gameActive = False
                        self.PvP = False
                    # click on any of the 9 squares event
                    for i in range(9):
                        if self.buttonList[i].collidepoint(event.pos) and self.tictactoe[i] == 0 and self.lockAll == False:
                            self.textList[i] = self.font.render(self.XorO,False,self.textColor)
                            if self.PvP == True:
                                if self.XorO == 'x':
                                    self.XorO = 'o'
                                    self.tictactoe[i] = -1
                                else:
                                    self.XorO = 'x'
                                    self.tictactoe[i] = 1
                                self.checkWin()
                            else:
                                self.tictactoe[i] = -1
                                self.checkWin()
                                # if there is a win 1 move away then play there
                                if (self.winCon[0] == 2 or self.winCon[1] == 2 or self.winCon[2] == 2 or self.winCon[3] == 2 or 
                                      self.winCon[4] == 2 or self.winCon[5] == 2 or self.winCon[6] == 2 or self.winCon[7] == 2):
                                    for j in range(8):
                                        if self.winCon[j] == 2:
                                            for x in range(3):
                                                if self.tictactoe[self.winConNums[j][x]] == 0:
                                                    self.botPlay(self.winConNums[j][x])
                                                    break
                                            break
                                # if there is a loss 1 move away then block it
                                elif (self.winCon[0] == -2 or self.winCon[1] == -2 or self.winCon[2] == -2 or self.winCon[3] == -2 or 
                                      self.winCon[4] == -2 or self.winCon[5] == -2 or self.winCon[6] == -2 or self.winCon[7] == -2):
                                    for j in range(8):
                                        if self.winCon[j] == -2:
                                            for x in range(3):
                                                if self.tictactoe[self.winConNums[j][x]] == 0:
                                                    self.botPlay(self.winConNums[j][x])
                                                    break
                                            break
                                # block side strat
                                elif self.tictactoe[4] == 0 and self.tictactoe[1] == 0 and self.tictactoe[7] == -1 and self.tictactoe[3] == 0 and self.tictactoe[5] == 0:
                                    self.botPlay(1)
                                elif self.tictactoe[4] == 0 and self.tictactoe[7] == 0 and self.tictactoe[1] == -1 and self.tictactoe[3] == 0 and self.tictactoe[5] == 0:
                                    self.botPlay(7)
                                elif self.tictactoe[4] == 0 and self.tictactoe[3] == 0 and self.tictactoe[5] == -1 and self.tictactoe[7] == 0 and self.tictactoe[1] == 0:
                                    self.botPlay(3)
                                elif self.tictactoe[4] == 0 and self.tictactoe[5] == 0 and self.tictactoe[3] == -1 and self.tictactoe[7] == 0 and self.tictactoe[1] == 0:
                                    self.botPlay(5)
                                elif self.tictactoe[1] == -1 and self.tictactoe[3] == -1 and self.tictactoe[0] == 0:
                                    self.botPlay(0)
                                elif self.tictactoe[1] == -1 and self.tictactoe[5] == -1 and self.tictactoe[2] == 0:
                                    self.botPlay(2)
                                elif self.tictactoe[5] == -1 and self.tictactoe[7] == -1 and self.tictactoe[8] == 0:
                                    self.botPlay(8)
                                elif self.tictactoe[7] == -1 and self.tictactoe[3] == -1 and self.tictactoe[6] == 0:
                                    self.botPlay(6)
                                # block L strat
                                elif self.tictactoe[2] == -1 and self.tictactoe[7] == -1 and self.tictactoe[6] == 0:
                                    self.botPlay(6)
                                elif self.tictactoe[0] == -1 and self.tictactoe[7] == -1 and self.tictactoe[8] == 0:
                                    self.botPlay(8)
                                elif self.tictactoe[6] == -1 and self.tictactoe[1] == -1 and self.tictactoe[2] == 0:
                                    self.botPlay(2)
                                elif self.tictactoe[8] == -1 and self.tictactoe[1] == -1 and self.tictactoe[0] == 0:
                                    self.botPlay(0)
                                elif self.tictactoe[2] == -1 and self.tictactoe[3] == -1 and self.tictactoe[6] == 0:
                                    self.botPlay(6)
                                elif self.tictactoe[8] == -1 and self.tictactoe[3] == -1 and self.tictactoe[0] == 0:
                                    self.botPlay(0)
                                elif self.tictactoe[0] == -1 and self.tictactoe[5] == -1 and self.tictactoe[8] == 0:
                                    self.botPlay(8)
                                elif self.tictactoe[6] == -1 and self.tictactoe[5] == -1 and self.tictactoe[2] == 0:
                                    self.botPlay(2)
                                # if center slot is empty then play there
                                elif self.tictactoe[4] == 0:
                                    self.botPlay(4)
                                # block corner start
                                elif self.tictactoe[7] == 0 and self.tictactoe[4] == 1 and self.tictactoe[1] == 0:
                                    self.botPlay(7)
                                # block middle start
                                elif self.tictactoe[8] == 0 and self.tictactoe[4] == -1:
                                    self.botPlay(8)
                                else:
                                    for j in range(9):
                                        if self.tictactoe[j] == 0:
                                            self.botPlay(j)
                                            break
                                self.checkWin()
                # click menu events
                if event.type == pygame.MOUSEBUTTONDOWN and self.gameActive == False:
                    # pvp button event
                    if self.pvpButton.collidepoint(event.pos):
                        self.PvP = True
                    # pve button event
                    if self.pveButton.collidepoint(event.pos) or self.pvpButton.collidepoint(event.pos):
                        self.gameActive = True
                        self.initialize()
                        
            self.screen.fill('black')
            #draw game
            if self.gameActive:
                for i in range(9):
                    self.screen.blit(self.colorBoxList[i],self.buttonCordinates[i])
                    self.screen.blit(self.textList[i],self.textCordinates[i])
                self.screen.blit(self.winColorBox1,(360,65))
                self.screen.blit(self.winColorBox2,(360,175))
                self.screen.blit(self.winText1,(385,25))
                self.screen.blit(self.winText2,(385,135))
                self.screen.blit(self.winScore1,(415,78))
                self.screen.blit(self.winScore2,(415,188))
                self.screen.blit(self.restartColorBox,(360,235))
                self.screen.blit(self.restartText,(370,245))
                self.screen.blit(self.menuColorBox,(360,290))
                self.screen.blit(self.menuText,(390,300))
            #draw menu
            else:
                self.screen.blit(self.pvpColorBox,(200,75))
                self.screen.blit(self.pvpText,(240,85))
                self.screen.blit(self.pveColorBox,(200,175))
                self.screen.blit(self.pveText,(240,185))
                
            # update game 60fps
            pygame.display.update()
            self.clock.tick(60)
    
    def initialize(self):
        self.lockAll = False
        self.XorO = 'x'
        for i in range(9):
            self.tictactoe[i] = 0
            self.textList[i] = self.font.render('',False,self.textColor)
    
    def botPlay(self, slot):
        self.tictactoe[slot] = 1
        self.textList[slot] = self.font.render('o',False,self.textColor)
    
    def checkWin(self):
        self.winCon[0] = self.tictactoe[0] + self.tictactoe[1] + self.tictactoe[2]
        self.winCon[1] = self.tictactoe[3] + self.tictactoe[4] + self.tictactoe[5]
        self.winCon[2] = self.tictactoe[6] + self.tictactoe[7] + self.tictactoe[8]
        self.winCon[3] = self.tictactoe[0] + self.tictactoe[3] + self.tictactoe[6]
        self.winCon[4] = self.tictactoe[1] + self.tictactoe[4] + self.tictactoe[7]
        self.winCon[5] = self.tictactoe[2] + self.tictactoe[5] + self.tictactoe[8]
        self.winCon[6] = self.tictactoe[0] + self.tictactoe[4] + self.tictactoe[8]
        self.winCon[7] = self.tictactoe[2] + self.tictactoe[4] + self.tictactoe[6]
        # if win condition is met give winner a point and lock board
        for i in range(8):
            if self.winCon[i] == 3:
                self.oWins += 1
                self.winScore2 = self.smallFont.render(f'{self.oWins}',False,self.textColor)
                self.lockAll = True
            elif self.winCon[i] == -3:
                self.xWins += 1
                self.winScore1 = self.smallFont.render(f'{self.xWins}',False,self.textColor)
                self.lockAll = True
                
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption('TicTacToe')
        # set variables
        self.screen = pygame.display.set_mode((520,350))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('./fonts/Pixeltype.ttf',200)
        self.smallFont = pygame.font.Font('./fonts/Pixeltype.ttf',50)
        self.textColor = 'forestgreen'
        self.buttonBgColor = 'grey25'
        self.buttonList,self.colorBoxList,self.textList,self.textCordinates,self.buttonCordinates,self.tictactoe = [0] * 9,[0] * 9,[0] * 9,[0] * 9,[0] * 9,[0] * 9
        self.everyTime,self.everyThird,self.oWins,self.xWins = 0,0,0,0
        self.winCon = [0] * 8
        self.lockAll,self.gameActive,self.PvP = False,False,False
        self.winConNums = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        # create 3x3 game board
        for i in range(9):
            self.colorBoxList[i] = pygame.Surface((100,100))
            self.colorBoxList[i].fill(self.buttonBgColor)
            x = 15 + self.everyTime
            y = 15 + self.everyThird
            self.textCordinates[i] = x+17,y-5
            self.buttonCordinates[i] = x,y
            self.everyTime += 110
            if self.everyTime == 330:
                self.everyThird += 110
                self.everyTime = 0
            self.buttonList[i] = pygame.Rect(x,y,100,100)

        # create everything on the right side of the game
        self.winColorBox1 = pygame.Surface((135,50))
        self.winColorBox1.fill(self.buttonBgColor)
        self.winText1 = self.smallFont.render('X Wins',False,self.textColor)
        self.winColorBox2 = pygame.Surface((135,50))
        self.winColorBox2.fill(self.buttonBgColor)
        self.winText2 = self.smallFont.render('O Wins',False,self.textColor)
        self.winScore1 = self.smallFont.render('0',False,self.textColor)
        self.winScore2 = self.smallFont.render('0',False,self.textColor)

        self.restartColorBox = pygame.Surface((135,45))
        self.restartColorBox.fill(self.buttonBgColor)
        self.restartText = self.smallFont.render('Restart',False,self.textColor)
        self.restartButton = pygame.Rect(360,235,135,45)

        self.menuColorBox = pygame.Surface((135,45))
        self.menuColorBox.fill(self.buttonBgColor)
        self.menuText = self.smallFont.render('Menu',False,self.textColor)
        self.menuButton = pygame.Rect(360,290,135,45)
        
        # create everything for main menu
        self.pvpColorBox = pygame.Surface((135,50))
        self.pvpColorBox.fill(self.buttonBgColor)
        self.pvpText = self.smallFont.render('PvP',False,self.textColor)
        self.pvpButton = pygame.Rect(200,75,135,50)

        self.pveColorBox = pygame.Surface((135,50))
        self.pveColorBox.fill(self.buttonBgColor)
        self.pveText = self.smallFont.render('PvE',False,self.textColor)
        self.pveButton = pygame.Rect(200,175,135,50)

        # run game loop
        self.startGame()

if __name__ == "__main__":
    app = App()