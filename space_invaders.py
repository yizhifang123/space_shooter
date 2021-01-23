import random
import math
import time

import pygame
from threading import Thread
import threading
from pygame import mixer

pygame.init()

display_width = 700
display_height = 800
destroyed = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Shooter')

mixer.music.load('background.wav')
mixer.music.play(-1)

black = (0, 0, 0)
white = (255, 255, 255)
LIGHTRED = (255, 100, 100)
ship_width = 73
x = (display_width * 0.45)
y = (display_height * 0.8)
event = threading.Event
player_vel = 5
vel = 10
score_value = 0
font = pygame.font.Font('Minecraft.ttf', 32)
textX = 10
textY = 10

clock = pygame.time.Clock()
crashed = False
ship_Img = pygame.image.load('001-space-invaders.png')
background = pygame.image.load('hie.png')


def ship(x, y):
    gameDisplay.blit(ship_Img, (x, y))


bulletImg = pygame.image.load('bulet.png')
bulletY = 620
bulletX = 0
bulletY_change = 10
bullet_state = "ready"

thing_startx = random.randrange(0, display_width)
thing_starty = -600
thing_speed = 12

thing_width = 100
thing_height = 100
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
ship_speed = 0


def things(thingx, thingy, thingw, thingh, color):
    rock = pygame.image.load('rock.png')
    gameDisplay.blit(rock, (thingx, thingy))



def power_ups():
        speed = pygame.image.load('001-idea.png')
        for i in range(100):
            gameDisplay.blit(speed, (random.randint(50, 600), random.randint(50, 700)))
            time.sleep(3)

def score(score_value):
    text = font.render("Score: " + str(score_value), True, LIGHTRED)
    gameDisplay.blit(text, [10, 10])


def shoot_projectiles(x, y):
    global bullet_state
    bullet_state = "fire"
    gameDisplay.blit(bulletImg, (x + 16, y + 10))


def my_collision(thing_startx, thing_starty, bulletX, bulletY):
    distance = math.sqrt((math.pow(thing_startx - bulletX, 2)) + (math.pow(thing_starty - bulletY, 2)))
    if distance < 90:
        return True
    else:
        return False


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if x <= 0:
        x = 0

    if x >= 630:
        x = 630

    if y <= 0:
        y = 0

    if y >= 730:
        y = 730

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_SPACE]:
        if bullet_state is "ready":
            bullet_SOund = mixer.Sound('laser.wav')
            bullet_SOund.play()
            bulletX = x
            shoot_projectiles(x, y)

    x += x_change
    y += y_change

    gameDisplay.fill(black)
    gameDisplay.blit(background, (0, 0))
    things(thing_startx, thing_starty, thing_width, thing_height, LIGHTRED)
    things(thing_startx, thing_starty, thing_width, thing_height, LIGHTRED)
    thing_starty += thing_speed
    score(score_value)
    power_ups()
    ship(x, y)


    if bulletY <= 0:
        bulletY = y
        bullet_state = "ready"

    if bullet_state is "fire":
        shoot_projectiles(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = my_collision(thing_startx, thing_starty, bulletX, bulletY)
    if collision:
        ex_SOund = mixer.Sound('explosion.wav')
        ex_SOund.play()
        bulletY = y
        bullet_state = "ready"
        score_value += 1
        thing_startx = random.randrange(0, display_width)
        thing_starty = -600

    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0, display_width)

    if y < thing_starty + thing_height:
        crashed = False

        if thing_startx < x < thing_startx + thing_width or thing_startx < x + 73 < thing_startx + thing_width:
            crashed = True
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
