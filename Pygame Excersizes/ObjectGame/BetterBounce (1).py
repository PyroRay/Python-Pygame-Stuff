#Harper Kim
#Ball Bounce Method Assignment
#Python 2.7.17

import pygame, sys, math
from random import *

h=600
w=800

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Better Bounce Method Asignment")

clock = pygame.time.Clock()

ballList = []

def distance(obj1x, obj1y, obj2x, obj2y):
	return math.sqrt( ((obj1x - obj2x) ** 2) + ((obj1y - obj2y) ** 2) )

class ball:
	def __init__(self):

		self.radius = 10

		self.x = randint(0 + self.radius, w - self.radius)
		self.y = randint(0 + self.radius, h - self.radius)

		self.colour = (randint(0,255), randint(0,255), randint(0,255))
		
		self.angle = random() * 2 * math.pi
		self.speed = random() * 10

		self.xVelocity = math.cos(self.angle) * self.speed
		self.yVelocity = math.sin(self.angle) * self.speed

	def update(self):
		self.x += self.xVelocity
		self.y -= self.yVelocity
		self.nextx = self.x + self.xVelocity
		self.nexty =  self.y - self.yVelocity

		pygame.draw.circle(screen, (self.colour), (int(self.x), int(self.y)), self.radius, 0)
	
	def bounce(self):

		for i in ballList:

			if distance(self.nextx, self.nexty, i.nextx, i.nexty) < (self.radius + i.radius) and distance(self.nextx, self.nexty, i.nextx, i.nexty) != 0:
				self.angle = math.tan((self.nextx - i.nextx) / (self.nexty - i.nexty))
				i.angle = math.tan((i.nexty - self.nexty) / (i.nextx - self.nextx))
				#i.angle = math.tan((self.nexty - i.nexty) / (self.nextx - i.nextx) * -1)

				self.speed = abs(self.speed + i.speed) / 2 #averages speed between balls
				i.speed = self.speed #averages speed between balls

				self.xVelocity = math.cos(self.angle) * self.speed
				self.yVelocity = math.sin(self.angle) * self.speed
				i.xVelocity = math.cos(i.angle) * i.speed
				i.yVelocity = math.sin(i.angle) * i.speed

				self.nextx += self.xVelocity
				self.nexty -= self.yVelocity
				i.nextx += i.xVelocity
				i.nexty -= i.yVelocity

		if self.nextx > w - self.radius or self.nextx < 0 + self.radius:
			self.xVelocity *= -1
		elif self.nexty > h - self.radius or self.nexty < 0 + self.radius:
			self.yVelocity *= -1

for x in range(30):
	ballList.append(ball())

runGame = True

while runGame:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runGame = False

	screen.fill((0,0,0))

	for x in ballList:
		x.update()
	
	for y in ballList:
		y.bounce()

	pygame.display.update()
	clock.tick(60)

pygame.quit()