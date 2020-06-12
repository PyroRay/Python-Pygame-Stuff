#Stage Data for 3xCSL
#Python 2.7.18
#Harper Kim

from pygame import *

screen_dimensions = Vector2(1280, 720)

#Battlezone
stage0_platform0 = {"platform": False, "dimensions": Vector2(800, 50), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2 - 200), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage0_platform1 = {"platform": True, "dimensions": Vector2(250, 20), "location": Vector2(screen_dimensions.x * 1 / 4 + 10, screen_dimensions.y / 2 - 10), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage0_platform2 = {"platform": True, "dimensions": Vector2(250, 20), "location": Vector2(screen_dimensions.x * 3 / 4 - 10, screen_dimensions.y / 2 - 10), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage0_platform3 = {"platform": True, "dimensions": Vector2(250, 20), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2 + 145), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage0 = [stage0_platform0, stage0_platform1, stage0_platform2, stage0_platform3]

#Capture
stage1_platform0 = {"platform": False, "dimensions": Vector2(600, 60), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2 - 100), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage1 = [stage1_platform0]

#Fader
stage1_platform0 = {"platform": False, "dimensions": Vector2(200, 30), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 5), \
    "velocity": Vector2(6,0), "minimum": Vector2(screen_dimensions.x * 1 / 4, screen_dimensions.y / 5), \
    "maximum": Vector2(screen_dimensions.x * 3 / 4, screen_dimensions.y / 5)}
stage1_platform1 = {"platform": True, "dimensions": Vector2(200, 30), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y * 4 / 5), \
    "velocity": Vector2(-6,0), "minimum": Vector2(screen_dimensions.x * 1 / 4, screen_dimensions.y * 4 / 5), \
    "maximum": Vector2(screen_dimensions.x * 3 / 4, screen_dimensions.y * 4/ 5)}
stage1_platform2 = {"platform": True, "dimensions": Vector2(200, 30), "location": Vector2(screen_dimensions.x / 5, screen_dimensions.y / 2), \
    "velocity": Vector2(0,5), "minimum": Vector2(screen_dimensions.x / 5, screen_dimensions.y / 4), \
    "maximum": Vector2(screen_dimensions.x / 5, screen_dimensions.y * 3 / 4)}
stage1_platform3 = {"platform": True, "dimensions": Vector2(200, 30), "location": Vector2(screen_dimensions.x * 4 / 5, screen_dimensions.y / 2), \
    "velocity": Vector2(0,-5), "minimum": Vector2(screen_dimensions.x * 4/ 5, screen_dimensions.y / 4), \
    "maximum": Vector2(screen_dimensions.x * 4 / 5, screen_dimensions.y * 3 / 4)}
stage2 = [stage1_platform0, stage1_platform1, stage1_platform2, stage1_platform3]

stage_data = [stage0, stage1, stage2]