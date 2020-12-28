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
    def __init__(self, head=False, changes=0):
        super(Player, self).__init__()
        self.surf = pygame.Surface(SNAKE_SIZE)
        self.surf.fill(SNAKE_COLOR)
        #self.rect = self.surf.get_rect()
        if head:
            self.rect = pygame.Rect(SNAKE_ORIGIN, SNAKE_SIZE)
        else:
            self.rect = pygame.Rect(changes, SNAKE_SIZE)
        self.changesx = 0
        self.changesy = 0

    def update(self, pressed_keys):
        #move sprite based on key pressed
        if (pressed_keys[K_UP]):
            self.changesx = 0
            self.changesy = -SNAKE_BLOCK
        elif (pressed_keys[K_DOWN]):
            self.changesx = 0
            self.changesy = SNAKE_BLOCK
        elif (pressed_keys[K_LEFT]):
            self.changesx = -SNAKE_BLOCK
            self.changesy = 0
        elif (pressed_keys[K_RIGHT]):
            self.changesx = SNAKE_BLOCK
            self.changesy = 0
        self.rect.move_ip(self.changesx, self.changesy)
        #return True if snake went off screen
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            return True
        return False
