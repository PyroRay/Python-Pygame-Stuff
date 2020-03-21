#Ray Peng
#Excersize 1
#Mr.Blake blk.2

import pygame, math, random, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Random Shapes")

clrBorder = pygame.Color(170, 170, 170)
clrRandom = pygame.Color(0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    xLoc = random.randint(0, 1024)
    yLoc = random.randint(0, 768)
    randSize1 = random.randint(30, 100)
    randSize2 = random.randint(30, 100)
    randShapeNum = random.randint(1,4)
    clrRandom = pygame.Color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    if randShapeNum == 1:
        #pygame.draw.circle(windowSurfaceObj, clrBorder, (xLoc, yLoc), randSize1 + 30, 0)
        pygame.draw.circle(windowSurfaceObj, clrRandom, (xLoc, yLoc), randSize1, 0) # - int((randSize1/10)/2)
    elif randShapeNum == 2:
        #pygame.draw.rect(windowSurfaceObj, clrBorder, (xLoc - 15, yLoc - 15, randSize1 + 30, randSize2 + 30), 0)
        pygame.draw.rect(windowSurfaceObj, clrRandom, (xLoc, yLoc, randSize1, randSize2), 0)
    elif randShapeNum == 3:
        #pygame.draw.ellipse(windowSurfaceObj, clrBorder, (xLoc - 15, yLoc - 15, randSize1 + 30, randSize2 + 30), 0)
        pygame.draw.ellipse(windowSurfaceObj, clrRandom, (xLoc, yLoc, randSize1, randSize2), 0)

    elif randShapeNum == 4:
        iSides = random.randint(3, 7)
        iAngle = (math.pi * 2)/iSides
        lPoints = []
        for i in range(iSides):
            iX = math.cos(iAngle * i)*randSize1 + xLoc
            iY = math.sin(iAngle * i)*randSize1 + yLoc
            lPoints.append((iX, iY))        

        pygame.draw.polygon(windowSurfaceObj, clrRandom, tuple(lPoints))
        
    pygame.display.update()
    fpsClock.tick(60)
