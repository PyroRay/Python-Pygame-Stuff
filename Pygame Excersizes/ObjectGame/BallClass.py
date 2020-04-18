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
screendim = pygame.display.get_surface().get_size()
#endregion

#region Classes

# class vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def magnitude(self):
#         return math.sqrt(x**2 + y**2)

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
playerbot = robot(10, clrWhite, screendim[0]//2, screendim[1]//2)

robots = []

#spawn robots
while numRobots > 0:
    # print(screendim[1])
    robots.append(robot(5, clrRed, random.randint(0, screendim[0]), screendim[1]//2,random.randint(-5,5),-1))
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
    #endregion

    #region Player Direction

    if up_pressed:
        playerbot.setdirection(None ,playerbot.direction.y - playerbot.speed)
        #playerbot.move(0,-playerbot.speed)
    if down_pressed:
        playerbot.setdirection(None ,playerbot.direction.y + playerbot.speed)
        #playerbot.move(0,playerbot.speed)
    if left_pressed:
        playerbot.setdirection(playerbot.direction.x - playerbot.speed,None)
        #playerbot.move(-playerbot.speed,0)
    if right_pressed:
        playerbot.setdirection(playerbot.direction.x + playerbot.speed,None)
        #playerbot.move(playerbot.speed,0)
    if playerbot.x < 0 or playerbot.x > screendim[0]:
        playerbot.setdirection(-playerbot.direction.x,None)
        #right_pressed = True
        #left_pressed = False
    #if playerbot.x > screendim[0]:
        #right_pressed = False
        #left_pressed = True
    if playerbot.y < 0 or playerbot.y > screendim[1]:
        playerbot.setdirection(None,-playerbot.direction.y)
        #up_pressed = False
        #down_pressed = True
    #if playerbot.y > screendim[1]:
        #up_pressed = True
        #down_pressed = False
        
    #endregion

    #region Robots Direction
    for i in range(len(robots)):
        # print(i)
        if timer % 240 == 0:    
            robots[i].setdirection(random.randint(-robots[i].speed,robots[i].speed),random.randint(-robots[i].speed,robots[i].speed))
        elif(robots[i].x > screendim[0]):
            robots[i].setdirection(-1)
        elif(robots[i].x < 0):
            robots[i].setdirection(1)
        if(robots[i].y <= 0 - 2*(delay)):
            robots[i].y = screendim[1] + delay
        if(robots[i].y >= screendim[1] + 2*(delay)):
            robots[i].y = 0 - delay
        #region collision
        impact = Vector2((playerbot.x- robots[i].x),(playerbot.y-robots[i].y)) # the vector pointing from bad ball to player 
        if impact.magnitude() <= (playerbot.radius + robots[i].radius): # then, we have impact
            # new direction vector for player = ndir_player 
            # ndir_player = dir_player + magnitude(dir_enemy)*cosɵ*impact_unit
            impact_unit = impact / impact.magnitude()
            cosTheta = robots[i].direction.dot(impact_unit) / robots[i].direction.magnitude()
            playerbot.direction = playerbot.direction +robots[i].direction.magnitude()*cosTheta*impact_unit
            robots[i].direction = robots[i].direction + playerbot.direction.magnitude()*cosTheta*(-impact_unit)
            up_pressed = False
            left_pressed = False
            right_pressed = False
            down_pressed = False
            # if robots[i].x > playerbot.x: # bad ball is to the right of player
            #     robots[i].setdirection(robots[i].speed)
            #     right_pressed = False
            #     left_pressed = True
            # elif robots[i].x < playerbot.x:
            #     robots[i].setdirection(-robots[i].speed)
            #     right_pressed = True
            #     left_pressed = False
            
            # if robots[i].y > playerbot.y:
            #     robots[i].setdirection(None, robots[i].speed)
            #     down_pressed = False
            #     up_pressed = True
            # elif robots[i].y < playerbot.y:
            #     robots[i].setdirection(None, -robots[i].speed)
            #     down_pressed = True
            #     up_pressed = False
        #endregion
        
        playerbot.move()
        robots[i].move()
        robots[i].draw()
    #endregion



    playerbot.draw()

    windowSurfaceObj.blit(playerbot.image, (int(playerbot.x - playerbot.radius),int(playerbot.y - playerbot.radius)))

    #region Ticks
    timer += 1
    pygame.display.update()
    fpsClock.tick(20)
    #endregion

#endregion