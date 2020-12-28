# simple snakes game with pygame

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

#import and initiate pygame
from player import Player
import pygame
import time
pygame.init()

from config import *
#Set up drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake game by Ben')

font_style = pygame.font.SysFont(None, 20)

def message(msg, color, coord):
    msg_surf = font_style.render(msg, True, color)
    screen.blit(msg_surf, coord)

#Initiate a player object, in this case a snake
snake = Player()

#Run game until user ask to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        # did the user hit a KEY
        if event.type == KEYDOWN:
            # if ESCAPE key is pressed
            if event.key == K_ESCAPE:
                running = False
        # if user clicked close button
        if event.type == QUIT:
            running = False

    #Variables
    snake_speed = 30
    clock = pygame.time.Clock()

    #Get all the keys pressed
    pressed_keys = pygame.key.get_pressed()

    #update snake every frame
    collided = snake.update(pressed_keys)
    #if snake collided
    if (collided):
        running = False
    # Fill the background with white
    screen.fill((238, 238, 238))

    # draw snake onto screen
    screen.blit(snake.surf, snake.rect)

    #flip the display screen (use this to update the content)
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(snake_speed)

# Quit game here
pygame.quit()
