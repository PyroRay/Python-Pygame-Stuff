#Harper Kim
#Pixel Collision Assignment
#Python 2.7.17

import pygame, sys, math
from pygame.locals import *
from pygame import gfxdraw
from PIL import Image

pygame.init()
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Self Driving Car')

LeftTurn = (0, 0, 0)
RightTurn = (255, 255, 255)

track = pygame.image.load('TrackBG.jpg')
CollisionMap = Image.open('CollisionMap.jpg')

class car:
	def __init__(self):
		self.x = 100
		self.y = 300

		self.speed = 5
		self.direction = 0
		self.rad = 0

		self.image = pygame.image.load('Car.png')
		self.w = self.image.get_width()
		self.h = self.image.get_height()

		self.vertexlength = math.hypot(self.h / 2, self.w / 2) #length between the centre of car and vertex of car
		self.vertexangle = math.pi / 2 - math.atan2(self.h / 2, self.w / 2) #angle made with the centre of car and vertex of car
	
	def move(self):
		self.rad = self.direction * math.pi/180

		self.x += self.speed * math.sin(self.rad)
		self.y += self.speed * math.cos(self.rad)

		#sets a point at the left vertex of car and extends by 20 pixels
		self.leftx = self.x + (self.vertexlength + 20) * math.sin(self.rad + self.vertexangle)
		self.lefty = self.y + (self.vertexlength + 20) * math.cos(self.rad + self.vertexangle)

		#sets a point at the right vertex of car and extends by 20 pixels
		self.rightx = self.x + (self.vertexlength + 20) * math.sin(self.rad - self.vertexangle)
		self.righty = self.y + (self.vertexlength + 20) * math.cos(self.rad - self.vertexangle)

		rotated = pygame.transform.rotate(self.image, self.direction)
		rect = rotated.get_rect()
		rect.center = self.x, self.y

		screen.blit(rotated, rect)

	def turn(self):
		if CollisionMap.getpixel((self.rightx, self.righty)) == LeftTurn:
			self.direction += 5
		if CollisionMap.getpixel((self.leftx, self.lefty)) == RightTurn:
			self.direction -= 5

MyCar = car()
MyCar.move() #generate x, y, leftx, lefty, rightx, righty values

RunMe = True

while RunMe:
	for event in pygame.event.get():
		if event.type == QUIT:
			RunMe = False

	screen.blit(track, (0,0))
	MyCar.turn()
	MyCar.move()

	pygame.display.update()
	fpsClock.tick(60)

pygame.quit()