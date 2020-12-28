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
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface(SNAKE_SIZE)
        self.surf.fill(SNAKE_COLOR)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        #move sprite based on key pressed
        if (pressed_keys[K_UP]):
            self.rect.move_ip(0, -SNAKE_BLOCK)
        if (pressed_keys[K_DOWN]):
            self.rect.move_ip(0, SNAKE_BLOCK)
        if (pressed_keys[K_LEFT]):
            self.rect.move_ip(-SNAKE_BLOCK, 0)
        if (pressed_keys[K_RIGHT]):
            self.rect.move_ip(SNAKE_BLOCK, 0)

        #prevent sprite going off screen
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            return True
        return False
