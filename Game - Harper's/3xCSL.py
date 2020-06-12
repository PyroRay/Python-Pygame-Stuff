#Final Project
#3xCSL
#Python 2.7.18
#Harper Kim

#region Imports

import pygame, sys, math
from pygame import *
from random import *
from ImageManager import image_list
from StageData import stage_data
from CharacterData import character_data

#endregion

#region Init

pygame.init()

screen_dimensions = Vector2(1280, 720)

def v2_to_int_tuple(vector):
	return int(vector.x), int(vector.y)

def loc_to_draw_loc(location, offset):
	return Vector2(location.x - (offset.x / 2), screen_dimensions.y - (location.y + offset.y / 2))

game_screen = pygame.display.set_mode(v2_to_int_tuple(screen_dimensions))
screen_centre = screen_dimensions / 2
pygame.display.set_caption("3xCSL")

monospace = pygame.font.SysFont("monospace", 50)
title_image = pygame.image.load("Title.png")#.convert_alpha()

character_choice = [0,0]
mapnumber = 0

game_clock = pygame.time.Clock()
game_state = "init"



#endregion

#region Classes

class Player:

	def __init__(self, number):
		self.lives = 3

		self.number = number
		self.charnumber = character_choice[number]

		self.weight = character_data[self.charnumber]["stats"]["weight"]

		self.walkspeed = character_data[self.charnumber]["stats"]["walkspeed"]
		self.airspeed = character_data[self.charnumber]["stats"]["airspeed"]
		self.jumpspeed = character_data[self.charnumber]["stats"]["jumpspeed"]
		self.fallspeed = character_data[self.charnumber]["stats"]["fallspeed"]

		self.dimensions = character_data[self.charnumber]["stats"]["dimensions"]

	def spawn(self):
		self.state = "air"
		self.substate = "idle"
		self.direction = "right"

		self.percent = 0.0

		self.jump = False
		self.onterrain = 0
		
		self.animationframe = 0

		self.location = Vector2(screen_centre.x, screen_dimensions.y)
		self.velocity = Vector2(0,0)
		self.acceleration = Vector2(0,0)

	def check(self):
		if keydic[self.number]["up"] and self.jump:
				self.jump = False
				self.state = "air"
				self.substate = "idle"
				self.velocity.y = self.jumpspeed
				self.velocity.x = 0
				if keydic[self.number]["left"]:
					self.direction = "left"
					self.velocity.x = -self.walkspeed
				elif keydic[self.number]["right"]:
					self.velocity.x = self.walkspeed
					self.direction = "right"
		
		elif self.state == "air":
			if keydic[self.number]["down"]:
				self.acceleration.y = -self.fallspeed * 3
			else:
				self.acceleration.y = -self.fallspeed
			if True:
				if self.substate == "attack":
					if self.animationframe <= self.attackframes:
						self.animationframe += 1
					else:
						self.substate = "idle"
						self.animationframe = 0
				elif keydic[self.number]["attack"]:
					self.attack()

			if keydic[self.number]["left"]:
				if self.velocity.x > -self.airspeed:
					self.velocity.x -= 2
					self.direction = "left"
			elif keydic[self.number]["right"]:
				if self.velocity.x < self.airspeed:
					self.velocity.x += 2
					self.direction = "right"
			if abs(self.velocity.x) > self.walkspeed:
				self.velocity.x *= 0.8
			self.acceleration.x *= 0.8
			self.acceleration.y *= 0.5
			
		elif self.state == "ground":
			if keydic[self.number]["down"] and terrain_list[self.onterrain].platform:
				self.location.y -= self.fallspeed * 2
				self.state = "air"
				self.substate = "drop"
			else:
				self.location.y = terrain_list[self.onterrain].topbound + hurtbox_list[self.number].radius
				if self.substate == "attack":
					self.velocity.x *= 0.5
					if self.animationframe <= self.attackframes:
						self.animationframe += 1
					else:
						self.substate = "idle"
						self.animationframe = 0
				elif self.substate == "idle" and keydic[self.number]["attack"]:
					self.attack()
				elif keydic[self.number]["left"]:
					self.substate = "walk"
					self.direction = "left"
					if self.velocity.x > -self.walkspeed:
						self.velocity.x -= 4
				elif keydic[self.number]["right"]:
					self.substate = "walk"
					self.direction = "right"
					if self.velocity.x < self.walkspeed:
						self.velocity.x += 4
				else:
					self.substate = "idle"
					self.velocity.x *= 0.5
				self.acceleration.x *= 0.2
	
	def attack(self):
		self.substate = "attack"
		keydic[self.number]["attack"] = False

		if keydic[self.number]["up"]:
			self.attackdirection = "up"
		elif keydic[self.number]["down"] and self.state == "air":
			self.attackdirection = "down"
		elif keydic[self.number]["left"]:
			self.attackdirection = "left"
		elif keydic[self.number]["right"]:
			self.attackdirection = "right"
		else:
			self.attackdirection = self.direction
		
		self.animationframe = 0
		self.attackframes = character_data[self.charnumber]["attacks"][self.attackdirection]["attackframes"]

		for x in range(len(character_data[self.charnumber]["attacks"][self.attackdirection]["hitboxes"])):
			hitbox_list.append(Hitbox(self.number, self.charnumber, x, self.attackdirection))
	
	def draw(self):
		pygame.draw.rect(game_screen, (0,0,0), (v2_to_int_tuple(loc_to_draw_loc(self.location, self.dimensions)), v2_to_int_tuple(self.dimensions)), 0)

	def update(self):

		self.check()

		self.velocity += self.acceleration
		self.location += self.velocity

		self.draw()
		
		
		

