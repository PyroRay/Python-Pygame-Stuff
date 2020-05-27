#Ray Peng
#Platforming game
#Mr Blake

#possible sprites: opengameart.org

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
    def __init__(self, speed, color, height, width, xset, yset, falling = False):
        # self.image = pygame.image.load('squirrel.png')
        self.radius = 15 #basically the size
        self.direction = ""
        self.speed = speed
        self.color = color
        self.size = (width, height)
        self.x = xset
        self.y = yset
        self.falling = falling

    def draw(self):
        pygame.draw.rect(windowSurfaceObj, (self.color), (self.x - self.size[0]//2, self.y - self.size[1]//2, self.size[0], self.size[1]))
        pygame.draw.circle(windowSurfaceObj, clrRed, (self.x, self.y), 5)
    
    def move(self, dirx = 0, diry = 0):
        self.x += dirx
        self.y += diry

player1 = player(10, clrWhite, 100, 50, screendim[0]//2, screendim[1]//2)

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

    if left_pressed:
        player1.move(-player1.speed)
    elif right_pressed:
        player1.move(player1.speed)

    if player1.y + player1.size[1] >= screendim[1]-20: # player is on the ground
        # print("ground")
        # player1.move() # player is not moving
        player1.falling = False
        if up_pressed:
            player1.move(0, -10)
        else:
            player1.falling = True

    if player1.falling:
        player1.move(0, 5)

    player1.move()
    player1.draw()

    pygame.display.update()
    fpsClock.tick(60)