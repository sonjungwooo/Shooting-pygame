from asyncio import Event
import pygame
import sys
from time import sleep


BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def initGame():
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padWidth))
    pygame.display.set_caption("Shoot For The Earth")
    clock = pygame.time.Clock()

def runGame() :
    global gamePad, clock

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        gamePad.fill(BLACK)
        pygame.display.update()

        clock.tick(60)
    runGame.quit()

initGame()
runGame()

def drawObject(obj, x,y):
    global gamePad
    gamePad.blit(obj, (x,y))
def initGame() :
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Shoot For The Earth')
    background = pygame.image.load('background.png')
    clock = pygame.time.clock()
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

def initGame() :
    global gamePad, clock, background, volunteer
    pygame.init()
    gamePad.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Shoot For The Earth')
    background = pygame.image.load('background.png')
    volunteer = pygame.image.load('volunteer.png')
    clock = pygame.time.clock()

def runGame(): 
    global gamepad, clock, background, volunteer

    volunteerSize = volunteer.get_rect().size
    volunteerWidth = volunteerSize[0]
    volunteerHeight = volunteerSize[1]

    x = padWidth * 0.4
    y = padHeight * 1
    servantX = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        drawObject(background, 0,0)
        drawObject(volunteer, x,y)

    onGame = False
    while not onGame:
        for event in pygame.event.get() :
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    servantX-= 10
                elif event.key == pygame.K_RIGHT:
                    servant += 10
            
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    volunteerX = 0
        
        drawObject(background,0,0)

        x += volunteerX
        if x<0:
            x=0
        elif x> padWidth - volunteerWidth:
            x = padWidth - volunteerWidth

def initGame():
    global gamePad, clock, background,volunteer, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.diplay.set_caption('Shoot For The Earth')
    background = pygame.image.load('background.png')
    volunteer = pygame.image.load('volunteer.png')
    clock = pygame.time.clock()
    missile = pygame.time.load('missile.png')

def runGame():
    global gamePad, clock , background, volunteer, missile
    missileXY = []
    onGame = False

    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    volunteerX -= 10
                elif event.key == pygame.K_RIGHT:
                    volunteerX += 10
                elif event.key == pygame.K_SPACE:
                    missileX = x + volunteerWidth/2
                    missileY = y - volunteerHeight
                    missileXY.append([missileX, missileY])
        
        drawObject(volunteer, x, y)

        if len (missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 15
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)
        
        pygame.display.update()

from asyncio import Event
import pygame
import sys 
import random 
from time import sleep

padWidth =500
padHeight =660
plasticImage = ['image1.png','image2.png','image3.png','image4.png','image5.png','image6.png','image7.png']

missileXY = []

plastic = pygame.image.load(random.choice(plasticImage))
plasticSize = plastic.get_rect().size
plasticWidth= plasticSize[0]
plasticHeight = plasticSize[1]

plasticX = random.randrange(0, padWidth - plasticWidth)
plasticY = 0
plasticSpeed = 3
            
if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)
plasticY += plasticSpeed

if plasticY > padHeight:
    plastic = pygame.image.load(random.choice(plasticImage))
    plasticSize = plastic.get.rect().size 
    plasticWidth = plasticSize(0)
    plasticHeight = plasticSize[1]
    plasticX = random.randrange(0, padWidth - plasticWidth)
    plasticY = 0
drawObject(plastic, plasticX, plasticY)

pygame.display.update()

def initGame():
    global gamePad, clock, background, volunteer, missile, pop
    pygame.init() 
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame. display.set_caption('Shoot For The Earth')
    background = pygame.image.load('background.png')
    volunteer = pygame.image.load('volunteer.png')
    clock = pygame.time.clock()
    missile = pygame.image.load('missile.png')
    pop = pygame.image.load('pop.png')

def runGame():
    global gamePad, clock, background,volunteer, missile, pop

    isShot = False
    shotCount = 0
    plasticPassed = 0

    onGame = False
    while not onGame:
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 15
                missileXY[i][1] = bxy[1]

                if bxy[1] < plasticY:
                    if bxy[0] > plasticX and bxy[0] < plasticX + plasticWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1
                
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        
        if isShot:
            drawObject(pop, plasticX, plasticY)

            plastic = pygame. image.load(random.choice(plasticImage))
            plasticSize = plastic.get_rect().size 
            plasticWidth = plasticSize[0]
            plasticHeight = plasticSize[1]
            plasticX = random.randrange(0, padWidth - plasticWidth)
            plasticY=0
            isShot = False

        drawObject(plastic, plasticX, plasticY)

