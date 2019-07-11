# Challange!
# using basic shapes draw a house on the screen!

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
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (235,235,235)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (65,231,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

# fill background with color
gameSurface.fill(GRAY)

# triangle roof (do this with them probably)
t1 = (500, 100)
t2 = (150, 350)
t3 = (850, 350)


pygame.draw.polygon(gameSurface, GREEN, (t1, t2, t3))

# square house
rect1 = pygame.Rect(150, 350, 700, 400)
pygame.draw.rect(gameSurface, BLUE, rect1)


# square window
rect2 = pygame.Rect(200, 450, 150, 150)
pygame.draw.rect(gameSurface, RED, rect2)

rect3 = pygame.Rect(650, 450, 150, 150)
pygame.draw.rect(gameSurface, YELLOW, rect3)

# rectangular door
rect4 = pygame.Rect(425, 450, 150, 300)
pygame.draw.rect(gameSurface, PURPLE, rect4)

# doorknob
pygame.draw.circle(gameSurface,BLACK,(550,625),10)

# extras if you finnished
# color everything the way you want it
# add foreground and backgroud (grass and sky?)
# add a sun or moon

# update and redraw entire screen
pygame.display.flip()

# main game loop
running = True #when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


