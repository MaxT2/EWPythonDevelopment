# pygame basic sprite setup - base of all pygame projects

# import pygame library so we can use it!
import pygame

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


# fill entire screen with color
game_surface.fill((255, 255, 255))


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
    # limit the frame rate of your game
    clock.tick(FPS)

    # print mouse position for easy shape placement
    #store mouse positions



    print(pygame.mouse.get_pos())

    # update stuff

    # draw stuff

    # lastly: update and redraw entire screen
    pygame.display.flip()
