# Ray Peng
# Platforming game
# Mr Blake

# 'W' to jump, 'A' to move left, 'D' to move right

# region imports

import pygame, sys, random, math, os
from pygame.locals import *

pygame.init()

# endregion

# region variables

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
_JUMPTIME = 20 # Constant value, num pixels player jumps per frame. that determines jump time (higher value means longer jump time)
_FALLSPEED = 5 # Constant value, num of pixels player falls per frame
_DEBUG = True
# highestplaty = screendim[1]
# lowestplaty = 0
# rightmostplatx = screendim[0]
# leftmostplatx = 0
vectorx = 0
vectory = 0
stagenum = 2
restart = False

# endregion

# region classes

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
    def __init__(self, color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, isfalling=False):
        # self.image = pygame.image.load('squirrel.png')
        self.direction = ""
        self.speed = speed
        self.isfalling = isfalling
        self.fallspeed = _FALLSPEED
        self.jumptime = _JUMPTIME # Determines jump time (higher value means longer jump time)
        self.jumpcounter = 0 # Tracks num of pixels the player gets to jump each frame
        self.onground = False
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
# The self.onground will change according to changes in diry, so lines 169-179 of move() will set self.onground
        if diry >= 0: # Going down OR not going at all
            # print(self.boty(self.y + diry))
            # print(self.boundary.bottomleft.y)
            if self.boty(self.y + diry) >= self.boundary.bottomleft.y: # check if hypothetical pos_y of player's bottom side is > bottom bounds
                # print("hello") 
                self.y = self.topy(self.boundary.bottomleft.y) # set bottom side to be at the bottom bound edge
                self.onground = True
            else:
                # print("whyyy")
                self.y += diry
                self.onground = False
        elif diry < 0: # Going up
            # print(self.topy(self.y + diry), self.boundary.topright.y)
            if self.topy(self.y + diry) < self.boundary.topright.y: # check if hypothetical pos_y of player's top side is < top bounds
                self.y = self.boty(self.boundary.topright.y) # set top side to be at the top bound edge
            else:
                self.y += diry
                
        # self.x += dirx
        # self.y += diry
    def animate(self, onground):
        # selects image to show based on action and animation timer
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

# endregion

# region character create

# (color, height, width, xset, yset, rightbound, topbound, leftbound, botbound, speed, falling=False) # constructor
player1 = Player(clrWhite, 100, 50, 25, 600, screendim[0], 0, 0, screendim[1], 10)

# endregion

# region Stages

