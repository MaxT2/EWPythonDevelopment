# import pygame library so we can use it!
import pygame
from pygame.locals import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources
# color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (235,235,235)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (65,231,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)


def draw_house(x, y, width, height, screen, color):
    points = [(x, y - ((2 / 3.0) * height)), (x, y), (x + width, y), (x + width, y - (2 / 3.0) * height),
              (x, y - ((2 / 3.0) * height)), (x + width / 2.0, y - height), (x + width, y - (2 / 3.0) * height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)


# main game loop
running = True #when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill entire screen
    gameSurface.fill(255)
    draw_house(200,500, 500,500,gameSurface,RED)





    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()



