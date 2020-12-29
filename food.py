import pygame, random
from config import *


class Food(pygame.sprite.Sprite):
    def __init__(self, screen, x=None, y=None):
        super(Food, self).__init__()
        self.screen = screen
        self.surf = pygame.Surface(FOOD_SIZE)
        self.surf.fill(FOOD_COLOR)
        self.width, self.height = SNAKE_SIZE
        self.x = x
        self.y = y
        if not x or not y:
            self.newPos()

    def newPos(self):
        self.x = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_SIZE[0])
        self.y = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_SIZE[1])

    def draw(self):
        #self.screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(self.screen, FOOD_COLOR, (self.x, self.y, *FOOD_SIZE))
