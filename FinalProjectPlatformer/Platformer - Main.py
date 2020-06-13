# Ray Peng
# Platforming game
# Mr Blake

# possible sprites: opengameart.org

# 'W' to jump, 'A' to move left, 'D' to move right

import pygame, sys, random, math, os
from pygame.locals import *

pygame.init()
pygame.mixer.init()

windowSurfaceObj = pygame.display.set_mode((1280, 720))
dir_path = os.path.dirname(os.path.realpath(__file__))
pygame.display.set_caption('Platformer')
gameStart = False
fpsClock = pygame.time.Clock()
clrBlack = pygame.Color(0, 0, 0)
clrRed = pygame.Color(255, 0, 0)
clrGreen = pygame.Color(0, 255, 0)
clrWhite = pygame.Color(255, 255, 255)
clrDrkGrey = pygame.Color(102, 102, 102)
animImages = [pygame.image.load(dir_path + r'\Sprites\Main Character\charIdle.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charJumpRight.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charWalk1Right.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charWalk2Right.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charJumpLeft.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charWalk1Left.png'), pygame.image.load(dir_path + r'\Sprites\Main Character\charWalk2Left.png')]
animNum = 0
animArrayNum = 0
animTimer = 0
bckgrdImage = pygame.image.load(dir_path + r'\Sprites\background.png')
startmenu = pygame.image.load(dir_path + r'\Sprites\startmenu.png')
restartmenu = pygame.image.load(dir_path + r'\Sprites\restartmenu.png')
prizeimage = pygame.image.load(dir_path + r'\Sprites\prize.png')
playlist = list()
playlist.append(dir_path + r'\Sounds\Music\Premonition.mp3')
pygame.mixer.music.load(playlist[0])
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)        
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
rightmostplatx = screendim[0]
leftmostplatx = 0
vectorx = 0
vectory = 0
stagenum = 0
restart = False

class Solids:
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound):
        self.size = (width, height)
        self.color = color
        self.x = xset # centre point, x-axis
        self.y = yset # centre point, y-axis
        class Boundary:
            def __init__(self,right,top,left,bottom):
                self.topright = pygame.Vector2(right, top)
                self.bottomleft = pygame.Vector2(left, bottom)
        self.boundary = Boundary(rightbound, topbound, leftbound, botbound) # physical bounds for this object
        # print("bound start", self.boundary.topright.x, self.boundary.topright.y, self.boundary.bottomleft.x, self.boundary.bottomleft.y)

    def leftx(self, hypox = None): # x coord of left side (hypox is an hypothetical x coord)
        """Calculates the leftmost x-axis position of the sprite given an imagined centre point

        Args:
            hypox (float, optional): The hypothetical centre position for the sprite along x-axis. Defaults to current self.x.

        Returns:
            float: The leftmost x-axis coordinate for the sprite
        """        
        if hypox is None:
            hypox = self.x
        # print("hypox1")
        # print(hypox)
        return hypox - self.size[0]//2

    def rightx(self, hypox = None): # x coord of right side (hypox is an hypothetical x coord)
        """Calculates the rightmost x-axis position of the sprite given an imagined centre point

        Args:
            hypox (float, optional): The hypothetical centre position for the sprite along x-axis. Defaults to current self.x.

        Returns:
            float: The rightmost x-axis coordinate for the sprite
        """        
        if hypox is None:
            hypox = self.x
        # print("hypox2")
        # print(hypox)
        return hypox + self.size[0]//2

    def topy(self, hypoy = None): # y of top (hypoy is an hypothetical y coord)
        """Calculates the highest y-axis position of the sprite given an imagined centre point

        Args:
            hypox (float, optional): The hypothetical centre position for the sprite along y-axis. Defaults to current self.y.

        Returns:
            float: The highest y-axis coordinate for the sprite
        """        
        if hypoy is None:
            hypoy = self.y
        # print("hypoy1")
        # print(hypoy)
        return hypoy - self.size[1]//2

    def boty(self, hypoy = None): # y of bottom (hypoy is an hypothetical y coord)
        """Calculates the lowest y-axis position of the sprite given an imagined centre point

        Args:
            hypox (float, optional): The hypothetical centre position for the sprite along y-axis. Defaults to current self.y.

        Returns:
            float: The lowest y-axis coordinate for the sprite
        """        
        if hypoy is None:
            hypoy = self.y
        # print("hypoy2")
        # print(hypoy)
        return hypoy + self.size[1]//2

    def draw(self):
        pygame.draw.rect(windowSurfaceObj, (self.color), (int(self.leftx()), int(self.topy()), self.size[0], self.size[1]))
        if _DEBUG:
            pygame.draw.circle(windowSurfaceObj, clrGreen, (self.x, self.y), 5)

