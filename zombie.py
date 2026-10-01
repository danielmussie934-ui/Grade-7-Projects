import pygame
import numpy as np
import typing
from random import randint, choice

pygame.init()

screen  = pygame.display.set_mode((800, 600))
running: bool = True
clock: object = pygame.time.Clock()
class Zombie:
    def __init__(self):
        self.zombies_pos_x = []
        self.zombies_pos_y = []
        self.current_x = 0
        self.current_y = 0
    def spawn(self): 
        while len(self.zombies_pos_x) <= 100:
            current_x = randint(-50, 850)
            if current_x < -15 or current_x > 815:
               self.zombies_pos_x.append(current_x)
        while len(self.zombies_pos_y) <= 100:
            current_y = randint(-50, 650)
            if current_y < -15 or current_y > 615:
                self.zombies_pos_y.append(current_y)
    def draw(self):
        for x in self.zombies_pos_x:
            self.current_x = x
            self.zombies_pos_x.remove(x)
            break
        for y in self.zombies_pos_y:
            self.current_y = y 
            self.zombies_pos_y.remove(y)
            break
        pygame.draw.rect(screen, (0, 255, 0), (self.current_x, self.current_y, 25, 10  ), border_radius = 3) #type: ignore
    def calculate(self, player_x: int, player_y: int):
        if player_x > self.current_x:
            self.current_x += 5
        if player_x < self.current_x:
            self.current_x -= 5
        if player_y < self.current_y:
            self.current_y -= 5
        if player_y > self.current_y:
            self.current_y += 5

        
class Player: 
    def __init__(self, x: int , y: int):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 10)
        
    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 5
        if self.rect.left < 0:
            self.rect.left = 0  
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:   
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0),  self.rect, border_radius = 2)

player = Player(350, 360)
zombies = Zombie()
while running:
    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))
    player.update(keys)
    zombies.spawn()
    zombies.calculate(player.rect.x, player.rect.y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    zombies.draw()
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

