import pygame
import sys
from time import sleep

BLACK = (0,0,0) # 
padWidth = 480
padHeight = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y))
    

def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('./res/background.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        drawObject(background, 0, 0)
        pygame.display.update()
    
    pygame.quit()

initGame()
runGame()
