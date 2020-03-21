#Ray Peng
#Excersize 1
#Mr.Blake blk.2

import pygame, random, sys, math, colorsys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Line Thing")

# clRed = 255
# clGreen = 0
# clBlue = 0
# clrChange = pygame.Color(clRed, clGreen, clBlue)
clrChange = pygame.Color(255, 255, 255)
HSVHue = 0
RGBDecimal = 0
iAngle = 0.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    HSVHue += 0.05
    RGBDecimal = colorsys.hsv_to_rgb(HSVHue, 1, 1)
    RGBValue = []

    for x in RGBDecimal:
        RGBValue.append(x*255)

    xLoc = math.sin(iAngle)*300
    yLoc = math.cos(iAngle)*300

    pygame.draw.line(windowSurfaceObj, tuple(RGBValue), (512, 384), (512+xLoc, 384+yLoc), 2)
    pygame.draw.line(windowSurfaceObj, tuple(RGBValue), (512, 384), (512-xLoc, 384-yLoc), 2)

    iAngle += math.radians(20)

    pygame.display.update()
    fpsClock.tick(60)
