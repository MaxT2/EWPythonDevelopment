# import pygame library so we can use it!
import pygame
import math

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

game_surface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

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

# game code that needs to run only once
# fill entire screen with color
game_surface.fill(255)

# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame


    for i in range(20):
        radians_x = i / 20
        radians_y = i / 6

        x = int(400 * math.sin(radians_x)) + 500
        y = int(400 * math.cos(radians_y)) + 500

        pygame.draw.line(game_surface, BLACK, [x, y], [x + 5, y], 5)

    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
