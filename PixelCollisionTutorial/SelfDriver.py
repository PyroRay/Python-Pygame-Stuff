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

import pygame
import sys
import math
import random
import os
from pygame.locals import *
from pygame import gfxdraw
from PIL import Image

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pixel Collision')

# define some coloured pens to draw with
clrWhite = (255, 255, 255)
clrBlack = (0, 0, 0)
clrGrey = (150, 150, 150)

LeftTurn = (0, 0, 0)
RightTurn = (255, 255, 255)

track = pygame.image.load('TrackBG.jpg')
CollisionMap = Image.open('CollisionMap2.jpg')


Count = 0
RunMe = True

print(CollisionMap.getpixel((200, 300)))
print(CollisionMap.getpixel((600, 300)))


class pixel:
	def __init__(self):
		self.R = 0
		self.B = 0
		self.G = 0
	def __gt__(self, pixel2):
		return math.sqrt(self.R**2+self.B**2+self.G**2) > math.sqrt(pixel2.R**2+pixel2.B**2+pixel2.G**2)
	def __lt__(self, pixel2):
		return math.sqrt(self.R**2+self.B**2+self.G**2) < math.sqrt(pixel2.R**2+pixel2.B**2+pixel2.G**2)
	def __et__(self, pixel2):
		return math.sqrt(self.R**2+self.B**2+self.G**2) == math.sqrt(pixel2.R**2+pixel2.B**2+pixel2.G**2)

class car:
	def __init__(self):
		self.x = 120
		self.y = 300
		self.speed = 1
		self.direction = 180
		self.image = pygame.image.load('Car.png')

	def move(self):
		rad = math.radians(self.direction)
		self.x += self.speed*math.sin(rad)
		self.y += self.speed*math.cos(rad)
		rotated = pygame.transform.rotate(self.image, self.direction)

		rect = rotated.get_rect()
		rect.center = self.x, self.y
		screen.blit(rotated, rect)
		#pygame.draw.circle(screen, clrGrey, (int(self.x), int(self.y)), 5)

	def turn(self, Count):
		directions=[self.direction,self.direction,self.direction] # initialize as three directions
		search_direction = self.direction
		search_sweep = 180  # 180 degrees sweeping spotlight
		shift_angle = search_sweep / 2
		pixel_counterclock, pixel_clockwise = pixel(), pixel()
		for search_radius in range(3,10,3): # `search_radius` is the starting search circle radius, goes (3→6→9)
			while (search_sweep > 1): # `search_direction` will point at the intended direction for the car given radius `search_radius`
				pixel_counterclock = CollisionMap.getpixel(((self.x-search_radius*math.cos(math.radians(search_direction))),(self.y-search_radius*math.sin(math.radians(search_direction)))))
				pixel_clockwise = CollisionMap.getpixel(((self.x+search_radius*math.cos(math.radians(search_direction))), (self.y+search_radius*math.sin(math.radians(search_direction)))))
				if(pixel_counterclock <= clrGrey and pixel_clockwise <= clrGrey): # whiteness: both search arrows are in the white
					search_direction += shift_angle
					shift_angle /= 2
				elif(pixel_counterclock > clrGrey and pixel_clockwise > clrGrey): # blackness: both search arrows are in the black 
					search_direction -= shift_angle
					shift_angle /= 2
				else: # split decision: `pixel_counterclock` was in black and `pixel_clockwise` was in the white, so narrow the sweep
					search_sweep /=2
					shift_angle = search_sweep
			directions[r/3-1]=search_direction
		# if the average diff between directions[0:2] `math.avg(directions[0]-directions[1],directions[1]-directions[2])` is negative and lesser that SOMENUMBER then, slow down and/or change direction more incrementally (i.e., `self.direction -= SMALLER_NUMBER`)
		# elif the average diff between directions[0:2] `math.avg(directions[0]-directions[1],directions[1]-directions[2])` is positive and greater that SOMENUMBER then, slow down and/or change direction more incrementally (i.e., `self.direction += SMALLER_NUMBER`)
		# (R, G, B) = CollisionMap.getpixel((self.x, self.y))
		# if (R + G + B) < 50:
		# 	self.direction -= 3
		# if (R + G + B) > 750:
		# 	self.direction += 3


MyCar = car()

while RunMe:

	for event in pygame.event.get():
		if event.type == QUIT:
			RunMe = False
			pygame.quit()

	Count += 1

	screen.blit(track, (0, 0))

	MyCar.turn(Count)
	MyCar.move()
	if Count > 15:
		print(MyCar.direction)
		Count = 0
		# os.system("pause")

	pygame.display.update()
	fpsClock.tick(60)
