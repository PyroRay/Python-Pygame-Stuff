import pygame, sys, random, math
from pygame.locals import *
pygame.init()

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
timer = 0
directions = ("slowleft", "slowright")
numRobots = 3
screendim = pygame.display.get_surface().get_size()
# badrobot = ()
# badrobot1direction = ""
# badrobot2direction = ""


class robot:
    def __init__(self, colorset, xset, yset):
        self.radius = 15
        self.set(colorset,xset,yset)

    def move(self, direction):
        if direction == "up":
            self.y -= 3
        elif direction == "down":
            self.y += 3
        elif direction == "left":
            self.x -= 3
        elif direction == "right":
            self.x += 3
        elif direction == "slowup":
            self.y -= 1
        elif direction == "slowdown":
            self.y += 1
        elif direction == "slowleft":
            self.x -= 1
        elif direction == "slowright":
            self.x += 1

    def draw(self):
        pygame.draw.circle(windowSurfaceObj, (self.color), (self.x, self.y), self.radius)

    def set(self, colorset, xset, yset):
        self.color = colorset
        self.x = xset
        self.y = yset

    def setXY(self, xset, yset):
        self.set(self.color, xset, yset)

def badrobotmovement(badrobot, timer, badrobotdirection, directions):
    if timer % 120 == 0:
        badrobotdirection = random.choice(directions)
    
    return badrobotdirection

playerbot = robot(clrWhite, screendim[0]//2, screendim[1]//2)

robots = []


while numRobots > 0:
    robots.append(robot(clrRed, screendim[1] + 20, random.randint(0, screendim[0])))
    numRobots-= 1
    
print(len(robots))

# badrobot1 = robot()
# badrobot1.color = clrRed
# badrobot1.x = pygame.display.get_surface().get_size()[0]//3
# badrobot1.y = pygame.display.get_surface().get_size()[1]//2

# badrobot2 = robot()
# badrobot2.color = clrRed
# badrobot2.x = pygame.display.get_surface().get_size()[0]//3
# badrobot2.y = pygame.display.get_surface().get_size()[1]//2

while True:
    windowSurfaceObj.fill(clrBlack)	
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

    if timer % 180 == 0:
        print("hello")

    if up_pressed:
        playerbot.move("up")
    if down_pressed:
        playerbot.move("down")
    if left_pressed:
        playerbot.move("left")
    if right_pressed:
        playerbot.move("right")

    # if timer > 120:
    #     timer = 0

    # badrobot1direction = badrobotmovement(badrobot1, timer, badrobot1direction, directions)
    # badrobot1.move(badrobot1direction)
    # badrobot1.move("slowup")
    # badrobot2direction = badrobotmovement(badrobot2, timer, badrobot2direction, directions)
    # badrobot2.move(badrobot2direction)
    # badrobot2.move("slowup")
    
    playerbot.draw()
    # badrobot1.draw()
    # badrobot2.draw()
    timer += 1

    pygame.display.update()
    fpsClock.tick(60)
