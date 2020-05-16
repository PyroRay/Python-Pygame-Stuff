# Grumpy Ogre
# Collision Detection
# Using the python image library
# Getpixel and PutPixel functions
						
# Image is the python image library (pil) and it contains a number of useful
# tools for manipulating images. I've included the documentation for the pil
# in this folder. Have a read through it and see the possibilities. The three
# tools I use here are the methods getpixel(), putpixel(), and  save()
# getpixel returns the rgb values for a given pixel at a given location
# putpixel actually places a pixel of a given colour at the location provided
# save ... well duh it saves the image file (I use it for testing)

import pygame, sys, math, random
from pygame.locals import *
from pygame import gfxdraw
from PIL import Image

pygame.init()
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pixel Collision')

# define some coloured pens to draw with
clrWhite = (255,255,255)
clrBlack = (0,0,0)
clrGrey = (150, 150, 150)

LeftTurn = (0, 0, 0)
RightTurn = (255, 255, 255)

track = pygame.image.load('TrackBG.jpg')
CollisionMap = Image.open('CollisionMap2.jpg')
	
	
Count = 0
RunMe = True

print(CollisionMap.getpixel((200, 300)))
print(CollisionMap.getpixel((600, 300)))

class car:
	def __init__(self):
		self.x = 120
		self.y = 300
		self.speed = 1
		self.direction = 180 
		self.image = pygame.image.load('Car.png')
	
	def move(self):
		rad = self.direction * math.pi/180
		self.x += self.speed*math.sin(rad)
		self.y += self.speed*math.cos(rad)
		rotated = pygame.transform.rotate(self.image, self.direction)
		
		rect = rotated.get_rect()
		rect.center = self.x, self.y
		screen.blit(rotated, rect)
		#pygame.draw.circle(screen, clrGrey, (int(self.x), int(self.y)), 5)
		
	def turn(self, Count):
		(R, G, B) = CollisionMap.getpixel((self.x, self.y))
		if (R + G + B) < 50:
			self.direction -= 3 
		if (R + G + B) > 750:
			self.direction += 3 

MyCar = car()

while RunMe:
    	
	for event in pygame.event.get():
		if event.type == QUIT:
			RunMe = False
			pygame.quit()
	
	Count +=1

	screen.blit(track, (0,0))
	MyCar.turn(Count)
	MyCar.move()
	if Count > 15:
		Count =0



	pygame.display.update()
	fpsClock.tick(60)