class Player(Solids):
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, falling=False):
        # self.image = pygame.image.load('squirrel.png')
        self.direction = ""
        self.speed = speed
        self.falling = falling
        self.jumptime = 20
        super().__init__(color, height, width, xset, yset, rightbound, topbound, leftbound, botbound)
    
    def move(self, dirx = 0, diry = 0):
        if dirx < 0: # Going left
            # print("rightbound", self.boundary.topright.x)
            if self.leftx(self.x + dirx) < self.boundary.bottomleft.x: # check if hypothetical pos_x of player's left side is < left bounds
                self.x = self.rightx(self.boundary.bottomleft.x) # set left side to be at the left bound edge
                # print("setbound left", self.boundary.bottomleft.x)
            else:
                self.x += dirx
        elif dirx > 0: # Going right
            # print("leftbound", self.boundary.bottomleft.x)
            if self.rightx(self.x + dirx) > self.boundary.topright.x: # check if  hypothetical pos_x of player's right side is > right bounds
                self.x = self.leftx(self.boundary.topright.x) # set right side to be at the right bound edge
                # print("setbound right", self.boundary.topright.x)
            else:
                self.x += dirx

        if diry > 0: # Going down
            # print(self.boty(self.y + diry))
            # print(self.boundary.bottomleft.y)
            if self.boty(self.y + diry) > self.boundary.bottomleft.y: # check if hypothetical pos_y of player's bottom side is > bottom bounds
                # print("hello") 
                self.y = self.topy(self.boundary.bottomleft.y) # set bottom side to be at the bottom bound edge
            else:
                # print("whyyy")
                self.y += diry
        elif diry < 0: # Going up
            # print(self.topy(self.y + diry), self.boundary.topright.y)
            if self.topy(self.y + diry) < self.boundary.topright.y: # check if hypothetical pos_y of player's top side is < top bounds
                self.y = self.boty(self.boundary.topright.y) # set top side to be at the top bound edge
            else:
                self.y += diry
                
        # self.x += dirx
        # self.y += diry
    def animate(self, onground):
        if left_pressed:
            if onground:
                if animNum == 1:
                    windowSurfaceObj.blit(animImages[5], (int(self.leftx()), int(self.topy())))
                elif animNum == 2:
                    windowSurfaceObj.blit(animImages[6], (int(self.leftx()), int(self.topy())))
            elif not(onground):
                windowSurfaceObj.blit(animImages[4], (int(self.leftx()), int(self.topy())))
        elif right_pressed:
            if onground:
                if animNum == 1:
                    windowSurfaceObj.blit(animImages[2], (int(self.leftx()), int(self.topy())))
                elif animNum == 2:
                    windowSurfaceObj.blit(animImages[3], (int(self.leftx()), int(self.topy())))
            elif not(onground):
                windowSurfaceObj.blit(animImages[1], (int(self.leftx()), int(self.topy())))
        else:
            windowSurfaceObj.blit(animImages[0], (int(self.leftx()), int(self.topy())))

        


class Platform(Solids):
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound,):
        super().__init__(color, height, width, xset, yset, rightbound, topbound, leftbound, botbound)

class Prize(Solids):
    def imgdraw(self):
        windowSurfaceObj.blit(prizeimage, (int(self.leftx()), int(self.topy())))

    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound,):
        super().__init__(color, height, width, xset, yset, rightbound, topbound, leftbound, botbound)

# windowSurfaceObj.blit(animImages[0], (int(self.leftx()), int(self.topy())))

# (color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, falling=False) # constructor
player1 = Player(clrWhite, 100, 50, 25, 600, screendim[0], 0, 0, screendim[1], 10)

