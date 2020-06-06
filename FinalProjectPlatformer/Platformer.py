# Ray Peng
# Platforming game
# Mr Blake

# possible sprites: opengameart.org

# 'W' to jump, 'A' to move left, 'D' to move right

import pygame, sys, random, math
from pygame.locals import *

windowSurfaceObj = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Platformer')
fpsClock = pygame.time.Clock()
clrBlack = pygame.Color(0, 0, 0)
clrRed = pygame.Color(255, 0, 0)
clrGreen = pygame.Color(0, 255, 0)
clrWhite = pygame.Color(255, 255, 255)
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
screendim = pygame.display.get_surface().get_size()
runGame = True
jumptime = 0
fallspeed = 5
_DEBUG = True
highestplaty = screendim[1]

class solids:
    def __init__(self, color, height, width, xset, yset):
        self.size = (width, height)
        self.color = color
        self.x = xset
        self.y = yset

    def leftx(self): # x of left side
        return self.x - self.size[0]//2

    def rightx(self): # x of right side
        return self.x + self.size[0]//2

    def topy(self): # y of top
        return self.y - self.size[1]//2

    def boty(self): # y of bottom
        return self.y + self.size[1]//2

    def draw(self):
        pygame.draw.rect(windowSurfaceObj, (self.color), (self.leftx(), self.topy(), self.size[0], self.size[1]))
        if _DEBUG:
            pygame.draw.circle(windowSurfaceObj, clrGreen, (self.x, self.y), 5)

class player(solids):
    def __init__(self, color, height, width, xset, yset, speed, falling=False):
        # self.image = pygame.image.load('squirrel.png')
        self.direction = ""
        self.speed = speed
        self.falling = falling
        self.jumptime = 20
        super().__init__(color, height, width, xset, yset)
    
    def move(self, dirx = 0, diry = 0):
        self.x += dirx
        self.y += diry

class platform(solids):
    def __init__(self, color, height, width, xset, yset):
        super().__init__(color, height, width, xset, yset)

# (color, height, width, xset, yset, speed, falling=False) # player constructor
player1 = player(clrWhite, 100, 50, screendim[0]//2, screendim[1]//2, 10)
platforms = [platform(clrRed, 40, 100, 500, 600), platform(clrRed, 40, screendim[0], screendim[0]//2, screendim[1])] # creates array of platforms

# platform(clrRed, 40, screendim[0], screendim[0]//2, screendim[1]),

def onGround(plr):
    
    for platform in platforms:
        if platform.leftx() < plr.rightx() and platform.rightx() > plr.leftx():
            if platform.topy() == plr.boty():
                return True
            else:
                return False

def jump(plr, jumptime):
    plr.move(0, -jumptime)


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
    #endregion

    if left_pressed:
        player1.move(-player1.speed)
    elif right_pressed:
        player1.move(player1.speed)

    if onGround(player1) and not(up_pressed): # player is on the ground
        fallspeed = 5 # resets the velocity of fall
        player1.falling = False # player stops falling
        jumptime = player1.jumptime # resets the player's jump
    elif up_pressed: # if player presses 'w'
        if jumptime > -5 and player1.y + jumptime < screendim[1]-20: # if player has enough 'jump'
            # print("jumping")
            jump(player1, jumptime)
            jumptime -= 1
        elif onGround(player1):
            player1.falling = False
            # print("stop")
        else:
            player1.falling = True
        # print(jumptime)
    elif not(onGround(player1)) and not(up_pressed): # if player is in air and lets go of 'w'
        player1.falling = True # player starts falling
        jumptime = -5 # prevents player from 'jumping' in the air


    if player1.falling:
        for platform in platforms:
            if platform.leftx() < player1.rightx() and platform.rightx() > player1.leftx():
                if player1.boty() < platform.topy():
                    highestplaty = platform.topy()
                if fallspeed > platform.topy() - player1.boty(): # if the player's falling vector is larger than the distance to the ground
                    if highestplaty == platform.topy():
                        fallspeed = int(platform.topy() - player1.boty()) # changes the vector to the distance between the player and the ground, therefore falling directly onto the surface
            else:
                highestplaty = screendim[1]
        player1.move(0, fallspeed)
        fallspeed += 1

    for x in range(0, len(platforms)):
        platforms[x-1].draw()

    player1.move()
    player1.draw()

    # pygame.draw.circle(windowSurfaceObj, clrGreen, (player1.x, (player1.y + player1.size[1]//2)), 5) #draws circle at bottom of player

    pygame.display.update()
    fpsClock.tick(60)