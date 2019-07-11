# import pygame library so we can use it!
import pygame
import random
from pygame.locals import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

gameSurface = pygame.display.set_mode((display_width, display_height))
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
# rectangle variables
rectX = 500
rectY = 500
rectXSpeed = 1.13
rectYSpeed = .8

# rect color
r_color = random.randint(100,255),random.randint(100,255),random.randint(100,255)

# load image file
image1 = pygame.image.load('hoodie.png')
image1 = pygame.transform.scale(image1, (56, 72))



# fill entire screen with color
gameSurface.fill(BLACK)


# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame
    # clear display (redraw background)
    # gameSurface.fill(BLACK)


    # update
    rectX += rectXSpeed
    rectY += rectYSpeed

    # if you hit the left or right side
    if rectX > display_width or rectX < 1:
        # reverse x direction
        rectXSpeed *= -1
        # set random color when it hits a side
        r_color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)

    # if you hit the top or bottom side
    if rectY > display_height or rectY < 1:
        # reverse y direction
        rectYSpeed *= -1
        # set random color when it hits a side
        r_color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)

    # set random cover every frame
    # r_color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)

    # draw
    # pygame.draw.rect(gameSurface, r_color, [rectX, rectY, 25, 25])
    # pygame.draw.circle(gameSurface,r_color,(int(rectX),int(rectY)),25)
    gameSurface.blit(image1, [rectX, rectY])


    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
