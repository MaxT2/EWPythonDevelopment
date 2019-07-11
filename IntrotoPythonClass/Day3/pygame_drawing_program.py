# what is a drawing program, what can you do?
# you can draw
# how?
# with the mouse, when you click
# what else can you do...
# change color of drawing tool ( with keyboard!)
# erase ( with mouse!)
# clear screen ( with keyboard!)

# if enough time
# change the size of the drawing implement using a variable


# step
# how do we draw a circle where the mouse is
# how do we only draw when we are pressing the mouse button
# how do we erase

# pygame basic sprite setup - base of all pygame projects

# import pygame library so we can use it!
import pygame
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
FPS = 60

# setup game resources
# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (235, 235, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (65, 231, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# list of colors for drawing
colors = [GREEN, PURPLE, YELLOW, BLUE]
#           0       1      2       3
# Current color position
color_position = 0

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


        # check keyboard inputs
        elif event.type == pygame.KEYDOWN:

            # clear screen
            if event.key == pygame.K_SPACE:
                # fill the screen with white
                game_surface.fill(WHITE)

            # if 1 key is pressed
            if event.key == pygame.K_1:
                # set color position to 0 ( green)
                color_position = 0

            # if 1 key is pressed
            if event.key == pygame.K_2:
                # set color position to 1 ( purple)
                color_position = 1

            # if 1 key is pressed
            if event.key == pygame.K_3:
                # set color position to 2 ( yellow)
                color_position = 2

            # if 1 key is pressed
            if event.key == pygame.K_4:
                # set color position to 3 ( blue)
                color_position = 3

    # game code that repeats every frame
    # store and print current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print("X = ", mouse_x, "Y = ", mouse_y)

    # limit the frame rate of your game
    clock.tick(FPS)

    # update stuff

    # draw stuff
    # only draw when left mouse clicked
    if pygame.mouse.get_pressed() == (1, 0, 0):
        # draw circle where mouse is
        circle(game_surface, colors[color_position], (mouse_x, mouse_y), 15)

    # check if right mouse button is pressed
    if pygame.mouse.get_pressed() == (0, 0, 1):
        # draw a white circle where the mouse is
        pygame.draw.circle(game_surface, WHITE, [mouse_x, mouse_y], 20)

    # lastly: update and redraw entire screen
    pygame.display.flip()
