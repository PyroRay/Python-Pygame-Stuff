
#region Imports
import pygame, sys, random, math
from pygame.locals import *
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
numRobots = 5
_playerspeed=3
screendim = pygame.display.get_surface().get_size()
#endregion

#region Classes

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return math.sqrt(x**2 + y**2)

class robot:
    def __init__(self, colorset, xset, yset, dirx=0, diry=0):
        self.radius = 15
        self.set(colorset,xset,yset)
        self.direction = vector(dirx, diry)

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
        pygame.draw.circle(windowSurfaceObj, (self.color), (self.x, self.y), self.radius)

    def set(self, colorset, xset, yset,dirx=0,diry=0):
        self.color = colorset
        self.x = xset
        self.y = yset
        self.direction = vector(dirx,diry)

    def setXY(self, xset, yset):
        self.set(self.color, xset, yset)
#endregion

#region Functions
# def badrobotmovement(badrobot, timer, badrobotdirection, directions):
#     if timer % 120 == 0:
#         badrobotdirection = random.choice(directions)
#     else:
#         if badrobot.x > screendim[0]:
#             badrobotdirection = "slowright"
#         elif badrobot.x < 0:
#             badrobotdirection = "slowleft"
    
#     return badrobotdirection
#endregion

#region Robot Spawning
playerbot = robot(clrWhite, screendim[0]//2, screendim[1]//2)

robots = []

#spawn robots
while numRobots > 0:
    # print(screendim[1])
    robots.append(robot(clrRed, random.randint(0, screendim[0]), screendim[1] + 20,random.randint(-1,1),-1))
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

    #region Player Direction
    if up_pressed:
        playerbot.move(0,-_playerspeed)
    if down_pressed:
        playerbot.move(0,_playerspeed)
    if left_pressed:
        playerbot.move(-_playerspeed,0)
    if right_pressed:
        playerbot.move(_playerspeed,0)
    #endregion

    #region Robots Direction
    for i in range(len(robots)):
        # print(i)
        # if hero bot is in contact with robots[i], hero loses 1 life and robots[i] moves opposite direction
        # hero bot x + radius 
        if timer % 120 == 0: # every 2 seconds, randomly change direction of robot
            robots[i].setdirection(random.randint(-1,1),random.randint(-_playerspeed,-1))
        elif(robots[i].x > screendim[0]): # if robot near right edge of screen, move it left
            robots[i].setdirection(-1)
        elif(robots[i].x < 0): # if robot near left edge of screen, move it right
            robots[i].setdirection(1)
        if(robots[i].y <= 0): # if the robot is at top of screen, wrap it around to bottom
            robots[i].y = screendim[1] + delay # 'delay' is the space below the screen where the robot starts
        robots[i].move()
        robots[i].draw()
    #endregion

    playerbot.draw()


    #region Ticks
    timer += 1
    pygame.display.update()
    fpsClock.tick(120)
    #endregion

#endregion