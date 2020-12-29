import pygame, random
from config import *

class Food(pygame.sprite.Sprite):
    def __init__(self, screen, snake, x=None, y=None):
        super(Food, self).__init__()
        self.screen = screen
        self.surf = pygame.Surface(FOOD_SIZE)
        self.img = pygame.image.load("images/apple.jpg")
        self.img = pygame.transform.scale(self.img, FOOD_SIZE)
        self.surf.fill(FOOD_COLOR)
        self.width, self.height = SNAKE_SIZE
        self.snake = snake
        self.x = x
        self.y = y
        if not x or not y:
            self.newPos()

    def newPos(self):
        while True:
            collided = False
            self.x = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_SIZE[0])
            self.y = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_SIZE[1])
            # While generating new position, make sure it does not spawn in the snake's body
            for x, y in self.snake.body:
                if self.x == x and self.y == y:
                    collided = True
            if not collided: break

    def draw(self):
        #self.screen.blit(self.surf, (self.x, self.y))
        self.screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(self.screen, FOOD_COLOR, (self.x, self.y, *FOOD_SIZE))
