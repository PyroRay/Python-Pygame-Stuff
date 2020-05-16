# Car Demo by Richard Jones
#   -Game Timing
#   -Object rotation
#   -Shortenend key input
#   -Sound objects
#   -Functional "exit" ... so far so good anyways!!!


# -~-~-~-~-~-~-~-~-~-~Various Declarations and Imports-~-~-~-~-~-~-~-
import pygame, math, sys
from pygame.locals import *
pygame.init()

winScreen = pygame.display.set_mode((800, 600))
car = pygame.image.load('Car.png')
track = pygame.image.load('TrackBG.jpg').convert()

clock = pygame.time.Clock()
k_up = k_down = k_left = k_right = 0
speed = direction = 0
position = (130, 200)

TURN_SPEED = 1
ACCELERATION = 1
MAX_FORWARD_SPEED = 4
MAX_REVERSE_SPEED = 0
BLACK = (0,0,0)
sndScreech = pygame.mixer.Sound("CARBRAKE.WAV")

# Add these
xTarget = 750
yTarget = 350
sndFart = pygame.mixer.Sound('raspberryfart.wav')

def distance(X1, Y1, X2, Y2):
    # dist formula sqrt((x2-x1)^2+(y2-y1)^2)
    return math.sqrt(math.pow((X1-X2), 2) + math.pow((Y1-Y2),2))

# -~-~-~-~-~-~-~-~-~-~ Game Loop-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
while 1:
# Step 1: set the fps of the game
    clock.tick(60)
    

# Step 2: check for keyboard events
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN # key down or up?
        if event.key == K_RIGHT:
            k_right = down * -3
            #sndScreech.play()
        elif event.key == K_LEFT:
            k_left = down * 3
            #sndScreech.play()
        elif event.key == K_UP:
            k_up =  down * 2
        elif event.key == K_DOWN:
            k_down = down * -1
        elif event.key == K_ESCAPE:
            sys.exit(0) # quit the game

# Step 3: set the speed, direction, acceleration and orientation of car
    speed += (k_up + k_down)
    k_up = k_down = 0 
    if speed > MAX_FORWARD_SPEED: speed = MAX_FORWARD_SPEED
    if speed < MAX_REVERSE_SPEED: speed = MAX_REVERSE_SPEED
    direction += (k_right + k_left)
    x, y = position
    rad = direction * math.pi / 180
    x += speed*math.sin(rad)
    y += speed*math.cos(rad)
    position = (x, y)
    # .. rotate the car image for direction
    rotated = pygame.transform.rotate(car, direction)
    # .. position the car on screen
    rect = rotated.get_rect()
    rect.center = position
  
    if distance(x, y, xTarget, yTarget) < 50:
        sndFart.play()
  
# Step 4: Render the car, background and flip
    winScreen.blit(track, (0,0))
    #Add this
    pygame.draw.circle(winScreen, (0,0,0), (xTarget, yTarget), 50, 5)
    
    winScreen.blit(rotated, rect)
    pygame.display.flip()
pygame.quit()
