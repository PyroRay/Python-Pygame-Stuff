#Ray Peng
#Platforming game
#Mr Blake

import pygame, sys, random, math
from pygame.locals import *

windowSurfaceObj = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Platformer')
fpsClock = pygame.time.Clock()
clrBlack = pygame.Color(0, 0, 0)
clrRed = pygame.Color(255, 0, 0)
clrWhite = pygame.Color(255, 255, 255)
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
screendim = pygame.display.get_surface().get_size()
runGame = True

class player:
    def __init__(self, speed, color, height, width, xset, yset, dirx, diry):
        self.image = pygame.image.load('squirrel.png')
        self.radius = 15 #basically the size
        self.direction = ""
        self.speed = speed
        self.color = color
        self.size = (height, width)
        self.x = xset
        self.y = yset

    def draw(self):
        pygame.draw.rect(windowSurfaceObj, (self.color), (self.size))
    
    def move(self, dirx, diry):
        if(dirx == None):
            self.x += self.direction.x
        else:
            self.x += dirx
        if(diry == None):
            self.y += self.direction.y
        else:
            self.y += diry

player1 = player(10, clrWhite, 10, 5, screendim[0]//2, screendim[1]//2)

while runGame:
    windowSurfaceObj.fill(clrBlack)	

    #region Events
    for event in pygame.event.get():
        if event.type == QUIT:
            runGame = False
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                # print("\'w\' key was pressed")
                up_pressed = True
            elif event.key == pygame.K_a:
                # print("\'a\' key was pressed")
                left_pressed = True
            elif event.key == pygame.K_s:
                # print("\'s\' key was pressed")
                down_pressed = True
            elif event.key == pygame.K_d:
                # print("\'d\' key was pressed")
                right_pressed = True
        elif event.type == KEYUP:
            if event.key == pygame.K_w:
                # print("\'w\' key was let go")
                up_pressed = False
            elif event.key == pygame.K_a:
                # print("\'a\' key was let go")
                left_pressed = False
            elif event.key == pygame.K_s:
                # print("\'s\' key was let go")
                down_pressed = False
            elif event.key == pygame.K_d:
                # print("\'d\' key was let go")
                right_pressed = False

    pygame.display.update()
    fpsClock.tick(60)