platformsP1 = [[Platform(clrDrkGrey, 40, 100, 200, 600, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 800, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 500, 575, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 400, 40, screendim[0], 520, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 150, 1205, 320, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])], \
    [Platform(clrDrkGrey, 40, 800, 600, 250, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 100, 450, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 800, 550, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 100, 500, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 500, 40, 1100, 470, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])], \
        [Platform(clrDrkGrey, 40, 50, 200, 600, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 50, 800, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 50, 500, 575, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 500, 1100, 320, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 600, 40, 870, 500, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 500, 501, 321, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, 400, 690, 180, screendim[0], 0, 0, screendim[1]), Platform(clrDrkGrey, 40, screendim[0], screendim[0]//2, screendim[1], screendim[0], 0, 0, screendim[1])]]\
             # creates array of stages and then a sub-array of platforms in that stage

prizes = [Prize(clrGreen, 120, 60, 1205, 240, screendim[0], 0, 0, screendim[1]), Prize(clrGreen, 120, 60, 1205, 640, screendim[0], 0, 0, screendim[1]), Prize(clrGreen, 120, 60, 1205, 240, screendim[0], 0, 0, screendim[1])] #creates array of prize locations for each stage
spawnlocation = [600, 25] # where the player will spawn in each level

# endregion

# region functions

def onGround(plr):
    platnum = 0
    for platform in platformsP1[stagenum]:
        platnum += 1
        # print(platnum)
        if platform.leftx() < plr.rightx() and platform.rightx() > plr.leftx():
            # print("in bounds")
            # print(topplaty, int(platform.topy()))
            if highestplaty == platform.topy():
                if int(platform.topy()) == int(plr.boty()):
                    # print("on plat")
                    return True
                else:
                    pass
                    # we don't yet know if the player isn't on another platform, so it is premature to return False
    return False # now we've checked all platforms, so it's safe to conclude player isn't on a platform

def jump(plr, jumpcount):
    plr.move(0, -jumpcount)
    
# endregion

# region main game

while runGame:

    # region start

    if gameStart:
        windowSurfaceObj.blit(bckgrdImage, (0, 0))
        pygame.mixer.music.set_volume(0.05)
    else:
        if restart:
            windowSurfaceObj.blit(restartmenu, (0, 0))
            pygame.mixer.music.set_volume(0.1)
        else:
            windowSurfaceObj.blit(startmenu, (0, 0))

    # endregion

    # region events
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
    # endregion

    # region movements

    vectorx = 0

    if left_pressed:
        vectorx = (-player1.speed)
    elif right_pressed:
        vectorx = (player1.speed)

    player1.move()
    # print(playerOnGround)

    if player1.onground and not(up_pressed): # player is on the ground
        player1.fallspeed = 5 # resets the velocity of fall
        player1.isfalling = False # player stops falling
        player1.jumpcounter = player1.jumptime # resets to the player's jump power
    elif up_pressed: # if player presses 'w'
        jump(player1, player1.jumpcounter)
        player1.jumpcounter -= 1
    elif not(player1.onground) and not(up_pressed): # if player is in air and lets go of 'w'
        player1.isfalling = True # player starts falling
        # player1.jumpcounter = -5 # prevents player from 'jumping' in the air

    # endregion

    # region bounds

    platnum2 = 0
    for x in range(0, len(platformsP1[stagenum])):
        # platnum2 += 1

        if platformsP1[stagenum][x].leftx() < player1.rightx() and platformsP1[stagenum][x].rightx() > player1.leftx(): # check if player is within horizontal range of platform (the player can stand or hit head on the platform)
            if platformsP1[stagenum][x].topy() < player1.boundary.bottomleft.y: # highestplaty: # checks if platform is higher than highest platform in that X area
                if player1.boty() <= platformsP1[stagenum][x].topy(): # checks if player is actually above platform
                    player1.boundary.bottomleft.y = platformsP1[stagenum][x].topy() #  sets player bottom boundary
                    if _DEBUG:
                        print("New Bottom Boundary", x, "=", player1.boundary.bottomleft.y)
                    # highestplaty = platform.topy() # sets highest platform to current platform Y
            # if highestplaty == platform.topy(): # checks if highest platform is the current platform
            #     if player1.boty() <= platform.topy(): # checks if player is actually above platform
            #         player1.boundary.bottomleft.y = highestplaty # sets player bottom boundary

            if platformsP1[stagenum][x].boty() > player1.boundary.topright.y: # lowestplaty: # checks if platform is lower than lowest platform in that X area
                if player1.topy() >= platformsP1[stagenum][x].boty(): # checks if player is actually below platform
                    player1.boundary.topright.y = platformsP1[stagenum][x].boty() # sets player top boundary
                    if _DEBUG:
                        print("New Top Boundary", x, "=", player1.boundary.topright.y)
                    # lowestplaty = platform.boty() # sets lowest platform to current platform Y
                # if lowestplaty == platform.boty(): # checks if lowest platform is the current platform
                #     if player1.topy() >= platform.boty(): # checks if player is actually below platform
                        

        else: # if not in the bounds of specified platform
            if player1.boundary.bottomleft.y == platformsP1[stagenum][x].topy(): # checks if highest platform is current platform
                player1.boundary.bottomleft.y = screendim[1] # resets bottom boundary
                if _DEBUG:
                    print("reset bottom boundary")
                # highestplaty = screendim[1] # resets highest platform
            if player1.boundary.topright.y == platformsP1[stagenum][x].boty(): # checks if lowest platform is current platform
                player1.boundary.topright.y = 0 # resets top boundary
                if _DEBUG:
                    print("reset top boundary")
                # lowestplaty = 0 # resets lowest platform

    if player1.isfalling:
        player1.move(0, player1.fallspeed)
        player1.fallspeed += 1

    for x in range(0, len(platformsP1[stagenum])): # update boundaries according to nearest platforms
        if _DEBUG:
            print("Examining platform ", x,"...")

        if platformsP1[stagenum][x].topy() < player1.boty() and platformsP1[stagenum][x].boty() > player1.topy(): # check if player is within vertical range of platform (can run into the edge of platform)
            if _DEBUG:
                print("Player can run into platform ", x)

            if platformsP1[stagenum][x].leftx() < player1.boundary.topright.x: # rightmostplatx: # checks if platform is further right than rightmost platform in that Y area
                if _DEBUG:
                    print("Platform ", x," is further right than previous rightmost platform")
                if player1.rightx() <= platformsP1[stagenum][x].leftx(): # checks if player is actually to the left of platform
                    player1.boundary.topright.x = platformsP1[stagenum][x].leftx() # sets rightmost platform to current platform X
                    if _DEBUG:
                        print("Player was to left of platform %d, so new R bound: %.1f" %(x,player1.boundary.topright.x))

            if platformsP1[stagenum][x].rightx() > player1.boundary.bottomleft.x: # leftmostplatx: # checks if platform is further left than leftmost platform in that Y area
                if _DEBUG:
                    print("Platform ", x," is further left than previous leftmost platform")
                if player1.leftx() >= platformsP1[stagenum][x].rightx(): # checks if player is actually to the right of platform
                    player1.boundary.bottomleft.x = platformsP1[stagenum][x].rightx() # sets leftmost platform to current platform X
                    if _DEBUG:
                        print("Player was to right of platform %d, so new L bound: %.1f" %(x,player1.boundary.bottomleft.x))

        else: # if not in the bounds of specified platform
            if _DEBUG:
                print("Player cannot run into platform ", x)
            if player1.boundary.bottomleft.x == platformsP1[stagenum][x].rightx(): # checks if leftmost platform is current platform
                player1.boundary.bottomleft.x = 0 # resets left boundary
                if _DEBUG:
                    print("reset left boundary")
                # leftmostplatx = 0 # resets leftmost platform
                
            if player1.boundary.topright.x == platformsP1[stagenum][x].leftx(): # checks if rightmost platform is current platform
                player1.boundary.topright.x = screendim[0] # resets right boundary
                if _DEBUG:
                    print("reset right boundary")
                # rightmostplatx = screendim[0] # resets rightmost platform

    # endregion

    #region collectprize

    if player1.x > prizes[stagenum].leftx() and player1.x < prizes[stagenum].rightx() and player1.y < prizes[stagenum].boty() and player1.y > prizes[stagenum].topy(): # if centre of player is in prize bounds
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(dir_path + r'\Sounds\Sound Effects\prizecollect.wav')) # play collection noise
        pygame.mixer.Channel(2).set_volume(0.3) # lower volume
        if stagenum + 1 >= len(prizes): # if the stage number is larger than the number of prizes
            gameStart = False # end game
            stagenum = -1 # reset stages
            restart = True # change title screen
        else: # if normal collection of prize
            stagenum += 1 # go to next stage 
            player1.x = spawnlocation[1] # reset everything else
            player1.y = spawnlocation[0]
            player1.boundary.topright.x = screendim[0]
            player1.boundary.topright.y = 0
            player1.boundary.bottomleft.x = 0
            player1.boundary.bottomleft.y = platformsP1[stagenum][-1].topy()
            lowestplaty = 0
            highestplaty = screendim[1]
            leftmostplatx = 0
            rightmostplatx = screendim[0]
    
    # endregion

    # region draw

    if animTimer % 15 == 0:
        animTimer = 0
        if animNum % 2 == 0:
            animNum = 0
        animNum += 1
    animTimer += 1

    if gameStart:
        for x in range(0, len(platformsP1[stagenum])):
            platformsP1[stagenum][x-1].draw()
        prizes[stagenum].imgdraw()
        player1.move(vectorx)
        player1.animate(player1.onground)

    # endregion

    pygame.display.update()
    fpsClock.tick(60)

# endregion