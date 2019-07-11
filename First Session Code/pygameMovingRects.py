# import pygame library so we can use it!
import pygame
import random

#initialize pygame
pygame.init()

#setup Game Surface (screen)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
gameSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
FPS = 60
# create game clock
clock = pygame.time.Clock()
# load image file
image1 = pygame.image.load('greatart.png')
image1 = pygame.transform.scale(image1,(100,100))

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

random_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
# Rectangle xpos variable
rect_x = 500
# Speed of x movement
rect_x_speed = 1
# Rectangle ypos variable
rect_y = 500
# Speed of y movement
rect_y_speed = 1

#main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update stuff
    # limit frame rate of game
    clock.tick(FPS)
    # draw background
    # gameSurface.fill(BLACK)
    # update x_position
    rect_x = rect_x + rect_x_speed
    # check to see if the square has left the screen in the x direction
    if rect_x > 1000 or rect_x < 0:
        rect_x_speed = rect_x_speed * -1
        random_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    #update y_position
    rect_y = rect_y + rect_y_speed

    if(x < 0):
        rect_x_speed = rect_x_speed *-1
    if (x > 1200):
        rect_x_speed = rect_x_speed * -1


    x = x + rect_x_speed
    y = y + rect_x_speed




    # check to see if the square has left the screen in the y direction
    if rect_y > 1000 or rect_y < 0:
        rect_y_speed = rect_y_speed * -1
        random_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # draw rectangle
    random_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    # pygame.draw.rect(gameSurface,random_color,[rect_x,rect_y,25,25])
    # draw image
    gameSurface.blit(image1,[rect_x,rect_y])

    # update and redraw screen
    # updates some of the screen
    # pygame.display.update()
    # updates entire screen
    pygame.display.flip()









