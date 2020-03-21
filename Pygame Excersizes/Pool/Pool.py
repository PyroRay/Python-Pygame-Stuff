#Pool cue challenge thing

import pygame, math
from pygame.locals import *
from sys import exit

pygame.init()

winScreen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("Cue and Ball")

lineX = 0
lineY = 0
lineLength = 200
TargetX = 0
TargetY = 0
ballX = 640
ballY = 360
iAngle = 0
Opp = 0
Adj = 0
m = 0
n = 0
A = 0
B = 0
FPSspeed = pygame.time.Clock()

RunGame = True
while RunGame:
    FPSspeed.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunGame = False

    TargetX, TargetY = pygame.mouse.get_pos()

    if TargetX < ballX and TargetY < ballY:
        iAngle = math.atan((ballY-TargetY)/(ballX-TargetX))
    elif TargetX > ballX and TargetY < ballY:
        iAngle = math.pi + math.atan((ballY-TargetY)/(ballX-TargetX))
    elif TargetX > ballX and TargetY > ballY:
        iAngle = math.pi + math.atan((ballY-TargetY)/(ballX-TargetX))
    elif TargetX < ballX and TargetY > ballY:
        iAngle = math.pi*2 + math.atan((ballY-TargetY)/(ballX-TargetX))

    xLoc = math.cos(iAngle)*lineLength
    yLoc = math.sin(iAngle)*lineLength
    
    # print(iAngle)
    winScreen.fill(pygame.Color(0, 0, 0))

    pygame.draw.line(winScreen, (255,255,255), (ballX, ballY), (ballX - xLoc, ballY - yLoc), 10)
    pygame.draw.circle(winScreen, (255,255,255), (ballX, ballY), 20, 0)
    # winScreen.fill(pygame.Color(0,0,0))
    pygame.display.update()
	
