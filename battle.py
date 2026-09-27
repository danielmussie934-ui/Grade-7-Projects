import pygame
import numpy as np
import typing
from random import randint, choice

pygame.init()

player1 = pygame.Rect((200, 275), (50, 30))
player2 = pygame.Rect((600, 275), (50, 30))

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x: int, y: int):
        self.bullets: list = []
        self.x = x
        self.y = y
    def get_rect(self):
            return pygame.Rect(self.x, self.y, 15, 10)

    def update(self, rect):
        rect.x += 5

player1_bullets = Bullet(player1.x, player1.y)
player2_bullets = Bullet(player2.x, player2.y)


def movement(keys) -> None:
    # player 1 movement logic
    if keys[pygame.K_w]:
        player1.top -= 5
    if keys[pygame.K_s]:
        player1.top += 5
    if keys[pygame.K_a]:
        player1.left -= 5
    if keys[pygame.K_d]:
        player1.left += 5
    # player 2 movement logic
    if keys[pygame.K_UP]:
        player2.top -= 5
    if keys[pygame.K_DOWN]:
        player2.top += 5
    if keys[pygame.K_LEFT]:
        player2.left -= 5
    if keys[pygame.K_RIGHT]:
        player2.left += 5
    # Bullet logic
    if keys[pygame.K_LSHIFT]:
        player1_bullets.bullets.append("Bullet")
    if keys[pygame.K_SPACE]:
        player2_bullets.bullets.append("Bullet")


def collison() -> None:
    # Checking if either crossed the line
    if player1.x >= 350:
        player1.x = 350
    if player2.x <= 400:
        player2.x = 400
    # Checking if they went behind them 
    if player1.x <= 0:
        player1.x = 0
    if player2.x >= 750:
        player2.x = 750
    # Checking if they went past the floor 
    if player1.y >= 550  :
        player1.y = 550
    if player2.y >= 550:
       player2.y = 550
    # Checking if they went over the top
    if player1.y <= 0:
        player1.y = 0
    if player2.y <= 0:
        player2.y = 0
    


while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    movement(keys)
    collison() 
    player1_bullets.update(player1_bullets.get_rect())
    print(player1_bullets.bullets)
    # Drawing / Rendering
    pygame.draw.rect(screen, (255, 0, 0), player1) # Drawing player 1
    pygame.draw.rect(screen, (0, 255, 0), player2) # Drawing player 2
    pygame.draw.line(screen, (255, 255, 255), (400, 600), (400, 0), width=3)
    if not len(player1_bullets.bullets) > 10:
     for item in range(len(player1_bullets.bullets)):
         pygame.draw.rect(screen, (255, 255, 0), player1_bullets.get_rect())

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
