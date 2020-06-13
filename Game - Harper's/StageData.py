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

stage0_platforms = [stage0_platform0, stage0_platform1, stage0_platform2, stage0_platform3]
stage0_buffs = []
stage0 = {"platforms": stage0_platforms, "buffs": stage0_buffs}

#Capture
stage1_platform0 = {"platform": False, "dimensions": Vector2(500, 60), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2 - 100), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage1_platform1 = {"platform": True, "dimensions": Vector2(125, 20), "location": Vector2(screen_dimensions.x * 1 / 4 - 50, screen_dimensions.y / 2 + 50), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}
stage1_platform2 = {"platform": True, "dimensions": Vector2(125, 20), "location": Vector2(screen_dimensions.x * 3 / 4 + 50, screen_dimensions.y / 2 + 50), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}

stage1_buff0 = {"radius": 90, "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2 - 30), "damageboost": 1.5}

stage1_platforms = [stage1_platform0, stage1_platform1, stage1_platform2]
stage1_buffs = [stage1_buff0]
stage1 = {"platforms": stage1_platforms, "buffs": stage1_buffs}

#Fader
stage2_platform0 = {"platform": True, "dimensions": Vector2(200, 20), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 5), \
    "velocity": Vector2(6,0), "minimum": Vector2(screen_dimensions.x * 1 / 4, screen_dimensions.y / 5), \
    "maximum": Vector2(screen_dimensions.x * 3 / 4, screen_dimensions.y / 5)}
stage2_platform1 = {"platform": True, "dimensions": Vector2(200, 20), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y * 4 / 5), \
    "velocity": Vector2(-6,0), "minimum": Vector2(screen_dimensions.x * 1 / 4, screen_dimensions.y * 4 / 5), \
    "maximum": Vector2(screen_dimensions.x * 3 / 4, screen_dimensions.y * 4/ 5)}
stage2_platform2 = {"platform": True, "dimensions": Vector2(200, 20), "location": Vector2(screen_dimensions.x / 5, screen_dimensions.y / 2), \
    "velocity": Vector2(0,5), "minimum": Vector2(screen_dimensions.x / 5, screen_dimensions.y / 4), \
    "maximum": Vector2(screen_dimensions.x / 5, screen_dimensions.y * 3 / 4)}
stage2_platform3 = {"platform": True, "dimensions": Vector2(200, 20), "location": Vector2(screen_dimensions.x * 4 / 5, screen_dimensions.y / 2), \
    "velocity": Vector2(0,-5), "minimum": Vector2(screen_dimensions.x * 4/ 5, screen_dimensions.y / 4), \
    "maximum": Vector2(screen_dimensions.x * 4 / 5, screen_dimensions.y * 3 / 4)}
stage2_platform4 = {"platform": True, "dimensions": Vector2(150, 20), "location": Vector2(screen_dimensions.x / 2, screen_dimensions.y / 2), \
    "velocity": Vector2(0,0), "minimum": None, "maximum": None}

stage2_platforms = [stage2_platform0, stage2_platform1, stage2_platform2, stage2_platform3, stage2_platform4]
stage2_buffs = []
stage2 = {"platforms": stage2_platforms, "buffs": stage2_buffs}

stage_data = [stage0, stage1, stage2]