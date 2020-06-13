#Character Data for 3xCSL
#Python 2.7.18
#Harper Kim

from pygame import *




#Yessuo
char0_stats = {"weight": 0.5, "walkspeed": 15, "airspeed": 10, "jumpspeed": 29, "fallspeed": 5, "dimensions": Vector2(55,55), "spawnhitbox": False}


char0_left_attack_hitbox0 = {"lock": False, "knockback": Vector2(-15, 8), "multiplyer": 2.0, "radius": 40, "offset": Vector2(0,0), "velocity": Vector2(-30,0), "duration": 4, "damage": 10}
char0_left_attack_hitboxes = [char0_left_attack_hitbox0]

char0_left_attack_visual0 = {"lock": False, "sync": False, "dimensions": Vector2(80,80), "offset": Vector2(0,0), "velocity": Vector2(-30,0), "duration": 4}
char0_left_attack_visuals = [char0_left_attack_visual0]

char0_left_attack = {"attackframes": 4, "hitboxes": char0_left_attack_hitboxes, "visual": char0_left_attack_visuals}


char0_right_attack_hitbox0 = {"lock": False, "knockback": Vector2(15, 8), "multiplyer": 2.0, "radius": 40, "offset": Vector2(0,0), "velocity": Vector2(30,0), "duration": 4, "damage": 10}
char0_right_attack_hitboxes = [char0_right_attack_hitbox0]

char0_right_attack_visual0 = {"lock": False, "sync": False, "dimensions": Vector2(80,80), "offset": Vector2(0,0), "velocity": Vector2(30,0), "duration": 4}
char0_right_attack_visuals = [char0_right_attack_visual0]

char0_right_attack = {"attackframes": 4, "hitboxes": char0_right_attack_hitboxes, "visual": char0_right_attack_visuals}


char0_up_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, 15), "multiplyer": 1.0, "radius": 25, "offset": Vector2(-25,50), "velocity": Vector2(0,0), "duration": 5, "damage": 15}
char0_up_attack_hitbox1 = {"lock": True, "knockback": Vector2(0, 15), "multiplyer": 1.0, "radius": 25, "offset": Vector2(0,50), "velocity": Vector2(0,0), "duration": 5, "damage": 15}
char0_up_attack_hitbox2 = {"lock": True, "knockback": Vector2(0, 15), "multiplyer": 1.0, "radius": 25, "offset": Vector2(25,50), "velocity": Vector2(0,0), "duration": 5, "damage": 15}
char0_up_attack_hitboxes = [char0_up_attack_hitbox0, char0_up_attack_hitbox1, char0_up_attack_hitbox2]

char0_up_attack_visual0 = {"lock": True, "sync": False, "dimensions": Vector2(100,50), "offset": Vector2(0,50), "velocity": Vector2(0,0), "duration": 5}
char0_up_attack_visuals = [char0_up_attack_visual0]

char0_up_attack = {"attackframes": 6, "hitboxes": char0_up_attack_hitboxes, "visual": char0_up_attack_visuals}


char0_down_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, -40), "multiplyer": 0, "radius": 25, "offset": Vector2(-10,-50), "velocity": Vector2(0,0), "duration": 5, "damage": 15}
char0_down_attack_hitbox1 = {"lock": True, "knockback": Vector2(0, -40), "multiplyer": 0, "radius": 25, "offset": Vector2(10,-50), "velocity": Vector2(0,0), "duration": 5, "damage": 15}
char0_down_attack_hitboxes = [char0_down_attack_hitbox0, char0_down_attack_hitbox1]

char0_down_attack_visual0 = {"lock": True, "sync": False, "dimensions": Vector2(75,50), "offset": Vector2(0,-50), "velocity": Vector2(0,0), "duration": 5}
char0_down_attack_visuals = [char0_down_attack_visual0]

char0_down_attack = {"attackframes": 5, "hitboxes": char0_down_attack_hitboxes, "visual": char0_down_attack_visuals}


char0_attacks = {"left": char0_left_attack, "right": char0_right_attack, "up": char0_up_attack, "down":char0_down_attack}

char0 = {"stats": char0_stats, "attacks": char0_attacks}




#Zeo
char1_stats = {"weight": 1.0, "walkspeed": 10, "airspeed": 5, "jumpspeed": 25, "fallspeed": 3, "dimensions": Vector2(65,65), "spawnhitbox": True}


char1_left_attack_hitbox0 = {"lock": False, "knockback": Vector2(-18, 6), "multiplyer": 4.0, "radius": 10, "offset": Vector2(0,0), "velocity": Vector2(-30,0), "duration": 10, "damage": 5}
char1_left_attack_hitboxes = [char1_left_attack_hitbox0]

char1_left_attack_visual0 = {"lock": False, "sync": True, "dimensions": Vector2(20,20), "offset": Vector2(0,0), "velocity": Vector2(-30,0), "duration": 10}
char1_left_attack_visuals = [char1_left_attack_visual0]

char1_left_attack = {"attackframes": 11, "hitboxes": char1_left_attack_hitboxes, "visual": char1_left_attack_visuals}


