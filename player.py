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
        self.screen = screen
        self.surf = pygame.Surface(SNAKE_SIZE)
        self.surf.fill(SNAKE_COLOR)
        #self.rect = self.surf.get_rect()
        self.body = [SNAKE_ORIGIN]
        self.width, self.height = SNAKE_SIZE
        self.direction = RIGHT
        self.prevDirection = self.direction

    def update(self):
        self.keys = pygame.key.get_pressed()
        # since key-presses are always 1 or 0, we can multiply each key with their respective value from the
        # static map above, LEFT = 4 in binary, so if we multiply 4*1|0 we'll get binary 0100 if it's pressed.
        # We can always safely combine 1, 2, 4 and 8 as they will never collide and thus always create a truth map of
        # which direction in bitwise friendly representation.
        if any((self.keys[K_UP], self.keys[K_DOWN], self.keys[K_LEFT], self.keys[K_RIGHT])):
            self.direction = self.keys[K_UP]*1 + self.keys[K_DOWN]*2 + self.keys[K_LEFT]*4 + self.keys[K_RIGHT]*8

        #make sure player cannot go reverse direction
        if self.direction & UP and self.prevDirection == 2:
            self.direction = 2
        elif self.direction & DOWN and self.prevDirection == 1:
            self.direction = 1
        elif self.direction & LEFT and self.prevDirection == 8:
            self.direction = 8
        elif self.direction & RIGHT and self.prevDirection == 4:
            self.direction = 4
        self.prevDirection = self.direction

        x, y = self.body[0] #get snake head
        self.body.pop() #remove last body
        if self.direction & UP:
            y = (y - SNAKE_BLOCK) % SCREEN_HEIGHT
        elif self.direction & DOWN:
            y = (y + SNAKE_BLOCK) % SCREEN_HEIGHT
        elif self.direction & LEFT:
            x = (x - SNAKE_BLOCK) % SCREEN_WIDTH
        elif self.direction & RIGHT:
            x = (x + SNAKE_BLOCK) % SCREEN_WIDTH
        self.body.insert(0, (x, y))

    def collided(self):
        x, y = self.body[0] #get snake head
        if (len(self.body) > 2):
            for bodyx, bodyy in self.body[1:]:
                #print(f"x :{x} y :{y}  bodyx :{bodyx} bodyy :{bodyy}")
                if x >= bodyx and x + self.width <= bodyx + self.width:
                    if y >= bodyy and y + self.height <= bodyy + self.height:
                        return True
        return False

    def eat(self, food):
        x, y = self.body[0] #get the head of the snake
        if x >= food.x and x + self.width <= food.x + food.width:
            if y >= food.y and y + self.height <= food.y + food.height:
                self.body.append(self.body[-1])
                return True
        return False

    def draw(self):
        #print(self.body)
        for x, y in self.body:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (x, y, *SNAKE_SIZE))
