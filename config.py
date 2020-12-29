# Define constants for the screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SNAKE_SIZE = (20, 20) #XY
# SNAKE_COLOR = (0, 200, 0) #RGB
SNAKE_COLOR = (12, 186, 104) #RGB
SNAKE_BLOCK = 20 #pixels between each move / frame update
SNAKE_ORIGIN = (0, 0)

FOOD_COLOR = (200, 200, 0)
FOOD_SIZE = (20, 20)

FONT_SIZE = 25

# Constants (Used for bitwise operations - https://www.tutorialspoint.com/python/bitwise_operators_example.htm)
UP    = 0b0001
DOWN  = 0b0010
LEFT  = 0b0100
RIGHT = 0b1000
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
