# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.surf = pygame.Surface(SNAKE_SIZE)
        self.surf.fill(SNAKE_COLOR)
        self.screen = screen
        #self.rect = self.surf.get_rect()
        self.body = [SNAKE_ORIGIN]
        self.width, self.height = SNAKE_SIZE
        self.direction = RIGHT

    def update(self, keys):
        self.keys = keys
        # since key-presses are always 1 or 0, we can multiply each key with their respective value from the
        # static map above, LEFT = 4 in binary, so if we multiply 4*1|0 we'll get binary 0100 if it's pressed.
        # We can always safely combine 1, 2, 4 and 8 as they will never collide and thus always create a truth map of
        # which direction in bitwise friendly representation.
        if any((self.keys[K_UP], self.keys[K_DOWN], self.keys[K_LEFT], self.keys[K_RIGHT])):
            self.direction = self.keys[K_UP]*1 + self.keys[K_DOWN]*2 + self.keys[K_LEFT]*4 + self.keys[K_RIGHT]*8

        print(self.body)
        x, y = self.body[0] #get snake head
        self.body.pop() #remove last body
        if self.direction & UP:
            y = y + SNAKE_BLOCK
        elif self.direction & DOWN:
            y = y - SNAKE_BLOCK
        elif self.direction & LEFT:
            x = x - SNAKE_BLOCK
        elif self.direction & RIGHT:
            x = x + SNAKE_BLOCK
        self.body.insert(0, (x, y))

    def eat(self, food):
        x, y = self.body[0] #get the head of the snake
        if x >= food.x and x + self.width <= food.x + food.width:
            if y >= food.y and y + self.height <= food.y + food.height:
                self.body.append(self.body[-1])
                return True
        return False

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (x, y, *SNAKE_SIZE))
            print(x, y)
