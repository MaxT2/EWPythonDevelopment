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

# setup for text on screen
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Python Rocks!", True, PURPLE, GREEN)

# main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with WHITE
    gameSurface.fill(WHITE)

    # draw triangle roof
    pygame.draw.polygon(gameSurface, BLUE, ((500, 100), (150, 350), (850, 350)))
    # draw rect of house
    # rect(surface,color,(xpos,ypos,width,height))
    pygame.draw.rect(gameSurface, GRAY, (150, 350, 700, 500))

    # draw the text
    gameSurface.blit(text, [500, 200])

    # update and redraw screen

    # updates some of the screen
    # pygame.display.update()
    # updates entire screen
    pygame.display.flip()
