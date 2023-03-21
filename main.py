import pygame
from pygame.gfxdraw import pixel
import math
pygame.init()

surf = pygame.display.set_mode((800, 800))
fov = math.pi / 4
player = [5, 5]
angle = 0
keycode = pygame.key.key_code
clock = pygame.time.Clock()

map = [
    "####################",
    "#                  #",
    "#                  #",
    "#        #         #",
    "#                  #",
    "#                  #",
    "#                  #",
    "#                  #",
    "#                  #",
    "####################"
]

#def pixel(surf, x, y, color):
#    pygame.draw.rect(surf, color, (x, y, scale, scale))

i = 0
speed = .1

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    surf.fill(0)
    keys = pygame.key.get_pressed()
    if keys[keycode('w')]:
        player = [math.sin(angle) * speed + player[0], math.cos(angle) + player[1]]
    if keys[keycode('s')]:
        player = [-math.sin(angle) * speed + player[0], -math.cos(angle) + player[1]]
    if keys[keycode('a')]:
        angle -= .1
    if keys[keycode('d')]:
        angle += .1
    for x in range(800):
        angling = (angle - fov/2) + (x/800) * fov
        step_size = .01
        distance = 0
        hit_wall = False
        eye = [math.sin(angling), math.cos(angling)]
        while not hit_wall and distance < 5:
            distance += step_size
            test = [
                player[0] + eye[0] * distance,
                player[1] + eye[1] * distance
            ]
            try:
                if map[round(test[1])][round(test[0])] == '#':
                    hit_wall = True
            except:
                pass
        ceiling = round(800/2 - 800 / distance)
        floor = round(600 - ceiling)
        for y in range(ceiling, floor):
            pixel(surf, x, y, [(255 / 7) * distance for i in range(3)])
    pygame.display.flip()
