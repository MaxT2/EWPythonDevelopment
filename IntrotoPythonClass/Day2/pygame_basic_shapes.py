# pygame basic sprite setup - base of all pygame projects

# import pygame library so we can use it!
import pygame
# import everythong in pygame.draw
from pygame.draw import *

# game code that needs to run only once

# initialize pygame code
pygame.init()

# setup display size
width = 1200
height = 800

# create game surface (the screen we will draw onto)
game_surface = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Window Caption!')

# setup framerate
clock = pygame.time.Clock()
FPS = 10

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


# fill entire screen with color
game_surface.fill(WHITE)


# main game loop
running = True
# when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        # if we close the game window, stop the loop
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame
    # store and print current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print("X = ", mouse_x, "Y = ", mouse_y)

    # limit the frame rate of your game
    clock.tick(FPS)

    # update stuff

    # draw stuff
    # draw all basic shapes

    # line (surface, color, (x,y),(x,y),width(optional))
    line(game_surface, GREEN, (600, 400), (600, 500), 10)

    # circle
    # circle(surface,color,(x,y), radius, width(optional)
    circle(game_surface, GREEN, (300, 200), 100)
    # do another!
    circle(game_surface, GREEN, (900, 200), 100)

    # rectangle
    # rect(surface, color, ((x,y), (width,height), width(optional))
    rect(game_surface, GREEN, [(300, 600), (600, 100)])

    # polygon
    # polygon(surface, color,(x1,y1,x2,y2))
    polygon(game_surface, GREEN, [(10, 10), (20, 20), (20, 40)])

    # lastly: update and redraw entire screen
    pygame.display.flip()