class Hurtbox:
	def __init__(self, owner):
		self.owner = owner
		self.radius = player_list[self.owner].dimensions.x / 2
		self.location = None
		self.nextlocation = None
		self.distance = None

	def update(self):
		self.location = player_list[self.owner].location
		self.nextlocation = player_list[self.owner].location + player_list[self.owner].velocity

		self.check()

		pygame.draw.circle(game_screen, (0,255,0), (v2_to_int_tuple(loc_to_draw_loc(self.location, Vector2(0,0)))), int(self.radius))

	def check(self):
		if player_list[self.owner].state == "air" and player_list[self.owner].substate == "walk":
			player_list[self.owner].substate = "idle"
		player_list[self.owner].state = "air"

		for i in terrain_list:
			if (self.nextlocation.y <= i.topbound + self.radius and self.nextlocation.y > i.botbound - self.radius) and (self.nextlocation.x < i.rightbound + self.radius and self.nextlocation.x > i.leftbound - self.radius):
				if self.location.x > i.rightbound + self.radius:
					player_list[self.owner].location.x = i.rightbound + self.radius
					player_list[self.owner].velocity.x = 0
					player_list[self.owner].acceleration.x = 0
				elif self.location.x < i.leftbound - self.radius:
					player_list[self.owner].location.x = i.leftbound - self.radius
					player_list[self.owner].velocity.x = 0
					player_list[self.owner].acceleration.x = 0

				if player_list[self.owner].velocity.y > 0 and not i.platform:
					player_list[self.owner].location.y = i.botbound - self.radius
					player_list[self.owner].velocity.y = 0
					player_list[self.owner].acceleration.y = 0
				elif player_list[self.owner].velocity.y <= 0 and not (keydic[self.owner]["down"] and i.platform) and not (player_list[self.owner].substate == "drop" and player_list[self.owner].onterrain == i.number):
					player_list[self.owner].jump = True
					player_list[self.owner].onterrain = i.number
					player_list[self.owner].state = "ground"
					player_list[self.owner].velocity.y = 0
					player_list[self.owner].acceleration.y = 0

		for i in hitbox_list:
			if i.owner != self.owner and i.enabled:
				if Vector2.distance_to(self.location, i.location) < (self.radius + i.radius):
					for x in hitbox_list:
						if i.owner == x.owner and i.direction == x.direction:
							x.enabled = False
					player_list[self.owner].acceleration = i.knockback + Vector2(i.knockback.x * i.multiplyer * (2 - player_list[self.owner].weight) * (player_list[self.owner].percent / 100.0), i.knockback.y * i.multiplyer * (2.0 - player_list[self.owner].weight) * (player_list[self.owner].percent / 100.0))
					print(player_list[self.owner].acceleration, i.knockback, i.multiplyer, 2 - player_list[self.owner].weight, player_list[self.owner].percent / 100.0)
					player_list[self.owner].percent += i.damage
					player_list[self.owner].velocity = Vector2(0,0)
		
		if self.location.x < -150 or self.location.x > screen_dimensions.x + 150 or self.location.y < -150 or self.location.y > screen_dimensions.y + 150:
			player_list[self.owner].lives -= 1
			player_list[self.owner].spawn()

