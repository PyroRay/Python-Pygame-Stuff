#Character Data for 3xCSL
#Python 2.7.18
#Harper Kim

from pygame import *

#Yessuo
char0_stats = {"weight": 0.5, "walkspeed": 15, "airspeed": 10, "jumpspeed": 30, "fallspeed": 5, "dimensions": Vector2(55,55)}

char0_left_attack_hitbox0 = {"lock": False, "knockback": Vector2(-30, 10), "multiplyer": 1.0, "radius": 25, "offset": Vector2(0,0), "velocity": Vector2(-50,0), "duration": 2, "damage": 10}
char0_left_attack_hitboxes = [char0_left_attack_hitbox0]
char0_left_attack = {"attackframes": 9, "hitboxes": char0_left_attack_hitboxes}

char0_right_attack_hitbox0 = {"lock": False, "knockback": Vector2(30, 10), "multiplyer": 1.0, "radius": 25, "offset": Vector2(0,0), "velocity": Vector2(50,0), "duration": 2, "damage": 10}
char0_right_attack_hitboxes = [char0_right_attack_hitbox0]
char0_right_attack = {"attackframes": 9, "hitboxes": char0_right_attack_hitboxes}

char0_up_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, 10), "multiplyer": 1.0, "radius": 25, "offset": Vector2(-25,50), "velocity": Vector2(0,0), "duration": 5, "damage": 10}
char0_up_attack_hitbox1 = {"lock": True, "knockback": Vector2(0, 10), "multiplyer": 1.0, "radius": 25, "offset": Vector2(0,50), "velocity": Vector2(0,0), "duration": 5, "damage": 10}
char0_up_attack_hitbox2 = {"lock": True, "knockback": Vector2(0, 10), "multiplyer": 1.0, "radius": 25, "offset": Vector2(25,50), "velocity": Vector2(0,0), "duration": 5, "damage": 10}
char0_up_attack_hitboxes = [char0_up_attack_hitbox0, char0_up_attack_hitbox1, char0_up_attack_hitbox2]
char0_up_attack = {"attackframes": 9, "hitboxes": char0_up_attack_hitboxes}

char0_down_attack_hitbox0 = {"lock": True, "knockback": Vector2(0, -30), "multiplyer": 1.0, "radius": 25, "offset": Vector2(0,-50), "velocity": Vector2(0,0), "duration": 5, "damage": 10}
char0_down_attack_hitboxes = [char0_down_attack_hitbox0]
char0_down_attack = {"attackframes": 12, "hitboxes": char0_down_attack_hitboxes}

char0_attacks = {"left": char0_left_attack, "right": char0_right_attack, "up": char0_up_attack, "down":char0_down_attack}

char0 = {"stats": char0_stats, "attacks": char0_attacks}

#Zeo
char1_stats = {"weight": 1, "walkspeed": 10, "airspeed": 5, "jumpspeed": 25, "fallspeed": 3, "dimensions": Vector2(65,65)}





char1 = {"stats": char1_stats}

#Morede
char2_stats = {"weight": 1.5, "walkspeed": 7, "airspeed": 3, "jumpspeed": 17, "fallspeed": 1.5, "attacklength": 30, "dimensions": Vector2(75,75)}
char2 = {"stats": char2_stats}

character_data = [char0, char1, char2]