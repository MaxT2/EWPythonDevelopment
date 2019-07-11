# import pygame library so we can use it!
import pygame

#initialize pygame
pygame.init()

#setup Game Surface (screen)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
gameSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#setup game resources
#color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (235,235,235)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (65,231,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

#main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update and redraw screen
    # updates some of the screen
    # pygame.display.update()
    # updates entire screen
    pygame.display.flip()