class Hitbox:
	def __init__(self, owner, character, number, direction):
		self.owner = owner
		self.number = number
		self.character = character
		self.direction = direction
		self.enabled = True
		self.animationframe = 0
		
		self.lock = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["lock"]

		self.damage = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["damage"]		
		self.knockback = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["knockback"]
		self.multiplyer = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["multiplyer"]

		self.radius = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["radius"]
		self.offset = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["offset"]
		self.velocity = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["velocity"]

		self.location = player_list[self.owner].location + self.offset
		
		self.duration = character_data[self.character]["attacks"][self.direction]["hitboxes"][self.number]["duration"]

	def update(self):
		if self.animationframe <= self.duration:
			self.animationframe += 1
		elif self.enabled:
			self.enabled = False

		if self.lock:
			self.location = player_list[self.owner].location + self.offset
		else:
			self.location += self.velocity

		if self.enabled:
			pygame.draw.circle(game_screen, (255,0,0), (v2_to_int_tuple(loc_to_draw_loc(self.location, Vector2(0,0)))), self.radius)
		

class Terrain:
	def __init__(self, mapnumber, number):
		self.number = number
		self.map = mapnumber

		self.platform = stage_data[self.map][self.number]["platform"]
		self.dimensions = stage_data[self.map][self.number]["dimensions"]
		self.location = stage_data[self.map][self.number]["location"]
		self.velocity = stage_data[self.map][self.number]["velocity"]
		self.minloc = stage_data[self.map][self.number]["minimum"]
		self.maxloc = stage_data[self.map][self.number]["maximum"]
		
		self.leftbound = self.location.x - (self.dimensions.x / 2)
		self.rightbound = self.location.x + (self.dimensions.x / 2)
		self.topbound = self.location.y + (self.dimensions.y / 2)
		self.botbound = self.location.y - (self.dimensions.y / 2)
	
	def update(self):
		self.move()

		self.leftbound = self.location.x - (self.dimensions.x / 2)
		self.rightbound = self.location.x + (self.dimensions.x / 2)
		self.topbound = self.location.y + (self.dimensions.y / 2)
		self.botbound = self.location.y - (self.dimensions.y / 2)

		for x in player_list:
			if x.state == "ground" and x.onterrain == self.number:
				x.location += self.velocity

		pygame.draw.rect(game_screen, (0,0,0), (v2_to_int_tuple(loc_to_draw_loc(self.location, self.dimensions)), v2_to_int_tuple(self.dimensions)), 0)

	def move(self):
		
		if self.velocity != Vector2(0,0):
			if (self.location.x > self.maxloc.x) or (self.location.x < self.minloc.x) or (self.location.y > self.maxloc.y) or (self.location.y < self.minloc.y):
				self.velocity = Vector2(self.velocity.x * -1, self.velocity.y * -1)
				self.location += self.velocity
				#print self.location, self.minloc, self.maxloc

		self.location += self.velocity

class Effects:
	def __init__(self):
		print("")

class Buffs:
	def __init__(self):
		print("")

#endregion

#region Game

keydic = [{"up": False, "down": False, "left": False, "right": False, "attack": False, "defend": False},{"up": False, "down": False, "left": False, "right": False, "attack": False, "defend": False}, {"enter": False, "escape": False}]

