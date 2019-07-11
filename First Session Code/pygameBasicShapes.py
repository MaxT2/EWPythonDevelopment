# import pygame library so we can use it!
import pygame

#initialize pygame
pygame.init()

#setup Game Surface (screen)
gameSurface = pygame.display.set_mode((1000,1000))

#setup game resources
#color definitions
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (82,245,255)

#main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #start of update process
    #fill screen with a color
    gameSurface.fill(WHITE)

    #draw a circle
    pygame.draw.circle(gameSurface,BLUE,(300,300),100)
    pygame.draw.circle(gameSurface,BLUE,(700,300),100)

    #draw a line
    pygame.draw.line(gameSurface,BLUE,(400,600),(600,600),20)

    #draw a rectangle
    pygame.draw.rect(gameSurface, BLACK, (60,120,80,300))

    #draw polygon
    pygame.draw.polygon(gameSurface, BLACK, ())


    # update and redraw screen
    # updates some of the screen
    pygame.display.update()
    # updates entire screen
    # pygame.display.flip()