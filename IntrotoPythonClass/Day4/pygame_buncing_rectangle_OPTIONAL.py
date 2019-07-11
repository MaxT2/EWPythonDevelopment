# pygame basic sprite setup - base of all pygame projects
# get a shape on the screen with x y variables
# move it by changing x or y every frame in our update code


# import pygame library so we can use it!
import random

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
FPS = 30

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# to move stuff on the screen we need to store its positon and change it over time
x_position = 400
y_position = 400

x_speed = 10
y_speed = 30

# color variable
draw_color = (255, 0, 0)

# define rectangle shape to draw
rect_1 = pygame.Rect((0, 0), (25, 25))

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
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # print("X = ", mouse_x, "Y = ", mouse_y)

    # limit the frame rate of your game
    clock.tick(FPS)

    # update stuff

    # X AXIS CHECKS
    # if the rectangle hits the right wall (x = width)
    if rect_1.right > width:
        # change direction in the x axis
        x_speed *= -1
        draw_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # if the rectangle hits the left wall (x = 0)
    if rect_1.left < 0:
        # change direction in the x axis
        x_speed *= -1
        draw_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # Y AXIS CHECKS
    # if the rectangle hits the right wall (x = width)
    if rect_1.bottom > height:
        # change direction in the x axis
        y_speed *= -1
        draw_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # if the rectangle hits the left wall (x = 0)
    if rect_1.top < 0:
        # change direction in the x axis
        y_speed *= -1
        draw_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # update our squares position
    # x_position = x_position + x_position
    x_position += x_speed
    y_position += y_speed

    # draw stuff

    # draw a background each frame before drawing everything else
    # game_surface.fill(WHITE)

    # draw our shape on the screen

    # set the center of the shape to our x and y positions
    rect_1.center = (x_position, y_position)
    # draw rectangle on screen
    rect(game_surface, draw_color, rect_1)

    # lastly: update and redraw entire screen
    pygame.display.flip()