while game_state != "stop":

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			game_state = "stop"

		elif event.type == KEYDOWN:
			
			if event.key == pygame.K_w:
				keydic[0]["up"] = True
			elif event.key == pygame.K_a:
				keydic[0]["left"] = True
			elif event.key == pygame.K_s:
				keydic[0]["down"] = True
			elif event.key == pygame.K_d:
				keydic[0]["right"] = True
			elif event.key == pygame.K_e:
				keydic[0]["attack"] = True
			
			elif event.key == pygame.K_UP:
				keydic[1]["up"] = True
			elif event.key == pygame.K_LEFT:
				keydic[1]["left"] = True
			elif event.key == pygame.K_DOWN:
				keydic[1]["down"] = True
			elif event.key == pygame.K_RIGHT:
				keydic[1]["right"] = True
			elif event.key == pygame.K_SLASH:
				keydic[1]["attack"] = True

			elif event.key == pygame.K_RETURN:
				keydic[2]["enter"] = True
			elif event.key == pygame.K_ESCAPE:
				keydic[2]["escape"] = True

			elif event.key == pygame.K_1:
				mapnumber = 0
			elif event.key == pygame.K_2:
				mapnumber = 1
			elif event.key == pygame.K_3:
				mapnumber = 2
			elif event.key == pygame.K_4:
				character_choice[0] = 0
			elif event.key == pygame.K_5:
				character_choice[0] = 1
			elif event.key == pygame.K_6:
				character_choice[0] = 2
			elif event.key == pygame.K_7:
				character_choice[1] = 0
			elif event.key == pygame.K_8:
				character_choice[1] = 1
			elif event.key == pygame.K_9:
				character_choice[1] = 2
		
		elif event.type == KEYUP:

			if event.key == pygame.K_w:
				keydic[0]["up"] = False
			elif event.key == pygame.K_a:
				keydic[0]["left"] = False
			elif event.key == pygame.K_s:
				keydic[0]["down"] = False
			elif event.key == pygame.K_d:
				keydic[0]["right"] = False
			elif event.key == pygame.K_e:
				keydic[0]["attack"] = False
			
			elif event.key == pygame.K_UP:
				keydic[1]["up"] = False
			elif event.key == pygame.K_LEFT:
				keydic[1]["left"] = False
			elif event.key == pygame.K_DOWN:
				keydic[1]["down"] = False
			elif event.key == pygame.K_RIGHT:
				keydic[1]["right"] = False
			elif event.key == pygame.K_SLASH:
				keydic[1]["attack"] = False

			elif event.key == pygame.K_RETURN:
				keydic[2]["enter"] = False
			elif event.key == pygame.K_ESCAPE:
				keydic[2]["escape"] = False

	if game_state == "init":
		player_list = []
		hurtbox_list = []
		hitbox_list = []
		terrain_list = []
		game_state = "title"

	elif game_state == "title":
		game_screen.blit(image_list["game"]["title"], (0,0))
		if keydic[2]["escape"]:
			game_state = "stop"
		elif keydic[2]["enter"]:
			for a in range(2):
				player_list.append(Player(a))
				player_list[a].spawn()
				hurtbox_list.append(Hurtbox(a))
			for b in range(len(stage_data[mapnumber])):
				terrain_list.append(Terrain(mapnumber,b))
			game_state = "game"
	elif game_state == "game":

		if keydic[2]["escape"]:
			game_state = "init"

		game_screen.fill((255,255,255))

		percent = monospace.render(str(player_list[0].percent) + "%", False, (0,0,0))
		displaystate = monospace.render(player_list[1].state, False, (0,0,0))
		displaysubstate = monospace.render(player_list[1].substate, False, (0,0,0))
		displayjump = monospace.render(str(player_list[1].jump), False, (0,0,0))
		game_screen.blit(percent, (0,0))
		game_screen.blit(displaystate, (0,40))
		game_screen.blit(displaysubstate, (0,80))
		game_screen.blit(displayjump, (0,120))
		
		for x in terrain_list:
			x.update()

		for x in player_list:
			if x.lives == 0:
				game_state = "init"
			x.update()

		for x in hurtbox_list:
			x.update()

		for x in hitbox_list:
			x.update()

	pygame.display.update()		
	game_clock.tick(60)

#endregion

pygame.quit()