char1_right_attack_hitbox0 = {"lock": False, "knockback": Vector2(18, 6), "multiplyer": 4.0, "radius": 10, "offset": Vector2(0,0), "velocity": Vector2(30,0), "duration": 10, "damage": 5}
char1_right_attack_hitboxes = [char1_right_attack_hitbox0]

char1_right_attack_visual0 = {"lock": False, "sync": True, "dimensions": Vector2(20,20), "offset": Vector2(0,0), "velocity": Vector2(30,0), "duration": 10}
char1_right_attack_visuals = [char1_right_attack_visual0]

char1_right_attack = {"attackframes": 11, "hitboxes": char1_right_attack_hitboxes, "visual": char1_right_attack_visuals}


char1_up_attack_hitbox0 = {"lock": False, "knockback": Vector2(0, 0), "multiplyer": 1.0, "radius": 10, "offset": Vector2(0,0), "velocity": Vector2(0,15), "duration": 10, "damage": 5}
char1_up_attack_hitboxes = [char1_up_attack_hitbox0]

char1_up_attack_visual0 = {"lock": False, "sync": True, "dimensions": Vector2(20,20), "offset": Vector2(0,0), "velocity": Vector2(0,15), "duration": 10}
char1_up_attack_visuals = [char1_up_attack_visual0]

char1_up_attack = {"attackframes": 13, "hitboxes": char1_up_attack_hitboxes, "visual": char1_up_attack_visuals}


char1_down_attack_hitbox0 = {"lock": False, "knockback": Vector2(0,0), "multiplyer": 1.0, "radius": 10, "offset": Vector2(0,0), "velocity": Vector2(0,-15), "duration": 10, "damage": 5}
char1_down_attack_hitboxes = [char1_down_attack_hitbox0]

char1_down_attack_visual0 = {"lock": False, "sync": True, "dimensions": Vector2(20,20), "offset": Vector2(0,0), "velocity": Vector2(0,-15), "duration": 10}
char1_down_attack_visuals = [char1_down_attack_visual0]

char1_down_attack = {"attackframes": 13, "hitboxes": char1_down_attack_hitboxes, "visual": char1_down_attack_visuals}


char1_bubble_hitbox0 = {"lock": False, "knockback": Vector2(0,0), "multiplyer": 1.0, "radius": 40, "offset": Vector2(0,0), "velocity": Vector2(0,0), "duration": 90, "damage": 30}
char1_bubble_hitboxes = [char1_bubble_hitbox0]

char1_bubble_visual0 = {"lock": False, "sync": True, "dimensions": Vector2(80,80), "offset": Vector2(0,0), "velocity": Vector2(0,0), "duration": 90}
char1_bubble_visual = [char1_bubble_visual0]

char1_bubble = {"hitboxes": char1_bubble_hitboxes, "visual": char1_bubble_visual}

char1_attacks = {"left": char1_left_attack, "right": char1_right_attack, "up": char1_up_attack, "down":char1_down_attack, "misc": char1_bubble}

char1 = {"stats": char1_stats, "attacks": char1_attacks}




#Morede
char2_stats = {"weight": 1.8, "walkspeed": 7, "airspeed": 3, "jumpspeed": 16, "fallspeed": 1.5, "attacklength": 30, "dimensions": Vector2(75,75), "spawnhitbox": False}


char2_left_attack_hitbox0 = {"lock": True, "knockback": Vector2(-35, 20), "multiplyer": 2.0, "radius": 30, "offset": Vector2(-70,10), "velocity": Vector2(0,0), "duration": 14, "damage": 30}
char2_left_attack_hitboxes = [char2_left_attack_hitbox0]

char2_left_attack_visuals = []

char2_left_attack = {"attackframes": 45, "hitboxes": char2_left_attack_hitboxes, "visual": char2_left_attack_visuals}


char2_right_attack_hitbox0 = {"lock": True, "knockback": Vector2(35, 20), "multiplyer": 2.0, "radius": 30, "offset": Vector2(70,10), "velocity": Vector2(0,0), "duration": 14, "damage": 30}
char2_right_attack_hitboxes = [char2_right_attack_hitbox0]

char2_right_attack_visuals = []

char2_right_attack = {"attackframes": 45, "hitboxes": char2_right_attack_hitboxes, "visual": char2_right_attack_visuals}


char2_up_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, 40), "multiplyer": 1.0, "radius": 30, "offset": Vector2(0,50), "velocity": Vector2(0,0), "duration": 14, "damage": 20}
char2_up_attack_hitboxes = [char2_up_attack_hitbox0]

char2_up_attack_visuals = []

char2_up_attack = {"attackframes": 30, "hitboxes": char2_up_attack_hitboxes, "visual": char2_up_attack_visuals}


char2_down_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, -40), "multiplyer": 0, "radius": 30, "offset": Vector2(0,-50), "velocity": Vector2(0,0), "duration": 7, "damage": 20}
char2_down_attack_hitboxes = [char2_down_attack_hitbox0]

char2_down_attack_visuals = []

char2_down_attack = {"attackframes": 30, "hitboxes": char2_down_attack_hitboxes, "visual": char2_down_attack_visuals}


char2_attacks = {"left": char2_left_attack, "right": char2_right_attack, "up": char2_up_attack, "down": char2_down_attack}

char2 = {"stats": char2_stats, "attacks": char2_attacks}




character_data = [char0, char1, char2]