def writeScore(count) :
    global gamePad
    font = pygame.font.Font ('NanumGoThic.ttf', 20)
    text = font.render('파괴한 운석: ' + str(count), True, (255,255,255))
    gamePad.blit(text,(10,0))

def writePassed(count) :
    global gamePad
    font = pygame.font.Font('NanumFoThic.ttf', 20)
    text = font.render('놓친 운석: ' + str(count), True, (255,0,0))
    gamePad.Blit(text, (360,0))

    writeScore(shotCount)

    plasticY += plasticSpeed

    if plasticY >padHeight:
        plastic =pygame.image.load(random.choice(plasticImage))
        plasticSize = plastic.get_rect().size
        plasticWidth = plasticSize[0]
        plasticHeight = plasticSize[1]
        plasticX = random.randrange(0, padWidth - plasticWidth)
        plasticY= 0
        plasticPassed += 1

    writePassed(plasticPassed)
    if isShot:
        drawObject(pop, plasticX,plasticY)

        plastic = pygame.image.load(random.choice(plasticImage))
        plasticSize = plastic.get_rect(0).size
        plasticWidth = plasticSize[0]
        plasticHeight = plasticSize[1]
        plasticX = random.randrange(0, padWidth - plasticWidth)
        plasticX = 0
        isShot = False

        plasticSpeedSpeed += 0.04
        if plasticSpeed >= 15:
            plasticSpeed = 10

def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255, 0,0))
    textpos = text. get_rect() 
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.display.update()
    sleep(2)
    runGame()

def crash() :
    global gamePad
    writeMessage('전투기 파괴됨')

def gameover():
    global gamePad
    writeMessage('GAME OVER') 
    
    x += volunteerX
    if x<0:
        x=0
    elif x>padWidth- volunteerWidth:
        x= padWidth - volunteerWidth

    if y< plasticY + plasticHeight:
        if (plasticX > x and plasticX < x + volunteerWidth) or \
        (plasticX + plasticWidth > x and plasticX + plasticWidth < x + volunteerWidth):
            crash()
    
    drawObject(volunteer, x, y)

if plasticPassed == 3:
    gameover()

    writePassed(plasticPassed)

padWidth = 500
padHeight = 660

plasticImage = ['','',]

popSound = ['','','',]

def initGame() :
    global gamePad, clock, background, volunteer, missile, pop, missileSound, gameoverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Shoot For The Earth')
    background = pygame.image.load('background.png')
    clock = pygame.time.clock()
    volunteer = pygame.image.load('volunteer.png')
    missile = pygame.image.load('missile.png')
    pygame.mixer.music.load('Track 77.png')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('Track 78.flac')
    gameoverSound = pygame.mixer.Sound('')

def runGame() :
    global gamePad, clock, background, volunteer, missile, pop, missileSound
    
    if event.key == pygame.K_SPACE:
        missileSound.play()
        missileX = x+ volunteerWidth/2
        missileY = y- volunteerHeight
        missileXY.append([missileX, missileY])

def writeMessage(text) :
    global gamePad, gameoverSound
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameoverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()

    plastic = pygame.image.load(random.choice(plasticImage))
    plasticSize = plastic.get_rect().size
    plasticWidth = plasticSize[0]
    plasticHeight = plasticSize[1]
    destroySound = pygame.mixer.Sound(random.choice(popSound))

    if isShot:
        drawObject(pop, plasticX, plasticY)
        destroySound.play()

        plastic = pygame.image.load(random.choice(plasticImage))
        plasticSize = plastic.get_rect().size
        plasticWidth = plasticSize[0]
        plasticHeight = plasticSize[1]
        plasticX = random.randrange(0, padWidth - plasticWidth)
        plasticY = 0
        destroySound = pygame.mixer.Sound(random.choice(popSound))
        isShot = False



