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
import Image

pygame.init()
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pixel Collision')

# define some coloured pens to draw with
clrWhite = (255,255,255)
clrBlack = (0,0,0)
clrGrey = (150, 150, 150)

Turn180 = (0, 0, 0)

track = pygame.image.load('TrackBG.jpg')
CollisionMap = Image.open('CollisionMap1.jpg')
	
	
Count = 0
RunMe = True

print(CollisionMap.getpixel((200, 300)))
print(CollisionMap.getpixel((600, 300)))

class car:
	def __init__(self):
		self.x = 100
		self.y = 300
		self.speed = 2
		self.direction = 90 
		self.image = pygame.image.load('Car.png')
	
	def move(self):
		rad = self.direction * math.pi/180
		self.x += self.speed*math.sin(rad)
		self.y += self.speed*math.cos(rad)
		rotated = pygame.transform.rotate(self.image, self.direction)
		rect = rotated.get_rect()
		rect.center = self.x, self.y
		screen.blit(rotated, rect)
	def turn(self):
		if CollisionMap.getpixel((self.x, self.y)) == Turn180:
			self.direction += 180 
			

MyCar = car()

while RunMe:
	Count +=1

	screen.blit(track, (0,0))
	MyCar.turn()
	MyCar.move()

	

#picCollisionZone.putpixel((SnowX[index], SnowY[index]-1), clrBlack)


	pygame.display.update()
	fpsClock.tick(60)






