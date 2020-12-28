import pygame, random
from config import *


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface(SNAKE_SIZE)
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect()
        self.foodx = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_SIZE[0])
        self.foody = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_SIZE[1])