# region Platforms
platformsP1 = [[Platform(clrDrkGrey, 40, 100, 200, 600, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 800, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 500, 575, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 400, 40, screendim[0], 520, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 150, 1205, 320, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])], \
    [Platform(clrDrkGrey, 40, 800, 600, 250, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 100, 450, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 800, 550, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 500, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 500, 40, 1100, 470, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])], \
        [Platform(clrDrkGrey, 40, 50, 200, 600, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 50, 800, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 50, 500, 575, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 400, 40, screendim[0], 520, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 500, 1100, 320, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 600, 40, 870, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 500, 501, 321, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 400, 690, 180, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])]] # creates array of stages and then a sub-array of platforms

prizes = [Prize(clrGreen, 120, 60, 1205, 240, screendim[0], 0, 0, screendim[1]), Prize(clrGreen, 120, 60, 1205, 640, screendim[0], 0, 0, screendim[1]), Prize(clrGreen, 120, 60, 1205, 240, screendim[0], 0, 0, screendim[1])]
spawnlocations = [600, 25]
# endregion

# platform(clrRed, 40, screendim[0], screendim[0]//2, screendim[1]),

def onGround(plr):
    platnum = 0
    for platform in platformsP1[stagenum]:
        platnum += 1
        # print(platnum)
        if platform.leftx() < plr.rightx() and platform.rightx() > plr.leftx():
            # print("in bounds")
            # print(topplaty, int(platform.topy()))
            if topplaty == platform.topy():
                if int(platform.topy()) == int(plr.boty()):
                    # print("on plat")
                    return True
                else:
                    pass
                    # we don't yet know if the player isn't on another platform, so it is premature to return False
    return False # now we've checked all platforms, so it's safe to conclude player isn't on a platform

def jump(plr, jumptime):
    plr.move(0, -jumptime)
    

