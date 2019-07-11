# import pygame library so we can use it!
import pygame

# initialize pygame
pygame.init()

# setup Game Surface (screen)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
gameSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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
# fill background with white once at the beginning
gameSurface.fill(WHITE)

# main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check keyboard inputs
        elif event.type == pygame.KEYDOWN:

            # clear screen
            if event.key == pygame.K_SPACE:
                # fill the screen with white
                gameSurface.fill(WHITE)

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



    # get current mouse positions
    mouseX, mouseY = pygame.mouse.get_pos()

    # check if left mouse button is pressed
    if pygame.mouse.get_pressed() == (1, 0, 0):
        # draw a circle where the mouse is
        pygame.draw.circle(gameSurface, colors[color_position], [mouseX, mouseY], 20)

    # check if right mouse button is pressed
    if pygame.mouse.get_pressed() == (0, 0, 1):
        # draw a white circle where the mouse is
        pygame.draw.circle(gameSurface, WHITE, [mouseX, mouseY], 20)

    # update and redraw screen
    # updates some of the screen
    # pygame.display.update()
    # updates entire screen
    pygame.display.flip()
