import pygame, random
from config import *


class Food(pygame.sprite.Sprite):
    def __init__(self, snake_rect):
        super(Food, self).__init__()
        self.surf = pygame.Surface(FOOD_SIZE)
        self.surf.fill(FOOD_COLOR)
        self.x = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_SIZE[0])
        self.y = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_SIZE[1])
        self.rect = pygame.Rect(self.x, self.y, *FOOD_SIZE)
        while pygame.sprite.collide_rect(self, snake_rect):
            self.x = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_SIZE[0])
            self.y = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_SIZE[1])
            self.rect = pygame.Rect(self.x, self.y, *FOOD_SIZE)
        print(self.rect)
