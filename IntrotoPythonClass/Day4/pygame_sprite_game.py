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
FPS = 10

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#setup sprite groups
all_sprites = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

# create player and enemy sprite objects and add them to groups





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
    # update all sprites in group
    all_sprites.update()
    # draw stuff
    # draw all sprites in group on game_surface
    all_sprites.draw(game_surface)
    # lastly: update and redraw entire screen
    pygame.display.flip()
