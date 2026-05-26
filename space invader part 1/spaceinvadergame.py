import math 
import random
import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEM_START_Y_MAX = 150
ENEMY_SPEED_X  = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE =  27

pygame.init()

screen = pygame.displat.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

backround = pygame.image.load
(r"")
backround = pygame.transform.scale(backround,(SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption("Space Incader")
icon = pygame.image.load
(r"")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)


playerImg = pygame.image.load
(r"")
playerImg = pygame.transform.scale(playerImg, (64, 64))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_image = pygame.image.load
    (r"")
    
