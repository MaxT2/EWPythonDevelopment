# import pygame library so we can use it!
import pygame
import random
from pygame.locals import *
from pygame.draw import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

game_surface = pygame.display.set_mode((display_width, display_height))

# setup resources
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (235, 235, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (65, 231, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# setup for text
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Python Rocks", True, BLACK)

# main game loop
# when running is True game loop will run
running = True
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # do game stuff
    # fill entire screen with a color
    game_surface.fill(WHITE)

    # rcolor = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
    # screen.fill(rcolor)

    # drawing shapes
    # (displayReference,color,location,size)
    # cirlces!
    circle(game_surface, BLACK, (300, 300), 75)
    circle(game_surface, BLACK, (700, 300), 75)

    # lines
    line(game_surface, BLACK, (400, 700), (600, 700), 20)

    # rectangles
    rect(game_surface, BLACK, Rect((500, 550), (50, 50)))
    game_surface.blit(text, [400, 850])

    pygame.draw.polygon(game_surface, BLUE, ((100, 100), (400, 50), (800, 100)), 0)

    # rect and square
    # polygon maybe?

    # update and redraw entire screen
    pygame.display.flip()
    # delay to slow random change. Wont work for a game
    pygame.time.delay(300)
