# simple snakes game with pygame

#import and initiate pygame
from player import Player
from food import Food
import data
import pygame
import pygame.freetype
import time, random
pygame.init()
#import constants from config
from config import *

#Set up drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake game by Ben')
#Load window icon
icon = pygame.image.load("images/snake.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
background = pygame.transform.scale(pygame.image.load("images/grass2.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
playBTN = pygame.transform.scale(pygame.image.load("images/play-btn.png"), (200, 100))
playBTN = playBTN.convert_alpha()
playBTN_rect = playBTN.get_rect()
playBTN_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)

def message(msg, color, coord, font_size=FONT_SIZE):
    # set font style for rendering
    #font_style = pygame.font.SysFont(None, font_size)
    #font_style = pygame.font.Font("SF Atarian System Extended.ttf", font_size)
    font_style = pygame.freetype.Font("Alone On Earth.otf", font_size)
    msg_surf = font_style.render(msg, color)
    #Custom argument to position the text on the screen
    if coord == "center":
        screen.blit(msg_surf[0], (SCREEN_WIDTH/2 - msg_surf[1].width/2, SCREEN_HEIGHT/2 - msg_surf[1].height/2))
    elif coord[0] == "center":
        screen.blit(msg_surf[0], (SCREEN_WIDTH/2 - msg_surf[1].width/2, coord[1]))
    elif coord[1] == "center":
        screen.blit(msg_surf[0], (coord[0], SCREEN_HEIGHT/2 - msg_surf[1].height/2))
    else:
        screen.blit(msg_surf[0], coord)

def displayScoreboard(scores_board):
    coord = ["center", 250]
    coord_offset = 50
    message("Leaderboard:", "white", coord, 50)
    for scores in scores_board[1:6]: #Loop tru each scores
        # increase coord y with the offset
        coord[1] += coord_offset
        #combine the string
        msg = scores[0] + "    " + scores[1]
        #render the msg
        message(msg, "white", coord, 48)

def main(game_Started = False):
    #Initiate a player object, in this case a snake
    snake = Player(screen)
    food = Food(screen, snake)
    #Variables
    score = 0
    snake_speed = 10
    clock = pygame.time.Clock()
    alive = True
    #Run game until user ask to quit
    running = True
    gameStarted = game_Started
    while running:
        scores_board = data.read("scores.txt")
        while not gameStarted: #MENU
            screen.blit(background, background.get_rect())
            screen.blit(playBTN, playBTN_rect)
            displayScoreboard(scores_board)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        gameStarted = True
                    if event.key == K_RETURN:
                        gameStarted = True
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if playBTN_rect.collidepoint(pos):
                        gameStarted = True
                # if user clicked close button
                if event.type == QUIT:
                    running = False
                    gameStarted = True

        while gameStarted and running:
            while not alive:#Game Over
                #update new score
                if score != 0:
                    data.update(score)
                    score = 0
                message("GAME OVER!", "red", "center", 80)
                message("Press R to restart", "green", ("center", 350), 40)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_r:
                            main(True)
                        elif event.key == K_ESCAPE:
                            gameStarted = False
                            alive = True

            keypressed = [] #UP DOWN LEFT RIGHT
            # Did the user click the window close button?
            for event in pygame.event.get():
                # did the user hit a KEY
                if event.type == KEYDOWN:
                    # if ESCAPE key is pressed
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_LEFTBRACKET and snake_speed > 1:
                        snake_speed -= 1
                    elif event.key == K_RIGHTBRACKET:
                        snake_speed += 1
                    elif event.key == K_s:
                        snake_speed += 20
                    elif event.key == K_UP:
                        keypressed = [1, 0, 0, 0]
                    elif event.key == K_DOWN:
                        keypressed = [0,1, 0, 0]
                    elif event.key == K_LEFT:
                        keypressed = [0, 0, 1, 0]
                    elif event.key == K_RIGHT:
                        keypressed = [0, 0, 0, 1]
                # if user clicked close button
                if event.type == QUIT:
                    running = False

            # Fill the background with white
            screen.blit(background, background.get_rect())
            #update snake every frame
            snake.update(keypressed)
            #if the snake ate a food increment score and change food position
            if snake.eat(food):
                score += 1
                # increase snake speed every 5 food eaten
                if score % 5 == 0: snake_speed += 1
                food.newPos()
            #if the snake collided, game over
            if snake.collided():
                alive = False

            # Draw snake and food
            snake.draw()
            food.draw()
            # Display score board
            message("Score: " + str(score), "yellow", (5, 5))
            message("Speed: " + str(snake_speed), "yellow", ("center", 5))
            #flip the display screen (use this to update the content)
            #pygame.display.flip()
            pygame.display.update()
            clock.tick(snake_speed)

    # Quit game here
    pygame.quit()
    quit()
main()