while runGame:
    if gameStart:
        windowSurfaceObj.blit(bckgrdImage, (0, 0))
        pygame.mixer.music.set_volume(0.05)
    else:
        if restart:
            windowSurfaceObj.blit(restartmenu, (0, 0))
            pygame.mixer.music.set_volume(0.1)
        else:
            windowSurfaceObj.blit(startmenu, (0, 0))

    #region Events
    for event in pygame.event.get():
        if event.type == QUIT:
            runGame = False
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                # print("\'w\' key was pressed")
                up_pressed = True
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(dir_path + r'\Sounds\Sound Effects\jump.wav'))
                pygame.mixer.Channel(0).set_volume(0.3)
            elif event.key == pygame.K_a:
                # print("\'a\' key was pressed")
                left_pressed = True
            elif event.key == pygame.K_s:
                # print("\'s\' key was pressed")
                down_pressed = True
            elif event.key == pygame.K_d:
                # print("\'d\' key was pressed")
                right_pressed = True
            elif event.key == pygame.K_RETURN:
                # print("\'RETURN\' key was pressed")
                gameStart = True
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(dir_path + r'\Sounds\Sound Effects\start.wav'))
                pygame.mixer.Channel(1).set_volume(0.4)
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

    vectorx = 0

    if left_pressed:
        vectorx = (-player1.speed)
    elif right_pressed:
        vectorx = (player1.speed)

    playerOnGround = onGround(player1)
    # print(playerOnGround)

    if playerOnGround and not(up_pressed): # player is on the ground
        fallspeed = 5 # resets the velocity of fall
        player1.falling = False # player stops falling
        jumptime = player1.jumptime # resets the player's jump
    elif up_pressed: # if player presses 'w'
        if jumptime > -5 and player1.y + jumptime < screendim[1]-20: # if player has enough 'jump'
            # print("jumping")
            jump(player1, jumptime)
            jumptime -= 1
        elif playerOnGround:
            player1.falling = False
            # print("stop")
        else:
            player1.falling = True
    elif not(playerOnGround) and not(up_pressed): # if player is in air and lets go of 'w'
        player1.falling = True # player starts falling
        jumptime = -5 # prevents player from 'jumping' in the air
        # print("falling")

    platnum2 = 0
    for platform in platformsP1[stagenum]:
        platnum2 += 1
        # print(platnum2)
        # print(topplaty)
        if platform.leftx() < player1.rightx() and platform.rightx() > player1.leftx(): # check if player is within horizontal range of platform
            if platform.topy() < topplaty:
                # print(platnum2, platform.topy(), topplaty)
                if player1.boty() <= platform.topy():
                    topplaty = platform.topy()
                if topplaty == platform.topy():
                    if player1.boty() <= platform.topy():
                        player1.boundary.bottomleft.y = topplaty
                        # print("reset bottom", player1.boundary.bottomleft.y)
                            # print(topplaty)
                            # print(player1.boundary.bottomleft.y)

            if platform.boty() > botplaty:
                if player1.topy() >= platform.boty():
                    botplaty = platform.boty()
                if botplaty == platform.boty():
                    if player1.topy() >= platform.boty():
                        player1.boundary.topright.y = botplaty
                        # print("reset top", player1.boundary.topright.y)
                        # print(player1.boundary.topright.y)

        else:
            if topplaty == platform.topy():
                player1.boundary.bottomleft.y = screendim[1]
                topplaty = screendim[1]
                # print("reset bottom", player1.boundary.bottomleft.y)
            if botplaty == platform.boty():
                player1.boundary.topright.y = 0
                botplaty = 0
                # print("reset top", player1.boundary.topright.y)

    if player1.falling:
        player1.move(0, fallspeed)
        fallspeed += 1

    for platform in platformsP1[stagenum]:

        if platform.topy() < player1.boty() and platform.boty() > player1.topy():

            if platform.leftx() < rightmostplatx:
                if player1.rightx() <= platform.leftx():
                    rightmostplatx = platform.leftx()
                if rightmostplatx == platform.leftx():
                    if player1.rightx() <= platform.leftx():
                        player1.boundary.topright.x = rightmostplatx
                        # print("reset rightmost", player1.boundary.topright.x)

            if platform.rightx() > leftmostplatx:
                if player1.leftx() >= platform.rightx():
                    leftmostplatx = platform.rightx()
                if leftmostplatx == platform.rightx():
                    if player1.leftx() >= platform.rightx():
                        player1.boundary.bottomleft.x = leftmostplatx
                        # print("reset leftmost", player1.boundary.bottomleft.x)

        else:
            if leftmostplatx == platform.rightx():
                player1.boundary.bottomleft.x = 0
                leftmostplatx = 0
                # print("reset leftmost", player1.boundary.bottomleft.x)
            if rightmostplatx == platform.leftx():
                player1.boundary.topright.x = screendim[0]
                rightmostplatx = screendim[0]
                # print("reset rightmost", player1.boundary.topright.x)

        # print("right", player1.boundary.topright.x)
        # print("left", player1.boundary.bottomleft.x)

    if player1.x > prizes[stagenum].leftx() and player1.x < prizes[stagenum].rightx() and player1.y < prizes[stagenum].boty() and player1.y > prizes[stagenum].topy():
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(dir_path + r'\Sounds\Sound Effects\prizecollect.wav'))
        pygame.mixer.Channel(2).set_volume(0.3)
        if stagenum + 1 >= len(prizes):
            gameStart = False
            stagenum = -1
            restart = True
            # print("end")
        else:
            stagenum += 1
            player1.x = spawnlocations[1]
            player1.y = spawnlocations[0]
            player1.boundary.topright.x = screendim[0]
            player1.boundary.topright.y = 0
            player1.boundary.bottomleft.x = 0
            player1.boundary.bottomleft.y = platformsP1[stagenum][-1].topy()
            botplaty = 0
            topplaty = screendim[1]
            leftmostplatx = 0
            rightmostplatx = screendim[0]


    # print("left", player1.boundary.bottomleft.x)
    # print("right", player1.boundary.topright.x)

    if animTimer % 15 == 0:
        animTimer = 0
        if animNum % 2 == 0:
            animNum = 0
        animNum += 1
    animTimer += 1
    # print(animTimer)
    # print(animNum)

    if gameStart:
        for x in range(0, len(platformsP1[stagenum])):
            platformsP1[stagenum][x-1].draw()
        prizes[stagenum].imgdraw()
        player1.move(vectorx)
        player1.animate(playerOnGround)
        # print("waiting")
    # pygame.draw.circle(windowSurfaceObj, clrGreen, (int(player1.x), int(player1.y)), 5) #draws circle at bottom of player

    pygame.display.update()
    fpsClock.tick(60)