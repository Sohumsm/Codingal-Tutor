import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

backround = pygame.image.load("")

background = pygame.image.load("")
background = pygame.transform.scale(background, (800, 500))

pygame.display.set_caption("Space Invader")

icon = pygame.image.load("")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

playerImg = pygame.image.load("")
playerImg = pygame.transform.scale(playerImg, (64, 64))
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(
        pygame.image.load("")
    )
    bulletImg = pygame.image.load("")
bulletImg = pygame.transform.scale(bulletImg, (16, 24))

bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x, y):
    score = font.render("Score : " + str(store_value),True,(255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.reader("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (200,250))




