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
_DEBUG = False
topplaty = screendim[1]
botplaty = 0

class solids:
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound):
        self.size = (width, height)
        self.color = color
        self.x = xset
        self.y = yset
        self.v1 = pygame.Vector2(leftbound, botbound)
        self.v2 = pygame.Vector2(rightbound, topbound)
        self.boundary= [self.v1, self.v2]

    def leftx(self, hypox = None): # x coord of left side (hypox is an hypothetical x coord)
        if hypox is None:
            hypox = self.x
        # print("hypox1")
        # print(hypox)
        return hypox - self.size[0]//2

    def rightx(self, hypox = None): # x coord of right side (hypox is an hypothetical x coord)
        if hypox is None:
            hypox = self.x
        # print("hypox2")
        # print(hypox)
        return hypox + self.size[0]//2

    def topy(self, hypoy = None): # y of top (hypoy is an hypothetical y coord)
        if hypoy is None:
            hypoy = self.y
        # print("hypoy1")
        # print(hypoy)
        return hypoy - self.size[1]//2

    def boty(self, hypoy = None): # y of bottom (hypoy is an hypothetical y coord)
        if hypoy is None:
            hypoy = self.y
        # print("hypoy2")
        # print(hypoy)
        return hypoy + self.size[1]//2

    def draw(self):
        pygame.draw.rect(windowSurfaceObj, (self.color), (self.leftx(), self.topy(), self.size[0], self.size[1]))
        if _DEBUG:
            pygame.draw.circle(windowSurfaceObj, clrGreen, (self.x, self.y), 5)

class player(solids):
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, falling=False):
        # self.image = pygame.image.load('squirrel.png')
        self.direction = ""
        self.speed = speed
        self.falling = falling
        self.jumptime = 20
        super().__init__(color, height, width, xset, yset, rightbound, topbound, leftbound, botbound)
    
    def move(self, dirx = 0, diry = 0):
        if diry > 0: # Going down
            # print(self.boty(self.y + diry))
            # print(self.v1.y)
            if self.boty(self.y + diry) > self.v1.y: # check if hypothetical pos_y of player's bottom side is > bottom bounds
                # print("hello")
                self.y = self.topy(self.v1.y) # set bottom side to be at the bottom bound edge
            else:
                # print("whyyy")
                self.y += diry
        elif diry < 0: # Going up
            # print(self.topy(self.y + diry), self.v2.y)
            if self.topy(self.y + diry) < self.v2.y: # check if hypothetical pos_y of player's top side is < top bounds
                print('hit ceiling')
                self.y = self.boty(self.v2.y) # set top side to be at the top bound edge
            else:
                self.y += diry
                
        if dirx < 0: # Going left
            # print(self.v2.x)
            if self.leftx(self.x + dirx) < self.v2.x: # check if hypothetical pos_x of player's left side is < left bounds
                self.x = self.rightx(self.v2.x) # set left side to be at the left bound edge
            else:
                self.x += dirx
        elif dirx > 0: # Going right
            # print(self.v1.x)
            if self.rightx(self.x + dirx) > self.v1.x: # check if  hypothetical pos_x of player's right side is > right bounds
                self.x = self.leftx(self.v1.x) # set right side to be at the right bound edge
            else:
                self.x += dirx

        # self.x += dirx
        # self.y += diry

class platform(solids):
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound,):
        super().__init__(color, height, width, xset, yset, rightbound, topbound, leftbound, botbound)

# (color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, falling=False) # player constructor
player1 = player(clrWhite, 100, 50, screendim[0]//2, screendim[1]//2, screendim[1], 0, screendim[0], 0, 10)
platforms = [platform(clrRed, 40, screendim[0], screendim[0]//2, 0, 0, 0, 0, 0), platform(clrRed, 40, 100, 800, 600, screendim[1], 0, screendim[0], 0), platform(clrRed, 40, 100, 500, 550, screendim[1], 0, screendim[0], 0), platform(clrRed, 40, screendim[0], screendim[0]//2, screendim[1], 0, 0, 0, 0)] # creates array of platforms

# platform(clrRed, 40, screendim[0], screendim[0]//2, screendim[1]),

def onGround(plr):
    
    for platform in platforms:
        # print(platform)
        if platform.leftx() < plr.rightx() and platform.rightx() > plr.leftx():
            if topplaty == platform.topy():
                # print(int(plr.boty()), int(platform.topy()))
                if int(platform.topy()) == int(plr.boty()):
                    # print("on plat")
                    return True
                else:
                    # print("frickwhatiswrongwiththis")
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
            # print(platform)
            if platform.leftx() < player1.rightx() and platform.rightx() > player1.leftx(): # check if player is within horizontal range of platform
                if platform.topy() < topplaty: 
                    if player1.boty() < platform.topy():
                        topplaty = platform.topy()
                        if topplaty == platform.topy():
                            if player1.boty() < platform.topy():
                                player1.v1.y = topplaty
                                # print(player1.v1.y)
                    else:
                        topplaty = screendim[1]

                if platform.boty() > botplaty:
                    if player1.topy() > platform.boty():
                        botplaty = platform.boty()
                        if botplaty == platform.boty():
                            if player1.topy() > platform.boty():
                                player1.v2.y = botplaty
                                print(player1.v2.y)
                    else:
                        botplaty = 0

                # print(botplaty)

            else:
                print("reset")
                topplaty = screendim[1]
                botplaty = 0


            # print(topplaty)

                # if fallspeed > platform.topy() - player1.boty(): # if the player's falling speed is larger than the distance to the ground
                #     if topplaty == platform.topy():
                #         fallspeed = int(platform.topy() - player1.boty()) # changes the vector to the distance between the player and the ground, therefore falling directly onto the surface
        player1.move(0, fallspeed)
        fallspeed += 1

    for platform in platforms:

        if platform.topy() <= player1.boty() and platform.boty() >= player1.topy():

            if player1.leftx() > platform.rightx():
                player1.v2.x = platform.rightx()
                # print(player1.v2.x)

            elif player1.rightx() < platform.leftx():
                player1.v1.x = platform.leftx()
                # print(player1.v1.x)

        else:
            player1.v1.x = screendim[0]
            player1.v2.x = 0



    for x in range(0, len(platforms)):
        platforms[x-1].draw()

    player1.move()
    player1.draw()

    # pygame.draw.circle(windowSurfaceObj, clrGreen, (player1.x, (player1.y + player1.size[1]//2)), 5) #draws circle at bottom of player

    pygame.display.update()
    fpsClock.tick(60)