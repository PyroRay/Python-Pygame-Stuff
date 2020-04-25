#Ray Peng
#Better Ball Game with Semi-working Angular Mathematics
#Mr. Blake
#2D Game Design 12

#note: some random crashes may occur - not sure how to fix them

#region Imports
import pygame, sys, random, math
from pygame.locals import *
from pygame.math import Vector2
pygame.init()
#endregion

#region Defining Variables
windowSurfaceObj = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Object Game')
clrBlack = pygame.Color(0, 0, 0)
clrRed = pygame.Color(255, 0, 0)
clrWhite = pygame.Color(255, 255, 255)
fpsClock = pygame.time.Clock()
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
delay = 20 # How many pixels off screen the robot will be when it wraps around to the bottom from top
timer = 0
numRobots = 30
maxspeed = 10
screendim = pygame.display.get_surface().get_size()
#endregion

#region Classes

class robot:
    def __init__(self, speed, colorset, xset, yset, dirx=0, diry=0):
        self.image = pygame.image.load('squirrel.png')
        self.radius = 15 #basically the size
        self.set(speed,colorset,xset,yset)
        self.direction = Vector2(dirx, diry)
        self.speed = speed

    def setdirection(self,dirx=None,diry=None):
        if(dirx != None):
            self.direction.x = dirx
        if(diry != None):
            self.direction.y = diry

    def move(self, dirx=None, diry=None):
        if(dirx == None):
            self.x += self.direction.x
        else:
            self.x += dirx
        if(diry == None):
            self.y += self.direction.y
        else:
            self.y += diry

    def draw(self):
        pygame.draw.circle(windowSurfaceObj, (self.color), (int(self.x), int(self.y)), self.radius)

    def set(self, speed, colorset, xset, yset,dirx=0,diry=0):
        self.speed = speed
        self.color = colorset
        self.x = xset
        self.y = yset
        self.direction = Vector2(dirx,diry)

    def setXY(self, xset, yset):
        self.set(self.color, xset, yset)
#endregion

#region Robot Spawning
playerbot = robot(5, clrWhite, screendim[0]//2, screendim[1]//2, 0, 0.1)

robots = []

#spawn robots
while numRobots > 0:
    # print(screendim[1])
    robots.append(robot(5, clrRed, random.randint(0, screendim[0]), random.randint(0, screendim[1]),random.choice((-5,5)),-1))
    numRobots-= 1

#endregion

#region Main Game Loop
while True:
    windowSurfaceObj.fill(clrBlack)	

    #region Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                # print("\'w\' key was pressed")
                up_pressed = True
                left_pressed = False
                down_pressed = False
                right_pressed = False
            elif event.key == pygame.K_a:
                # print("\'a\' key was pressed")
                up_pressed = False
                left_pressed = True
                down_pressed = False
                right_pressed = False
            elif event.key == pygame.K_s:
                # print("\'s\' key was pressed")
                up_pressed = False
                left_pressed = False
                down_pressed = True
                right_pressed = False
            elif event.key == pygame.K_d:
                # print("\'d\' key was pressed")
                up_pressed = False
                left_pressed = False
                down_pressed = False
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

    #region Player Direction

    if up_pressed:
        playerbot.setdirection(0 ,-playerbot.speed)
    if down_pressed:
        playerbot.setdirection(0 ,playerbot.speed)
    if left_pressed:
        playerbot.setdirection(-playerbot.speed, 0)
    if right_pressed:
        playerbot.setdirection(playerbot.speed, 0)
    if playerbot.x < 0 or playerbot.x > screendim[0]:
        playerbot.setdirection(-playerbot.direction.x,None)
    if playerbot.y < 0 or playerbot.y > screendim[1]:
        playerbot.setdirection(None,-playerbot.direction.y)
        
    #endregion

    #region Robots Direction
    for i in range(len(robots)):
        if(robots[i].x >= screendim[0] + 2*(delay)):
            robots[i].x = 0 - delay
        elif(robots[i].x <= 0 - 2*(delay)):
            robots[i].x = screendim[0] + delay
        if(robots[i].y <= 0 - 2*(delay)):
            robots[i].y = screendim[1] + delay
        elif(robots[i].y >= screendim[1] + 2*(delay)):
            robots[i].y = 0 - delay
        if(robots[i].direction.x > maxspeed or robots[i].direction.x < -maxspeed):
            robots[i].setdirection(robots[i].direction.x/1.5)
        elif(robots[i].direction.y > maxspeed or robots[i].direction.y < -maxspeed):
            robots[i].setdirection(None, robots[i].direction.y/1.5)
        #region collision
        impact = Vector2((playerbot.x- robots[i].x),(playerbot.y-robots[i].y)) # the vector pointing from bad ball to player 
        if impact.magnitude() <= (playerbot.radius + robots[i].radius): # then, we have impact
            # new direction vector for player = ndir_player 
            # ndir_player = dir_player + magnitude(dir_enemy)*cosɵ*impact_unit
            impact_unit = impact / impact.magnitude()
            cosTheta = robots[i].direction.dot(impact_unit) / robots[i].direction.magnitude() + 0.000000000000002
            plrdir = playerbot.direction
            robdir = robots[i].direction
            playerbot.direction = robdir.magnitude()*math.acos(cosTheta)*impact_unit
            robots[i].direction = plrdir.magnitude()*math.acos(cosTheta)*(-impact_unit)
            up_pressed = False
            left_pressed = False
            right_pressed = False
            down_pressed = False
        #endregion
        robots[i].move()
        robots[i].draw()
    #endregion


    playerbot.move()
    playerbot.draw()

    windowSurfaceObj.blit(playerbot.image, (int(playerbot.x - playerbot.radius),int(playerbot.y - playerbot.radius)))

    #region Ticks
    timer += 1
    pygame.display.update()
    fpsClock.tick(60)
    #endregion

#endregion