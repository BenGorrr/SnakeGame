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
from food import Food
import pygame
import time, random
pygame.init()
#import constants from config
from config import *


#Set up drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake game by Ben')

font_style = pygame.font.SysFont(None, FONT_SIZE)

def message(msg, color, coord):
    msg_surf = font_style.render(msg, True, color)
    if coord == "center":
        screen.blit(msg_surf, (SCREEN_WIDTH/2 - msg_surf.get_width()/2, SCREEN_HEIGHT/2 - msg_surf.get_height()/2))
    else:
        screen.blit(msg_surf, coord)

#Initiate a player object, in this case a snake
snake = Player(screen)
food = Food(screen)
score = 0
clock = pygame.time.Clock()

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
    snake_speed = 10

    # Fill the background with white
    screen.fill((238, 238, 238))

    #update snake every frame
    snake.update()
    if snake.eat(food):
        score += 1
        food.newPos()
    snake.collided()
    # Display score board
    message("Score: " + str(score), "orange", (5, 5))

    # screen.blit(food.surf, (food.x, food.y))
    snake.draw()
    food.draw()
    #flip the display screen (use this to update the content)
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(snake_speed)

#Game Over
message("GAME OVER!", "red", "center")
pygame.display.update()
# Quit game here
#time.sleep(1)
pygame.quit()
